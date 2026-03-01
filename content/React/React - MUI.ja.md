+++
title = "React - MUI"
weight = 7
sort_by = "weight"
[extra]
+++
さらに

### MUIとは？

- GoogleのMaterial Designを実装するオープンソースのReactライブラリである

### 特徴

#### 迅速な製作

- MUIには2500人以上のオープンソース貢献者が参加中である

#### 美しさ

- 基本的なUIプロパティが美しさを提供する

#### 自由な修正

- ライブラリには様々なカスタマイズ機能が提供される

チーム間の協業

- バックエンドとデザイナー間の障壁を減らし、より効果的な協業を可能にする

#### 多様に使用される

- 2014年に始まり、React UIライブラリの中で最大のコミュニティを有している

種類

ボタン

- 単一タブの相互作用を通じてイベントを実行するコンポーネント

- ##### 基本構造

  react import Button from '@mui/material/Button'; //必須function buttonFunc() {    return(        <Button>Text</Button> //基本構造        <Button varient="text">Text</Button> //基本構造
      <Button varient="contained">Contained</Button> //背景が塗りつぶされたデザインのボタン<Button varient="outlined">Outlined</Button> //背景が塗りつぶされたデザインのボタン) }export default buttonFunc;

  ##### ボタン形状

  ###### 収められた

  - 背景が塗りつぶされた形状のボタン

  ###### 概要

  - 外側の枠線だけが塗りつぶされた形状のボタン

  ###### テキスト

  - 単にテキストのみ出力するボタン - 基本値です

  ![画像の代替テキスト](assets/img/React/MUI/default_button_design.png)

  ##### 色

  - **color**属性を使用して指定可能であり、様々なデフォルト色の指定が可能である

    - ###### プライマリ

      - 基本テーマカラー

    - ###### 二次

      - サブテーマの色

    - ###### エラー

      - 赤系の色

    - ###### 警告

      - オレンジ系の色

    - ###### 情報

      - 青系の色

    - ###### 成功

      - 緑系の色

  - **ただし**、カスタムカラーを使用するには、**sx={{color: red}}**のようにsx内部でスタイルを指定する必要がある

  - ###### 例

  react <Button color="error" variant="outlined">エラー</Button> //プリセットカラー<Button variant="outlined" sx={{color:"red"}}>赤いボタン</Button>

  ![画像の代替テキスト](assets/img/React/MUI/button_color.png)

  - 詳細は[こちら](https://mui.com/material-ui/customization/palette/#custom-colors)を参照してください

  ##### サイズ

  - **size** プロパティを使用して指定可能

  - ###### 種類

    - 小 - 中 - 大

    <Button variant="outlined" size='small'>ボタン</Button><Button variant="outlined" size='medium'>ボタン</Button><Button variant="outlined" size='large'>ボタン</Button>

    ![画像の代替テキスト](assets/img/React/MUI/button_size.png)

    <br><br>

  - 追加情報は[こちら](https://mui.com/material-ui/customization/palette/#custom-colors)を参照してください

#### テキストフィールド

- ユーザーの入力を受け付けるタイプのUI

- テキスト／ファイル添付など様々な形式のデータ入力が可能である

- ###### 基本構造

  react <TextField varient="outlined"></TextField>

変異体

  - 輪郭線 - バリエーション省略時のデフォルト値 - 下線デザインの入力欄- 塗りつぶし - 四角形図形の薄いグレー背景色の入力欄- 標準 - 四角形図形の入力欄

- ###### フォームプロパティ

  - ID/パスワードなど入力するデータに関する情報を提供するプロップ - required、disabled、read onlyなどが存在する - **required**: 必須入力 - **disabled**: 入力フィールドを無効化 - **read only**: 入力フィールド内のデータ修正不可

- ##### 検証

  - エラー状態のプロパティとして、ユーザーにデータ型の不一致などのフィードバックを提供できる

- ##### マルチライン（複数行入力）

  - TextFieldをMUI Base TextArea AutoSizeに変更する - **rows**を使用しない場合、高さは入力したデータのサイズに合わせて自動的に調整される - minRows、maxRowsを使用して最小/最大行数の設定が可能である

#### 進捗

- スピナーを利用して、作業の処理中であることを知らせる目的で使用されるプロップである

  - **ただし**、棒状などの形態でもカスタマイズが可能です

- **※注意** - CPU使用率が高く、200msごとに再レンダリングされるため、乱用しない方が良い

- ##### 色

  - secondary、success、inheritなどが存在する

- ##### サイズ

  - buttonとは異なり、pxやremなどを利用してサイズ指定が可能である - **例**

  react <CircularProgress size="20px"/>

- ##### 値

  - プログレスバーの充填度を調整するために使用する

  - 固定状態でプログレスバーを埋めるためには、variantに**determinate**を指定する必要がある

  - **value={値}** を使用して値を指定できる

  - 値にprogressを指定した場合、作業の完了率に応じて値が変化する

    - 例

      react <CircularProgress variant='determinate' value={25} />

##### 線形進捗

- 直線形状のプログレスバー - **LinearProgress**を使用して利用可能

#### ボックス

- 他のコンポーネントを囲むコンテナ型のコンポーネント

- 特定のコンポーネントを囲みスタイルを適用するために主に使用される

- **div** に追加機能を組み合わせた形態のコンポーネントである

- ##### 基本構造

~~~ {% raw %} <Box sx= {{ width: 100, height: 100, borderRadius: 1 m: 2 }} /> {% endraw %} ~~~



- **width**: 幅

- **height**: 高さ

- **m**: 上下左右の余白の長さ

  mの他にmt、mb、ml、mrが存在する

- **borderRadius**: コンポーネントの角丸の半径

#### グリッド

詳細は[こちら]({{ site.baseurl }}/posts/Grid)を参照してください。

---

参考資料

[Material UI - 概要](https://mui.com/material-ui/getting-started/)

[ボタン](https://mui.com/material-ui/react-button/)

[テキストフィールド](https://mui.com/material-ui/react-text-field/)

[進捗](https://mui.com/material-ui/react-progress/#circular-size)

[Box](https://mui.com/material-ui/react-box/)