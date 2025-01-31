import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# JSONファイルを読み込む
with open('/home/ota/repos/nestdaq-user-impl/schema/header.json', 'r') as f:
    schema = json.load(f)

properties = schema['definitions']

# 参照を解決する関数
def resolve_ref(ref):
    if ref.startswith('#'):
        ref_path = ref.split('/')[-1]
        return properties[ref_path]
    else:
        ref_file, ref_path = ref.split('#')
        ref_file = os.path.join(os.path.dirname('/home/ota/repos/nestdaq-user-impl/schema/header.json'), ref_file)
        with open(ref_file, 'r') as f:
            ref_schema = json.load(f)
        ref_properties = ref_schema['definitions']
        ref_path = ref_path.split('/')[-1]
        return ref_properties[ref_path]

# 画像の設定
bit_width = 10
bit_height = 20
margin = 1

# ビット列の総数を計算
total_bits = sum(details['bitLength'] for details in properties.values() if details['type'] != 'array' and details['type'] != 'object')
rows = (total_bits + 63) // 64  # 64ビットごとに改行

# キャンバスのサイズを設定
fig_width = bit_width * 64 + margin * 2
fig_height = (rows + 1) * bit_height + margin * 2

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

for prop, details in properties.items():
    if details['type'] == 'object':
        continue
    if details['type'] == 'array':
        # 配列の場合は1回だけ内容を表示
        items_ref = details['items'].get('$ref')
        if items_ref:
            ref_details = resolve_ref(items_ref)
            bit_length = ref_details['bitLength']
            description = ref_details['description']
        
        rect = patches.Rectangle((x, y), bit_length * bit_width, bit_height, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)
        fontsize = min(bit_length * bit_width, bit_height) * 3  # Adjust font size to fit within the box
        ax.text(x + (bit_length * bit_width) / 2, y + bit_height / 2, f"{prop}[]", ha='center', va='center', fontsize=fontsize)
        x += bit_length * bit_width
        bit_position += bit_length
        if bit_position % 64 == 0:
            x = margin
            y -= bit_height
        continue
    bit_length = details['bitLength']
    description = details['description']
    
    # ビット列を描画
    rect = patches.Rectangle((x, y), bit_length * bit_width, bit_height, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    # プロパティ名を四角の中心に真ん中揃えで描画
    fontsize = min(bit_length * bit_width, bit_height) * 3  # Adjust font size to fit within the box
    ax.text(x + (bit_length * bit_width) / 2, y + bit_height / 2, prop, ha='center', va='center', fontsize=fontsize)
    x += bit_length * bit_width
    bit_position += bit_length
    
    if bit_position % 64 == 0:
        x = margin
        y -= bit_height

# 画像を保存
plt.savefig('/home/ota/repos/nestdaq-user-impl/output/bit_field_diagram.pdf', format='pdf')
plt.close()
