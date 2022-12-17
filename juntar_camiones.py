import pandas as pd

plan_descarga = "C:/Users/Usuario/Desktop/221201.xlsx"

df2 = pd.read_excel(plan_descarga, header=1)
df = df2[["Shipment ID", "Consignment ID"]]


def junta_camion():
    full_camion = {}
    contador = 0

    for consignmet in df["Consignment ID"]:
        x = df.iloc[contador, 0]
        if not pd.isnull(x):
            full_camion[df2['Shipment ID'][contador]] = [consignmet]
            j = df2['Shipment ID'][contador]
        if pd.isnull(x):
            full_camion[j].append(consignmet)
            contador += 1
            continue
        contador += 1
    return full_camion