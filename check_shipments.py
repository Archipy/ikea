import pandas as pd

archivo = "C:/Users/Usuario/Desktop/PROPUESTA FINAL.xlsm"

df2 = pd.read_excel(archivo, sheet_name="PICKING")
df = df2[["DESDE"]].dropna()

camiones_duplicados = []
camiones_shipment = []

def shipment_duplicados():
    for shipment in df["DESDE"]:
        if type(shipment) == str and shipment != "BACKFLOW":
            camiones_duplicados.append(shipment)

    for camion in camiones_duplicados:
        if camion not in camiones_shipment:
            camiones_shipment.append(camion)
    return camiones_shipment