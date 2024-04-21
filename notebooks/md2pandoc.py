import re

def convert_markdown_to_pandoc(input_file, output_file):
    # Markdownファイルの読み込み
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    # MarpのMarkdownからPandocのMarkdownに変換
    pandoc_text = convert_marp_to_pandoc(markdown_text)

    # 変換結果を出力ファイルに保存
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(pandoc_text)

def convert_marp_to_pandoc(markdown_text):
    # ヘッダーレベルの変換
    pandoc_text = re.sub(r'^(#{1,6})\s', r'\1# ', markdown_text, flags=re.MULTILINE)

    # リストの変換
    pandoc_text = re.sub(r'^( *)(-|\+|\*) ', r'\1* ', pandoc_text, flags=re.MULTILINE)

    # リンクの変換
    pandoc_text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'[\1](\2)', pandoc_text)

    # 画像の変換（PandocではHTMLタグが認識される）
    pandoc_text = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', pandoc_text)

    return pandoc_text

# # Markdownファイルと出力ファイルを指定して変換を行う
# input_file = "input.md"      # 入力ファイル（MarpのMarkdown）
# output_file = "output.md"    # 出力ファイル（Pandocが認識する形式）

# convert_markdown_to_pandoc(input_file, output_file)
