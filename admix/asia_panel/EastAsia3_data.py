import pandas as pd


# パネル情報読み込み
dfsnp = pd.read_csv(
    "/mnt/c/python_files/django_python/django_admix/admix-master/admix-master/admix/asia_panel/JPN_KOH_HUN_SNPs.csv"
)
# allelesとFに分割
dfrs = pd.DataFrame(dfsnp.loc[:, ["dbSNP rsID", "Ref Allele"]])
dffre = pd.DataFrame(dfsnp.loc[:, ["Han", "Japanese", "Korean"]])
# Ref Allelesの相補鎖を追加
dfrs["Allele"] = dfrs["Ref Allele"]
dfrs["Allele"].replace({"A": "T", "G": "C", "T": "A", "C": "G"}, inplace=True)
dfrs.to_csv("EastAsia3.alleles", sep=" ", header=False, index=False)
dffre.to_csv("EastAsia3.F", sep=" ", header=False, index=False)
