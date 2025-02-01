# Header Schema

このファイルは `header.json` の内容を説明します。

## スキーマ概要

- `$schema`: JSON Schema のバージョン
- `title`: スキーマのタイトル
- `type`: オブジェクト型
- `definitions`: プロパティの定義

## プロパティ

### version
- **type**: integer
- **description**: Version
- **bitLength**: 8

### magic
- **type**: integer
- **description**: Magic number
- **bitLength**: 56

### length
- **type**: integer
- **description**: Length (in bytes)
- **bitLength**: 32

### headerLength
- **type**: integer
- **description**: Header length (in bytes)
- **bitLength**: 16

### status
- **type**: integer
- **description**: Status
- **bitLength**: 16

### type
- **type**: integer
- **description**: Type
- **bitLength**: 32

### reserved
- **type**: integer
- **description**: Reserved
- **bitLength**: 32

### banks
- **type**: array
- **items**: 
  - `$ref`: "header-extra-bank.json#/definitions/bank"

## 参照

### header-extra-bank.json

`banks` プロパティは `header-extra-bank.json` ファイルの `bank` 定義を参照しています。

#### bank
- **type**: object
- **required**: ["length", "bankname", "data"]
- **properties**:
  - **length**:
    - **type**: integer
    - **description**: Length of the bank
    - **bitLength**: 32
  - **bankname**:
    - **type**: string
    - **description**: Bank name
    - **bitLength**: 32
  - **data**:
    - **type**: integer
    - **description**: Bank data
    - **bitLength**: 64

## ビットフィールド図

以下の図は `header.json` のビットフィールドを示しています。

![Bit Field Diagram](../output/bit_field_diagram.pdf)