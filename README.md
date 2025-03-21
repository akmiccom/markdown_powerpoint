# markdownからpptxを作成する手順を考えてみた

## 参考にしたサイト

- [Pandoc User’s Guide 日本語版](https://pandoc-doc-ja.readthedocs.io/ja/latest/users-guide.html#slide-shows)
- [Marp for VS Codeを使ったMarkdownによるスライド作成入門](https://zenn.dev/oyashiro846/articles/0deab8230432a5)
- [Marpの見た目を調整する際の備忘録](https://zenn.dev/aikige/articles/marp-layout-tips)
- [What? Slides? From Markdown?](https://stymied.medium.com/what-slides-from-markdown-5239ed31e7ac)
- [R Markdown: The Definitive Guide](https://bookdown.org/yihui/rmarkdown/)
- [Markdownから直接PowerPointを作成する](https://yyhhyy.hatenablog.com/entry/2019/10/22/100000)
- [Marp入門〜応用｜markdownでプレゼン資料を楽に素早く作って発表しよう](https://zenn.dev/cota_hu/books/marp-beginner-advanced/viewer/intro)

## なぜこんなことを考えたのか？

最近会社のpptxのスライドマスターが更新されたのでこれを機会に色々試したいなと考えました。

まずは、markdown で資料を作成することで手間を減らせるかも、また数式を書く機会が多いのてそれは pptx では大変であ。ったことが思いつきます。

## 色々しらべてやるべきことを整理

- markdown で資料を作成
- marp でプレビュー確認
- marp に既定のcssをあてる
- pandoc で pptx を出力電圧
- pandoc で pptx にマスターをあてる
- 通常通り作成したようにして完成

## 基本方針

- markdown + Marp でスライドを見ながら作成
- pandoc を使って pptx で出力
- 規定のスライドマスターで保存

## 調べたこと

- marp の使い方
- pandoc の使い方
- css の作り方
- pptx のマスターレイアウトの設定
- 参照レイアウトの設定

## それぞれをまとめておく

- marp の使い方
- pandoc の使い方
- css の作り方
- pptx のマスターレイアウトの設定
- 参照レイアウトの設定

## PowerPointのレイアウト選択

スライドを作成する際、pptxライターはスライドの内容に基づいていくつかの事前定義されたレイアウトから選択します：

- タイトル スライド

このレイアウトは、メタデータフィールドである日付、著者、タイトルが存在する場合に、初期スライド用に使用されます。

- セクション見出し

このレイアウトは、pandocが「タイトルスライド」と呼ぶものに使用されます。つまり、スライドの階層より上の位置にヘッダーがあるスライドです。

- 2 つのコンテンツ

このレイアウトは、少なくとも2つのdivクラスで構成されたdiv（クラス：columns）を含むスライドに使用されます。

- 比較

このレイアウトは、「2つのコンテンツ」と異なり、少なくとも1つの列にテキストの後に非テキスト（例：画像や表）が続く場合に使用されます。

- コンテンツとキャプション

このレイアウトは、テキストの後に非テキスト（例：画像や表）が続く非2列のスライドに使用されます。

- 空白

このレイアウトは、白紙のコンテンツのみを含むスライドに使用されます。例えば、スピーカーノートのみを含むスライドや、非改行スペースのみを含むスライドなどです。

### タイトルとコンテンツ

このレイアウトは、他のレイアウトの基準に一致しないすべてのスライドに使用されます。

これらのレイアウトは、pandocに含まれるデフォルトのpptxリファレンスドキュメントから選択されます。ただし、--reference-docを使用して別のリファレンスドキュメントを指定した場合は、その代わりに選択されます。

## pandoc command

- markdown を powerpoint に変換する方法
pandoc input.md -t pptx -o output.pptx

- スライドを参照したいときの使い方
pandoc -s hoge.md -o hoge2.pptx --reference-doc=hogehoge.pptx
