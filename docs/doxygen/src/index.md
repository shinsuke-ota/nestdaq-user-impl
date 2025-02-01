# NestDAQ User Implementation (by SPADI Alliance) についてのまとめ自動化トライアル {#maingpage}

## 注意

内容については最新版を使っていますが、このページは非公式なのでリンクなどはご遠慮ください。
（個人のブックマーク程度にとどめてください）

## 成果物

- [ヘッダのまとめ](header-summary.md)

## 応用

- 他のビットフィールドを記述するのにも使ってもらえると思います。
- json ファイルを記述すれば対応したビットフィールドを作成します。
- 現在(2025/02/01)は github の [shinsuke-ota/nestdaq-user-impl](https://github.com/shinsuke-ota/nestdaq-user-impl/tree/restructure) の restructure branch に格納しています。

## ヘッダのまとめを作成するためにやったこと

### ヘッダーから json ファイルを作成する

github copilot でやってもらいましたが、おそらくコードを準備することも可能ではあるとは思います。ただ、フォーマットが決まっていないので、copilot でなんとなく書いてもらうほうが楽かなとは思いました。正確性は担保されているわけではないので、copilot を使う場合には正しいかどうかをチェックする必要があります。

たとえば copilot にヘッダーファイルを追加しておいて、

「ヘッダーファイルの構造を json スキーマになおしてください。バージョンが含まれる場合にはバージョンに分けて記述してください。v1 についてはすべてのヘッダに共通する部分は別途 header-common.json として括りだして、その内容を参照するようにしてください。」

とか言ってみると作成してくれます。

### json ファイルから画像とまとめの markdown ファイルを作成する

これも copilot でやってもらいましたが、簡単なものから順番に正しい結果を吐き出すように順番に機能を追加していきました。最終的には json スキーマを読みこんで、bit field の絵と、まとめの markdown ファイルを作成することができるようになりました。

docs/header/scripts ディレクトリで sh draw_all.sh を実行すると docs/doxygen/src/header 以下に自動的にファイルが作成されます。

### doxygen で全体をドキュメント化

markdown 単体は見づらいのでやっぱり html 化したいですね。あまり他のツールを知らないので、doxygen でサイト化してみました。設定などはまた後ほどまとめたい（願望）と思います。

docs/doxygen/build で doxygen とすると docs/doxygen/html に作成されます。