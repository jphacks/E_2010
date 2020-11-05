# Lunch Link Learning


[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2020/09/JPHACKS2020_ogp.jpg)](https://www.youtube.com/watch?v=G5rULR53uMk)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
### 製品説明（具体的な製品の説明）
### 特長
####1. 特長1
####2. 特長2
####3. 特長3

### 解決出来ること
### 今後の展望
### 注力したこと（こだわり等）
* 
* 

## 開発技術
### 活用した技術
#### API・データ
* 
* 

#### フレームワーク・ライブラリ・モジュール
* 
* 

#### デバイス
* 
* 

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
* 
* 

## 開発
* Django
First time

```
pip install -r requirements.txt
```

1. Migration
```
mysql -u<username> -p<password>
mysql> create database lunch;

python3 manage.py migrate
```

2. install package (js)
```
cd frontend/lunch-frontend
npm install
```

2. build react
```
cd frontend/lunch-frontend
npm run-script build
```

3. Run
```
python3 manage.py runserver
```

4. Access
```
curl http://localhost:8000
curl http://localhost:8000/admin
curl http://localhost:8000/api/users/
curl http://localhost:8000/api/users/1/
```
- admin ページにはスーパーユーザが必要
```
python manage.py createsuperuser
```

- デプロイ
  - https://qiita.com/frosty/items/66f5dff8fc723387108c
  - アプリ消した後同じ名前のものをすぐ作るとおかしくなる（設定が残ったままになってる？）
  - `heroku apps:destroy --app <appname>`
