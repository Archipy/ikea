import pandas as pd
import juntar_camiones
import check_shipments

archivo = "C:/Users/Usuario/Desktop/PROPUESTA FINAL.xlsm"

df2 = pd.read_excel(archivo, sheet_name="PICKING")
df = df2[["DESDE", "LV", "HASTA", "HFB", "MV"]].dropna()
df = df.drop(df[(df['MV'] == 2) | (df['MV'] == 1)].index)

dic_camiones = {}
extras = []
menaje = 0
textil = 0
orden = 0
banos = 0
ilu = 0
deco = 0
ninos = 0
actividades = 0


def check_market_repo():
    full_cam = juntar_camiones.junta_camion()
    check_shipments.shipment_duplicados()
    for shipment in check_shipments.camiones_shipment:

        menaje = 0
        textil11 = 0
        textil12 = 0
        orden = 0
        banos = 0
        ilu = 0
        deco = 0
        ninos = 0
        actividades = 0
        contador = 0

        articulos = df[(df["DESDE"] == shipment) & (df['HASTA'] == 'Sales')]["HFB"]
        act = df[(df['DESDE'] == shipment) & (df['HASTA'] == 'Sales')]

        for item in act["LV"]:
            if str(item).startswith("AO"):
                actividades += 1

        for articulo in articulos:
            if type(articulo) != str:
                if articulo == 14 or articulo == 15:
                    menaje += 1
                elif articulo == 11:
                    textil11 += 1
                elif articulo == 12:
                    textil12 += 1
                elif articulo == 18:
                    orden += 1
                elif articulo == 6:
                    banos += 1
                elif articulo == 10 or articulo == 13:
                    ilu += 1
                elif articulo == 16:
                    deco += 1
                elif articulo == 7 or articulo == 9:
                    ninos += 1
                else:
                    extras.append(articulo)

        for cami in full_cam:
            p = full_cam[cami]
            if shipment in p:
                dic_camiones.update({f"{cami}": {f"{p}": {"Orden": 0}}})
                camion = {"Menaje": menaje, "Textil 11": textil11, "Textil 12": textil12, "Orden": orden,
                          "Baños": banos,
                          "Iluminacion": ilu,
                          "Deco": deco, "Niños": ninos, "Actividades": actividades}
                dic_camiones[f"{cami}"][f"{p}"].update(camion)
        contador += 1

    return dic_camiones
