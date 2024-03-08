# Notebook
ペンギンハックバックエンド

## 起動
docker-compose up

## データベースのリセット
docker-compose exec oauth_api poetry run python -m api.reset_db