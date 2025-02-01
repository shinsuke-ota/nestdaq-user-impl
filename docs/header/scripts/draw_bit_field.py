"""
@file draw_bit_field.py
@brief Draws a bit field diagram from a JSON schema and outputs it in various formats.
This script reads a JSON schema file and generates a visual representation of the bit fields defined in the schema.
It supports resolving internal and external JSON references and can handle different schema versions.
The output includes a bit field diagram in PDF, PNG, and SVG formats, as well as a Markdown file with property details.
@section usage Usage
@code{.sh}
python draw_bit_field.py <input_file> [--output_dir <output_dir>] [--version <version>]
@endcode
@param input_file Path to the input JSON schema file.
@param output_dir Path to the output directory (default: 'readme-header').
@param version Schema version to use (e.g., v0, v1) (optional).
@section dependencies Dependencies
- json
- matplotlib
- os
- argparse
@section author Author
Shinsuke OTA <ota@rcnp.osaka-u.ac.jp>
@section date Date
2023-10-06
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import argparse

# 引数を解析
parser = argparse.ArgumentParser(description='Draw bit field diagram from JSON schema.')
parser.add_argument('input_file', type=str, help='Path to the input JSON schema file')
parser.add_argument('--output_dir', type=str, help='Path to the output directory', default='readme-header')

#parser.add_argument('output_file', type=str, help='Path to the output diagram file')
parser.add_argument('--version', type=str, help='Schema version to use (e.g., v0, v1)', default=None)
args = parser.parse_args()

# JSONファイルを読み込む
with open(args.input_file, 'r') as f:
    schema = json.load(f)

# バージョンが指定されている場合、そのバージョンの定義を使用
if args.version:
    properties = schema['definitions'][args.version]['properties']
else:
    properties = schema['properties']

# 参照を解決する関数


def resolve_ref(ref):
    """
    Resolves a JSON reference to its corresponding property.

    This function handles both internal references (starting with '#') and external references
    (containing a file path and a reference path separated by '#').

    Args:
        ref (str): The JSON reference to resolve. It can be an internal reference (e.g., '#/definitions/Property')
                   or an external reference (e.g., 'file.json#/definitions/Property').

    Returns:
        dict: The resolved property from the JSON schema.

    Raises:
        KeyError: If the reference path does not exist in the properties.
        FileNotFoundError: If the external reference file does not exist.
        json.JSONDecodeError: If the external reference file is not a valid JSON.
    """
    if ref.startswith('#'):
        ref_path = ref.split('/')[-1]
        return properties[ref_path]
    else:
        ref_file, ref_path = ref.split('#')
        ref_file = os.path.join(os.path.dirname(args.input_file), ref_file)
        with open(ref_file, 'r') as f:
            ref_schema = json.load(f)
        ref_properties = ref_schema['properties']
        ref_path = ref_path.split('/')[-1]
        return ref_properties[ref_path]


def calculate_bit_length(details):
    print(details)
    if '$ref' in details:
        ref_details = resolve_ref(details['$ref'])
        return ref_details['bitLength']
    if details['type'] == 'object':
        return 0
    if details['type'] == 'array':
        items_ref = details['items'].get('$ref')
        if items_ref:
            ref_details = resolve_ref(items_ref)
            return ref_details['bitLength']
        return 0
    return details['bitLength']


# 画像の設定
bit_width = 10
bit_height = 20
margin = 0.

# ビット列の総数を計算
total_bits = 0

for prop, details in properties.items():
    total_bits += calculate_bit_length(details)

rows = (total_bits + 63) // 64  # 64ビットごとに改行

# キャンバスのサイズを設定
fig_width = bit_width * 64 + margin * 2
fig_height = (rows + 1) * bit_height + margin * 2  # Adjust height for property names and descriptions

# ビット列を描画するためのキャンバスを作成
fig, ax = plt.subplots(figsize=(fig_width / 10, fig_height / 10))
ax.set_xlim(0, fig_width)
ax.set_ylim(0, fig_height)
ax.axis('off')

# ビット列を描画
x = margin
y = fig_height - margin - bit_height
bit_position = 0

# 一行目に64ビットを箱で表現する。箱のなかには左から順に 63 から 0 までのビット番号を描画する。
for i in range(64):
    rect = patches.Rectangle((x, y), bit_width, bit_height, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    text = str(63 - i)
    fontsize = min(bit_width, bit_height) * 3  # Adjust font size to fit within the box
    ax.text(x + bit_width / 2, y + bit_height / 2, text, ha='center', va='center', fontsize=fontsize)
    x += bit_width

# Reset x position after drawing the first row of 64 bits
x = margin
y -= bit_height

def draw_bit_field(x, y, bit_length, prop_name, bit_position, is_array=False):
    remaining_bits = 64 - (bit_position % 64)
    if bit_length > remaining_bits:
        # Draw the first part
        rect = patches.Rectangle((x, y), remaining_bits * bit_width, bit_height, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)
        label = f"{prop_name}[]" if is_array else prop_name
        fontsize = min(remaining_bits * bit_width, bit_height) * 3  # Adjust font size to fit within the box
        ax.text(x + (remaining_bits * bit_width) / 2, y + bit_height / 2, label, ha='center', va='center', fontsize=fontsize)
        
        # Move to the next line
        x = margin
        y -= bit_height
        bit_length -= remaining_bits
        bit_position += remaining_bits
    else:
        remaining_bits = bit_length

    # Draw the remaining part
    rect = patches.Rectangle((x, y), remaining_bits * bit_width, bit_height, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    label = f"{prop_name}[]" if is_array else prop_name
    fontsize = min(remaining_bits * bit_width, bit_height) * 3  # Adjust font size to fit within the box
    ax.text(x + (remaining_bits * bit_width) / 2, y + bit_height / 2, label, ha='center', va='center', fontsize=fontsize)
    
    return x + remaining_bits * bit_width, y, bit_position + remaining_bits

for prop, details in properties.items():
    if '$ref' in details:
        details = resolve_ref(details['$ref'])
    if details['type'] == 'object':
        continue
    if details['type'] == 'array':
        items_ref = details['items'].get('$ref')
        if items_ref:
            ref_details = resolve_ref(items_ref)
            bit_length = ref_details['bitLength']
            x, y, bit_position = draw_bit_field(x, y, bit_length, prop, bit_position, is_array=True)
            if bit_position % 64 == 0:
                x = margin
                y -= bit_height
        continue
    bit_length = details['bitLength']
    x, y, bit_position = draw_bit_field(x, y, bit_length, prop, bit_position)
    if bit_position % 64 == 0:
        x = margin
        y -= bit_height

# 出力ファイル名とディレクトリを設定
output_md_dir = args.output_dir
output_pdf_dir = output_md_dir + '/pdf'
output_png_dir = output_md_dir + '/png'
output_svg_dir = output_md_dir + '/svg'
os.makedirs(output_pdf_dir, exist_ok=True)
os.makedirs(output_png_dir, exist_ok=True)
os.makedirs(output_svg_dir, exist_ok=True)
os.makedirs(output_md_dir, exist_ok=True)

if args.version:
    base_filename = os.path.splitext(os.path.basename(args.input_file))[0] + f'-{args.version}'
else:
    base_filename = os.path.splitext(os.path.basename(args.input_file))[0]

output_pdf_file = os.path.join(output_pdf_dir, base_filename + '.pdf')
output_svg_file = os.path.join(output_svg_dir, base_filename + '.svg')
output_png_file = os.path.join(output_png_dir, base_filename + '.png')
output_small_png_file = os.path.join(output_png_dir, base_filename + '-s.png')
output_md_file = os.path.join(output_md_dir, base_filename + '.md')

# プロパティ名と description を Markdown として出力
with open(output_md_file, 'w') as md_file:
    title = schema.get('title', 'No Title')
    if (args.version):
        title = f"{title} ({args.version})"
    description = schema.get('description', 'No Description')
    md_file.write(f"# {title}\n\n")
    md_file.write(f"{description}\n\n")
    md_file.write("| Property Name | Bit Length | Description |\n")
    md_file.write("|---------------|------------|-------------|\n")
    for prop, details in properties.items():
        description = details.get('description', '')
        bit_length = details.get('bitLength', '')
        if '$ref' in details:
            details = resolve_ref(details['$ref'])
            bit_length = details.get('bitLength', bit_length)
            if description == '':
                description = details.get('description', '')
        md_file.write(f"| {prop} | {bit_length} | {description} |\n")
    # Embed the PNG image in the Markdown file
    relative_png_path = os.path.relpath(output_png_file, start=os.path.dirname(output_md_file))
    relative_pdf_path = os.path.relpath(output_pdf_file, start=os.path.dirname(output_md_file))
    relative_svg_path = os.path.relpath(output_svg_file, start=os.path.dirname(output_md_file))
    md_file.write(f"\n![Bit Field Diagram]({relative_svg_path})\n")
    # md_file.write(f"\n[Download PDF]({relative_pdf_path})\n")
#    md_file.write(f"\n[![Bit Field Diagram]({relative_png_path})]({relative_small_png_path})\n")

# 画像を保存
plt.savefig(output_pdf_file, format='pdf')
plt.savefig(output_png_file, format='png')
plt.savefig(output_svg_file, format='svg')
plt.close()

