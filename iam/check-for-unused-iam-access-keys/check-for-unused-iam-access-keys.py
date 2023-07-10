# Check IAM access keys that have not been used for more than a specified number of days
import boto3


# get iam users list
def get_iam_users():
    iam_client = boto3.client("iam")

    response = iam_client.list_users()
    iam_user_list = [user["UserName"] for user in response["Users"]]
    return iam_user_list


if __name__ == "__main__":
    print(get_iam_users())
