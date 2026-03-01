+++
title = "React - サーバーとの通信"
weight = 7
sort_by = "weight"
[extra]
+++
## サーバーとの通信

※この投稿ではAxiosを使用せず、FetchとFormDataのみを利用して実装しました

### REST API

#### 定義

- 2台のコンピュータがインターネットを通じて情報を交換するために使用する通信方式（インターフェース）

##### RESTとは？

- Representational State Transferの略称で、ネットワークにおけるデータの伝送／処理を定義したソフトウェアアーキテクチャを指す。- これを用いることで、大規模システム／マルチプラットフォームにおいても安定した通信の実現と修正が可能となる。

利点

拡張性

- RESTはクライアントとサーバー間の相互作用を担当するため、パフォーマンスの向上と拡張性において利点を提供する。

柔軟性

- RESTfulサービスは完全なクライアント-サーバー分離をサポートし、サーバー側のプラットフォーム/技術変更がクライアントに影響を与えないという柔軟性を提供する。- サーバーとクライアントの完全な分離により、アプリケーションを変更することなくDB層の変更などが可能となる。

##### 独立性

- REST APIは使用される技術とは独立して動作するため、様々なプログラミング言語でアプリケーションの実装が可能であり、通信に影響を与えずに技術の変更が可能である。

#### 構成

固有リソース識別子

- 各リソースを一意に識別するためにURLを使用する- **例)** http://testsite.com/posts/post1

メソッド

種類

- **GET** - サーバーからデータを受け取る際に使用 - **例)** ログインおよび投稿情報の取得 - **POST** - サーバーに新しいデータを追加する際に使用 - **例)** 会員登録および新規投稿の作成
- **PUT** - 既存のデータを変更する際に使用 - **例)** ユーザーデータの変更、記事の修正 - **DELETE** - サーバー上のデータを削除する際に使用 - **例)** 会員の退会、記事/コメントの削除

##### HTTPヘッダー

- HTTPメソッドが動作するためのデータ - リクエスト方式、認証情報、コンテンツタイプなどの情報を含んでいる。

パラメータ

- パスパラメータ（**URL**）- リソースに関する追加情報を要求するクエリパラメータ- クライアントを迅速に認証するクッキーパラメータ

#### 応答の構成

##### ステータスバー

二百

- **応答成功**を意味する

###### 201

- **POSTメソッドの応答成功**を意味する

###### 4XX

- **サーバーが処理できない不正なリクエスト**を意味する

404

- **リソースの探索不可**を意味する

##### メッセージ本文

- リソース表現を含むメッセージを指し、通常はXMLやJSONの形式で返される

  以下は上記に対するJSON形式のサンプルデータである

~~~json { "id":"testId1", "pwd":"testPwd1", "userName":"testUserName1" } ~~~

ヘッダー

- 応答に対するヘッダー／メタデータなどが該当し、エンコーディングや日付、コンテンツタイプなどの情報を含む

必要な要素

フェッチ

##### 定義

- JavaScriptの組み込みライブラリであり、非同期でサーバーとの通信を担当する。[^1]

#### FormData

##### 定義

- フォームフィールドと同様の方法でキー/値のデータを扱うためのオブジェクト- **XMLHttpRequest.send()** メソッドを利用して、データの送信が可能- GET送信の場合、URLSearchParamsコンストラクタに直接渡す方式で使用可能

メソッド

- **FormData.append()**: キーが存在する場合はそのキーに新しい値を追加し、キーが存在しない場合はキーと値を新たに追加する。- **FormData.delete()**: FormDataオブジェクトからキー/値ペアを削除する。- **FormData.entries()**: すべてのキー/値ペアを取得できるイテレータを返す。
- **FormData.get()**: 条件を満たす最初のキーの値を返す - **FormData.getAll()**: 条件を満たす全てのキーの値を配列で返す - **FormData.has()**: 特定のキーが存在するかどうかをブール値で返す
- **FormData.keys()**: すべてのキーに対するイテレータを返す- **FormData.set()**: 既存の値に新しい値を設定するか、新しいキー/値ペアを追加する- **FormData.values()**: すべての値に対するイテレータを返す

##### 使用方法

react const formData = new FormData(); //新しいFormDataオブジェクトを作成formData.append('id', 'tId1');formData.append('id', 'tId2'); //id=tId1, id=tId2のような形式で値を保存する

formData.get("id"); //最初の値であるtId1のみを返す


//送信のサンプルコードfetch('/url',{ method: "POST", body: formData });

1. new FormData() を使用して、新しい FormData を作成する2. append()/get() メソッドを使用して、値の追加/取得/変更が可能である3. 上記のサンプルコードのように、fetch や response などを使用して、FormData オブジェクトの送信が可能である

より詳細な内容は、こちらの[リンク](https://ko.javascript.info/formdata)を参照してください。

コース

#### 定義

- Cross-Origin-Resource-Sharingの略称で、ウェブページから他のサイトにアクセスできるようにする仕組みを意味する。

- JavaScriptでは、セキュリティ上の理由から異なるドメインへのリクエストを制限している（同一オリジンポリシー）。これを解決するには、CORSを設定する必要がある。

  - CORSが存在しない場合、他のアプリケーションからの偽のクライアントリクエスト送信などのセキュリティ上の問題が発生する可能性がある

- CORSの動作は次の通りである。

  1. ブラウザは、現在のプロトコル、ホスト、ポートの情報を含むオリジンヘッダーをリクエストに追加する。2. サーバーは現在のオリジンのヘッダーを確認し、要求されたデータとAccess-Control-Allow-Originヘッダーで応答する。
  3. ブラウザはアクセス制御リクエストヘッダーを確認後、返されたデータをクライアントアプリケーションと共有する。4. サーバーでクロスオリジンアクセスが許可されていない場合、エラーメッセージを返す。

  同一オリジンポリシー

  - ブラウザでは、クライアントが同一オリジン（origin）のリソースのみへのリクエストを許可する。- クライアントのURLのプロトコル、ポート、ホストが、クライアントがリクエストするサーバーと全て一致する場合にのみ、リクエストが許可される。- 例）クライアントURL : http://127.0.0.1:3000

  | URL | 成功可否 | 種類 | 失敗理由 | | -------------------------------- | :-------: | :---------: | :---------: | | http://127.0.0.1:3000/login.html | O | 同一オリジン | |
  | http://127.0.0.1:4000/main.html | X | 異なるオリジン | 異なるポート | | http://126.0.0.1:3000/main.html | X | 異なるオリジン | 異なるホスト |

  - 上記の例のように、同一のホストとポートを持つhttp://127.0.0.1:3000/login.html에서는クライアントが要求するサーバーが同一であるため、クライアントの要求に対してエラーなく正常に処理される。
  - しかし、http://127.0.0.1:4000/main.html은 はホストのみが同一で、**ポート**が異なり、http://126.0.0.1:3000/main.html는 クライアントとは**ホスト**が異なるため、クライアントのリクエストは正常に処理されない。

メソッド

##### アクセス制御 - 許可されたオリジン

- 特定のオリジンからのリクエストを許可する設定 - **⁎**: 全てのオリジンからのアクセスを許可

###### 使用方法

react Access-Control-Allow-Origin: URL

//例 header('Access-Control-Allow-Origin: http://127.0.0.1:3000'); ~~~

##### アクセス制御許可メソッド

- サーバーで許可するメソッドのリストを設定すること - GET、POST、PUT、DELETEなどが使用可能[^2]

###### 使用方法

react Access-Control-Request-Method: method

//예시header("Access-Control-Allow-Methods: POST");

##### Access-Control-Allow-Headers

- 許可されるヘッダーの一覧を設定すること

###### 使用方法

react Access-Control-Request-Headers: ヘッダータイプ

//예시header("Access-Control-Allow-Headers: Content-Type");







#### CORS事前リクエスト

- CORS相互作用において、一部のHTTPリクエストは複雑であるため、実際のリクエスト送信前にメソッドとヘッダーの確認を行う。- 一般的な状況では自動的に発生するが、単純なリクエストは事前実行リクエストが省略される。- 2～3つの構成でリクエストを送信し、Access-Control-Request-MethodとOriginを必須で受け取り、Access-Control-Request-Headersを選択的にリクエストする。

##### 動作方式

- 例）DELETE方式でリクエストがあった場合1. DELETEリクエストを行う前に、事前リクエストを通じてサーバーがDELETEを許可するかどうかを確認する2. サーバーがDELETEを許可する場合、Access-Control-Allow-MethodsにDELETEを含めて事前リクエストに応答する。



<br><br><br><br><br><br><br><br><br><br><br>

---

参考資料

- [RESTful APIとは何ですか？](https://aws.amazon.com/ko/what-is/restful-api/)

- [FormData](https://developer.mozilla.org/ko/docs/Web/API/FormData)

- [悪名高いCORSの概念と解決法 - まとめの最終版](https://inpa.tistory.com/entry/WEB-%F0%9F%93%9A-CORS-%F0%9F%92%AF-%EC%A0%95%EB%A6%AC-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95-%F0%9F%91%8F)

- [Access-Control-Request-Method](https://developer.mozilla.org/ko/docs/Web/HTTP/Reference/Headers/Access-Control-Request-Method)

  <br><br><br><br><br><br><br><br><br><br><br>

[^1]: [fetch]({{ site.baseurl }}/posts/비동기와-동기화)の詳細についてはリンクを参照してください。

[^2]: HTTPリクエストメソッドに関する詳細情報は[リンク](https://developer.mozilla.org/ko/docs/Web/HTTP/Reference/Methods)を参照してください。

