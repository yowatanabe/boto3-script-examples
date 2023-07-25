# Update stack parameters only

## 概要

- 複数のCloudFormationのスタックのパラメータのみ更新する
- アプリAのEC2、アプリBのEC2など基本的な設計は同じだがCloudFormationのスタックを分けて構築している場合に有効
- 運用手順の1つとして AWS CloudShell のPythonシェルから実行することを想定
- `cfn_stack_name_list`と`Parameters`を使用環境に応じて書き換える
- 意図しない変更を防ぐために変更しないパラメータは`UsePreviousValue`を`True`にしておくことを推奨

## 実行例

```bash
[cloudshell-user@ip-10-2-66-50 ~]$ python3
Python 3.7.16 (default, Mar 10 2023, 03:25:26)
[GCC 7.3.1 20180712 (Red Hat 7.3.1-15)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>>
>>> import boto3
>>>
>>> client = boto3.client("cloudformation")
>>>
>>> # 更新するスタック名のリスト
>>> cfn_stack_name_list = [
...     "stack1",
...     "stack2",
...     "stack3",
... ]
>>>
>>> # スタックのパラメータのみ更新
>>> for cfn_stack_name in cfn_stack_name_list:
...     try:
...         response = client.update_stack(
...             StackName=cfn_stack_name,
...             UsePreviousTemplate=True,
...             Parameters=[
...                 {
...                     "ParameterKey": "InstanceType",
...                     "ParameterValue": "t2.micro",
...                 },
...                 {
...                     "ParameterKey": "Name",
...                     "UsePreviousValue": True,
...                 },
...                 {
...                     "ParameterKey": "Environment",
...                     "UsePreviousValue": True,
...                 },
...             ],
...         )
...         print(f"成功 {cfn_stack_name}: {response}")
...     except Exception as e:
...         print(f"失敗 {cfn_stack_name}: {e}")
...
成功 stack1: {'StackId': '....', 'ResponseMetadata': {'RequestId': '....', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '....', 'date': '....', 'content-type': 'text/xml', 'content-length': '....', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}
失敗 stack2: An error occurred (ValidationError) when calling the UpdateStack operation: No updates are to be performed.
失敗 stack3: An error occurred (ValidationError) when calling the UpdateStack operation: Stack [stack3] does not exist
>>>
>>>
>>>
>>> # スタックのステータス確認
>>> for cfn_stack_name in cfn_stack_name_list:
...     try:
...         response = client.describe_stacks(
...             StackName=cfn_stack_name,
...         )
...         StackStatus = response["Stacks"][0]["StackStatus"]
...         print(f"{cfn_stack_name}のステータス: {StackStatus}")
...     except Exception as e:
...         print(f"失敗 {cfn_stack_name}: {e}")
...
stack1のステータス: UPDATE_IN_PROGRESS
stack2のステータス: UPDATE_COMPLETE
失敗 stack3: An error occurred (ValidationError) when calling the DescribeStacks operation: Stack with id stack3 does not exist
>>>
>>>
>>>
>>> # スタックのステータス確認
>>> for cfn_stack_name in cfn_stack_name_list:
...     try:
...         response = client.describe_stacks(
...             StackName=cfn_stack_name,
...         )
...         StackStatus = response["Stacks"][0]["StackStatus"]
...         print(f"{cfn_stack_name}のステータス: {StackStatus}")
...     except Exception as e:
...         print(f"失敗 {cfn_stack_name}: {e}")
...
stack1のステータス: UPDATE_COMPLETE
stack2のステータス: UPDATE_COMPLETE
失敗 stack3: An error occurred (ValidationError) when calling the DescribeStacks operation: Stack with id stack3 does not exist
>>>
>>>
>>>
>>> exit()
[cloudshell-user@ip-10-2-66-50 ~]$
```
