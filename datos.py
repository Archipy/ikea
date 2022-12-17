import pandas as pd

archivo = "C:/Users/Usuario/Desktop/PROPUESTA FINAL.xlsm"

df2 = pd.read_excel(archivo, sheet_name="PICKING")
df = df2[["LV", "MV", "HASTA", "DESDE", "TIE"]].dropna()


def aire_total():
    aire0 = 0
    aire1 = 0
    aire2 = 0

    articulo0 = df[df["DESDE"].str.contains("-", regex=False, na=False) & (df['MV'] == 0) & (df["HASTA"] == "Buffer")]
    for articulo in articulo0["MV"]:
        aire0 += 1
    articulo1 = df[df["DESDE"].str.contains("-", regex=False, na=False) & (df['MV'] == 1) & (df["HASTA"] == "Buffer")]
    for articulo in articulo1["MV"]:
        aire1 += 1
    articulo2 = df[df["DESDE"].str.contains("-", regex=False, na=False) & (df['MV'] == 2) & (df["HASTA"] == "Buffer")]
    for articulo in articulo2["MV"]:
        aire2 += 1
    return aire0, aire1, aire2


def check_datos():
    repo_mv0 = 0
    repo_mv1 = 0
    repo_mv2 = 0
    df0 = df.drop(df[(df['MV'] == 2) | (df['MV'] == 1)].index)
    for articulo0 in df0["HASTA"]:
        if articulo0 == "Sales":
            repo_mv0 += 1

    df1 = df.drop(df[(df['MV'] == 2) | (df['MV'] == 0)].index)
    for articulo1 in df1["HASTA"]:
        if articulo1 == "Sales":
            repo_mv1 += 1

    df2 = df.drop(df[(df['MV'] == 1) | (df['MV'] == 0)].index)
    for articulo2 in df2["HASTA"]:
        if articulo2 == "Sales":
            repo_mv2 += 1

    return repo_mv0, repo_mv1, repo_mv2


def check_tie_dormunt():
    tie00d = 0
    tie01d = 0
    tie02d = 0

    articulo0d = df[(df['TIE'] == 0) & (df['MV'] == 0) & (df["HASTA"] == "Sales") & (
        df["DESDE"].str.contains("064-", regex=False, na=False))]

    for articulo in articulo0d["MV"]:
        tie00d += 1

    articulo1d = df[(df['TIE'] == 0) & (df['MV'] == 1) & (df["HASTA"] == "Sales") & (
        df["DESDE"].str.contains("064-", regex=False, na=False))]

    for articulo in articulo1d["MV"]:
        tie01d += 1

    articulo2d = df[(df['TIE'] == 0) & (df['MV'] == 2) & (df["HASTA"] == "Sales") & (
        df["DESDE"].str.contains("064-", regex=False, na=False))]

    for articulo in articulo2d["MV"]:
        tie02d += 1

    return tie00d, tie01d, tie02d
