+++
title = "React - クラスと継承"
weight = 7
sort_by = "weight"
[extra]
+++
## クラス

### 定義

- 他のオブジェクト指向言語におけるクラスと同様に、オブジェクトを生成するためのテンプレート

### 特徴

- フィールド、生成、クラスメソッドが含まれる可能性がある

### 使用方法

- **class** キーワードを使用して宣言する- コンストラクタが必要な場合、**constructor** キーワードを使用して実装可能- 例コード

react //コンストラクタが不要な場合class Person{

}

//コンストラクタが必要な場合class Person{    constructor(){        }}~~~

<br>

### 相続

#### 定義

- あるオブジェクトのプロパティやメソッドを別のオブジェクトが継承して使用すること

#### 使用方法

- **extends** キーワードの使用

  - 'class 子クラス名 extends 親クラス名' の形式で使用する- **注意**- 継承されたクラスでは、コンストラクタで **super** キーワードを使用して親クラスのコンストラクタを呼び出す必要がある- super キーワードで呼び出さない場合、エラーが発生する

- サンプルコード

  react class Person{ constructor(firstName, lastName, age){ this.firstName = firstName; this.lastName = lastName; this.age = age; } }
  
  
  class Child extends Person{    constructor(firstName, lastName, age, hobby, favorite){        super(firstName, lastName, age);    }}~~~

  



---

**参考資料**

[実践！Spring BootとReactで始めるモダンWebアプリケーション開発](https://www.yes24.com/Product/Goods/119973506).