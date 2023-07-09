import sys

import boto3
from pytz import timezone

# コマンドラインの引数を取得
args = sys.argv
iam_user = args[1]


# メイン関数
def iam_access_key_created_date_check(iam_user):
    try:
        client = boto3.client("iam")
        access_key_details = client.list_access_keys(UserName=iam_user)
        key_created_date = access_key_details["AccessKeyMetadata"][0][
            "CreateDate"
        ].astimezone(timezone("Asia/Tokyo"))
    except client.exceptions.NoSuchEntityException:
        return "存在しないIAMユーザーです"

    return key_created_date


if __name__ == "__main__":
    print(iam_access_key_created_date_check(iam_user))
