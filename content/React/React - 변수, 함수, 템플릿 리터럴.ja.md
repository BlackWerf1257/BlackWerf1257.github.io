+++
title = " React - 変数、関数、テンプレートリテラル"
weight = 7
sort_by = "weight"
[extra]
+++
## 変数と定数

定数

#### 定義

- 宣言後に値の変更が不可能な変数

####宣言方法

- const 変数名 = 値 - 例コード

react const CV = 1.23;

特徴

- 宣言後に値の変更は不可能である - **ただし**、オブジェクトや配列の場合は内容の変更が**可能**である

### 変数

#### 定義

- 宣言後に値の変更が可能な値

####宣言方法

- **let** 変数名 = 値 - 例コード

react let CV = 1.23;

### 共通の特徴

- ブロック範囲を持つ

  - {}内部で定数を宣言した場合、ブロック外では呼び出しが不可能である- 下位ブロック内ではアクセスが可能である

  react let varA = 10; if(varA > 10){ console.log(varA); }

<br>

関数

 ###宣言方法

1. 一般的な方法

**function** 関数名(変数名) {}

サンプルコード

react関数 Calc(x) { return x * 2; }

2. 矢印関数

- 注意) ES6から使用可能 - 引数が1つの場合、括弧の省略が可能 - 関数の本体が式である場合、returnは必須ではない - 関数の引数がない場合、()のように空の括弧を指定しなければならない

- 宣言方法: **変数名 = 引数 => 戻り値**

サンプルコード

react //パラメータが一つである場合let Calc = x => x * 2;

//パラメータが複数ある場合let Calc = (a, b) => {    return a * b;}~~~

呼び出し方法

- **関数名(引数);**- 注意) 引数が複数ある場合、引数を括弧内に記述し、**カンマで区切る**必要がある

サンプルコード

~~~react Calc(5) Calc(5,10); ~~~

<br>

## テンプレートリテラル

### 定義

- MDM Webドキュメントによると、テンプレートリテラル(Template Literals)は、組み込み式を許可する文字列リテラル[^1]である。

- JavaScriptで文字列を結合する一般的な方法は、**+**演算子を利用することである。

  - サンプルコード

  reactlet name = {firstName : 'Minsu', lastName : 'Kim'};let greeting = "Hello, " + ${name.firstName}+ ${name.lastName};

- テンプレートリテラルを利用する場合は、**バッククォート(``)**を使用して利用可能である

  - サンプルコード

  reactlet name = {firstName : 'Minsu', lastName : 'Kim'};let greeting = `Hello, ${name.firstName} ${name.lastName}`;

  

---

**参考資料**

[コンポーネント状態](https://ko.legacy.reactjs.org/docs/faq-state.html)

[実践！Spring BootとReactで始めるモダンWebアプリケーション開発](https://www.yes24.com/Product/Goods/119973506).

<br>

<br>

<br>

[^1]: 大きな引用符(")で囲まれた文字の集合

