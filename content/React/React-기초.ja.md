+++
title = "React基礎"

weight = 7
sort_by = "weight"

[extra]
+++
## React

### 定義

- Reactは、UI構築のためのJavaScriptベースのWeb開発用ライブラリであり、コンポーネントを組み合わせてアプリを作成できるように支援するツールです。

### 特徴

1. 独立した再利用可能なコンポーネントの使用

- 独立した再利用可能なコンポーネントを用いてUIをモジュール化する

##### 2. 効率性向上のためのVDOMの使用

- 効率性を高めるために**VDOM**[^1]という概念を使用する

3. コンポーネントが複数の要素を返す場合の上位要素の使用

- コンポーネントが複数の要素を返す場合、親要素内に要素を配置する必要がある- 親要素としては**div**などを使用可能- 例コード

react関数 App(){ return( <div> <h1> Hello, World </h1> <p>初めてのReactベースのWebページ</p> </div> ); }

**さらに簡略化されたバージョン**

react //フラグメント使用function App {    return(        <React.Fragment>            <h1>Hello, World</h1>            <p>初めてのReactベースのWebページ</p>        </React.Fragment>    );}


//さらに簡略化されたフラグメント版function App{    return(        <>        <h1>Hello, World</h1>        <p>初めてのReactベースのWebページ</p>    </>);}

- 上記のコードはReact 16.2バージョンから使用可能である

4. コンポーネントの構成方式

- Reactでコンポーネントを構成する際には、クラスと関数を利用した2つの方法がある

  1. **関数方式**

     - 関数で構成する場合、return文は必須であり、コンポーネントの表示方法を決定する

     - サンプルコード

  react関数 App(){    return <h1> Hello, World </h1>}

  2. **クラス方式** - クラスで構成する場合、**render()**メソッドが必要となる - render()メソッドはコンポーネントのレンダリング結果を表示・更新する役割を担う - 例示コード

  ~~~react class App extends React.Component{ render() } ~~~
  
  

<br/><br/><br/><br/><br/>

### 参考にした本

[実践！Spring BootとReactで始めるモダンWebアプリケーション開発](https://www.yes24.com/Product/Goods/119973506).

---







[^1]: Visual Document Object Model（ビジュアル ドキュメント オブジェクト モデル）

