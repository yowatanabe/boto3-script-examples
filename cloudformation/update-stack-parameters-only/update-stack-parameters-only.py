import boto3

client = boto3.client("cloudformation")

# 更新するスタック名のリスト
cfn_stack_name_list = [
    "stack1",
    "stack2",
    "stack3",
]

# スタックのパラメータのみ更新
for cfn_stack_name in cfn_stack_name_list:
    try:
        response = client.update_stack(
            StackName=cfn_stack_name,
            UsePreviousTemplate=True,
            Parameters=[
                {
                    "ParameterKey": "InstanceType",
                    "ParameterValue": "t2.micro",
                },
                {
                    "ParameterKey": "Name",
                    "UsePreviousValue": True,
                },
                {
                    "ParameterKey": "Environment",
                    "UsePreviousValue": True,
                },
            ],
        )
        print(f"成功 {cfn_stack_name}: {response}")
    except Exception as e:
        print(f"失敗 {cfn_stack_name}: {e}")


# スタックのステータス確認
for cfn_stack_name in cfn_stack_name_list:
    try:
        response = client.describe_stacks(
            StackName=cfn_stack_name,
        )
        StackStatus = response["Stacks"][0]["StackStatus"]
        print(f"{cfn_stack_name}のステータス: {StackStatus}")
    except Exception as e:
        print(f"失敗 {cfn_stack_name}: {e}")
