## Admix
[![Build Status](https://travis-ci.org/stevenliuyi/admix.svg?branch=master)](https://travis-ci.org/stevenliuyi/admix)

Admixasia は[admix](https://github.com/stevenliuyi/admix) パッケージに東アジアの三か国（中国、日本、韓国）を追加したものです。(such as [23andme](https://www.23andme.com/) and [AncestryDNA](https://www.ancestry.com/dna/)).
使用法については、admixと同じですが、こちらはGithub経由でしかインストールできないので注意してください(3/15時点)

### Installation
#### Install from Github
You can use `pip` to install admixasia directly from this Github repository:
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


### 計算方法
祖先構成計算には最尤推定（MLE）アルゴリズムが適用され、その実装は極めて簡単である。
集団$k$に対するSNPマーカー$n$のマイナーアレル頻度を$F_{nk}$とする。
l_n^{minor}$と$l_n^{major}$はそれぞれマーカー$n$のマイナーアレルとメジャーアレルとし、$G_{ni}$を注目する個体のマーカー$n$における対立遺伝子( $i=1,2$ )とする。
対数尤度関数を最大化し、個体の混和率$q_k$を見つけることができる。

$$\chi_{{l^{minor}_n}}(G_{ni})j_i\log(F_{nk}q_k)+\chi_{{l^{major}_n}}(G_{ni})j_i\log((J_{nk}-F_{nk})q_k)$$


ここで、$chi$は指標関数、$J$と$j$はオールオンの行列/ベクトルである。なお、ここではアインシュタイン和の規約を暗示している。制約条件$0 ╱q_k╱1$、$sum {q_k} = 1$で、最適化技術を適用して混和割合$q_k$を求めることができる。
