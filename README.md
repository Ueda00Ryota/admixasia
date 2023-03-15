## Admix
[![Build Status](https://travis-ci.org/stevenliuyi/admix.svg?branch=master)](https://travis-ci.org/stevenliuyi/admix)

Admixasia は[admix](https://github.com/stevenliuyi/admix) パッケージに東アジアの三か国（中国、日本、韓国）を追加したものです。(such as [23andme](https://www.23andme.com/) and [AncestryDNA](https://www.ancestry.com/dna/)).
使用法については、admixと同じですが、こちらはGithub経由でしかインストールできないので注意してください(3/15時点)

### インストール

```
pip install git+https://github.com/Ueda00Ryota/admixasia
```

### 使用法
現在23andmeの生データに対応しております。パラメータは以下のように指定してください。
-f 入力ファイル名　-v ファイル形式　-m モデル（複数選択可能）　-o 出力ファイル

```
admixasia -f my_raw_data.txt -v 23andme -o result.txt
```

ヘルプ:
```
admixasia -h
```

### 出力結果
日本語対応に変更予定
- **English**

Command: `admixasia -m K12b`

Output:
```
Gedrosia: 0.06%
Siberian: 3.71%
Northwest African: 0.00%
Southeast Asian: 33.43%
Atlantic Med: 0.07%
North European: 0.00%
South Asian: 0.00%
East African: 0.00%
Southwest Asian: 0.01%
East Asian: 62.72%
Caucasus: 0.00%
Sub Saharan: 0.00%
```

### 生データ形式
plink形式(ped,fam),hapmap形式追加予定

| parameter value | vendor |
| --------------- | ------ |
| 23andme | [23andme](https://www.23andme.com/) |
| ancestry | [AncestryDNA](https://www.ancestry.com/dna/) |
| ftdna | [FamilyTreeDNA Family Finder](https://www.familytreedna.com/products/family-finder) |
| ftdna2 | [FamilyTreeDNA Family Finder](https://www.familytreedna.com/products/family-finder) (new format) |
| wegene | [WeGene](https://www.wegene.com/en/) |
| myheritage | [MyHeritageDNA](https://www.myheritage.com/dna) |

### モデル
選択可能モデル、その他情報はadmixと同じです。
新たにadmixに東アジアパネルを追加しています　EastAsia3
参考：https://onlinelibrary.wiley.com/doi/10.1111/ahg.12320

