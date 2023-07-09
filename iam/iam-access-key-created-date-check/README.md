# IAM Access Key Created Date Check

## 概要
任意のIAMユーザーのIAMアクセスキーの作成日時を確認する

## 使用方法
```
python iam-access-key-created-date-check.py <IAMユーザー名>
```

実行例
```
$ python iam-access-key-created-date-check.py demo-user
2023-07-09 11:39:15+09:00
```

存在しないIAMユーザーを指定した場合
```
$ python iam-access-key-created-date-check.py demo-user1
存在しないIAMユーザーです
```
