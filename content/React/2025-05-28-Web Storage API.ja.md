+++
title = "Web Storage API"
weight = 7
sort_by = "weight"
[extra]
+++
## Web Storage API



### 定義

- ウェブのデータをクライアントに保存できるデータ構造- SessionStorageとLocalStorageの2種類が存在する- **キー/値**のペアでデータを保存し、キーに基づいてデータを参照するデータ構造

<br>

種類

#### セッションストレージ

- ブラウザが維持されている間、データを保持するデータ構造- ブラウザを新しく開く場合、データが削除される

#### ローカルストレージ

- sessionStorageと同様だが、ブラウザを再起動してもデータが保持されるデータ構造- 有効期限の制限なく保存が可能であり、キャッシュやローカルストレージデータを消去しなければ削除されない

<br>

### 使用方法

react //データの保存sessionStorage.setItem("キーの名前", データ);localStorage.setItem("キーの名前", データ);

//例sessionStorage.setItem("SboolLogged", isLogged);localStorage.setItem("SboolLogged", isLogged);


//データの取得sessionStorage.getItem("キーの名前");localStorage.getItem("キーの名前");

//例sessionStorage.getItem("SboolLogged");localStorage.getItem("SboolLogged");


//データの削除sessionStorage.removeItem('キーの名前');localStorage.removeItem('キーの名前');

//例sessionStorage.removeItem('キーの名前');localStorage.removeItem('キーの名前');

~~~

<br><br><br><br><br><br><br><br><br><br><br>

---

**参考資料**

[[React] LocalStorage データ保存方法](https://velog.io/@jay_be/React-LocalStorage-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0)