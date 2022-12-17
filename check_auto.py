import pandas as pd
import juntar_camiones
import check_shipments

archivo = "C:/Users/Usuario/Desktop/PROPUESTA FINAL.xlsm"

df2 = pd.read_excel(archivo, sheet_name="PICKING")
df = df2[["LV", "MV", "HASTA", "DESDE"]].dropna()

pares_pasillos = ("8", "10", "12", "14", "16", "18", "20", "22")
impares_pasillos = ("5", "7", "9", "11", "13", "15", "17", "19")
pax_pasillos = ("21", "23")
veinticuatro_pasillos = ("24", "26")
fondopar_pasillos = ("28", "30", "32", "34", "36", "38", "40", "42")
fondoimpar_pasillos = ("25", "27", "29", "31", "33", "35", "37", "39", "41")
pasillo1a3_pasillos = ("1", "3")
dic_camiones = {}


def repo_auto():
    zona1 = 0
    zona2 = 0
    zona3 = 0
    zona4 = 0
    pasillo1a3 = 0
    impares = 0
    pares = 0
    pax = 0
    veinticuatro = 0
    fondopar = 0
    fondoimpar = 0

    articulo = df[(df['MV'] == 1) & (df["HASTA"] == "Sales") & (df["DESDE"].str.contains("-", regex=False, na=False))]
    for referencia in articulo["LV"]:
        if str(referencia).startswith("1") and len(str(referencia)) <= 3:
            zona1 += 1
        elif str(referencia).startswith("2") and len(str(referencia)) <= 3:
            zona2 += 1
        elif str(referencia).startswith("3") and len(str(referencia)) <= 3:
            zona3 += 1
        elif str(referencia).startswith("4") and len(str(referencia)) <= 3:
            zona4 += 1
        elif str(referencia).startswith("4") and len(str(referencia)) <= 3:
            zona4 += 1
        elif str(referencia).startswith(pasillo1a3_pasillos) and len(str(referencia)) <= 5:
            pasillo1a3 += 1
        elif str(referencia).startswith(pares_pasillos):
            pares += 1
        elif str(referencia).startswith(impares_pasillos):
            impares += 1
        elif str(referencia).startswith(pax_pasillos):
            pax += 1
        elif str(referencia).startswith(veinticuatro_pasillos):
            veinticuatro += 1
        elif str(referencia).startswith(fondopar_pasillos):
            fondopar += 1
        elif str(referencia).startswith(fondoimpar_pasillos):
            fondoimpar += 1

    return zona1, zona2, zona3, zona4, pares, impares, pax, veinticuatro, fondopar, fondoimpar, pasillo1a3


def camiones_auto():
    full_cam = juntar_camiones.junta_camion()
    check_shipments.shipment_duplicados()
    for shipment in check_shipments.camiones_shipment:
        zona1 = 0
        zona2 = 0
        zona3 = 0
        zona4 = 0
        pasillo1a3 = 0
        impares = 0
        pares = 0
        pax = 0
        veinticuatro = 0
        fondopar = 0
        fondoimpar = 0
        contador = 0

        articulos = df[(df["DESDE"] == shipment) & (df['MV'] == 1) & (df["HASTA"] == "Sales")]["LV"]

        for articulo in articulos:
            if str(articulo).startswith("1") and len(str(articulo)) <= 3:
                zona1 += 1
            elif str(articulo).startswith("2") and len(str(articulo)) <= 3:
                zona2 += 1
            elif str(articulo).startswith("3") and len(str(articulo)) <= 3:
                zona3 += 1
            elif str(articulo).startswith("4") and len(str(articulo)) <= 3:
                zona4 += 1
            elif str(articulo).startswith("4") and len(str(articulo)) <= 3:
                zona4 += 1
            elif str(articulo).startswith(pasillo1a3_pasillos) and len(str(articulo)) <= 5:
                pasillo1a3 += 1
            elif str(articulo).startswith(pares_pasillos):
                pares += 1
            elif str(articulo).startswith(impares_pasillos):
                impares += 1
            elif str(articulo).startswith(pax_pasillos):
                pax += 1
            elif str(articulo).startswith(veinticuatro_pasillos):
                veinticuatro += 1
            elif str(articulo).startswith(fondopar_pasillos):
                fondopar += 1
            elif str(articulo).startswith(fondoimpar_pasillos):
                fondoimpar += 1

        for cami in full_cam:
            p = full_cam[cami]
            if shipment in p:
                dic_camiones.update({f"{cami}": {f"{p}": {"pares": 0}}})
                camion = {"pares": pares, "impares": impares, "fondopar": fondopar, "fondoimpar": fondoimpar,
                          "pax": pax, "2426": veinticuatro, "1a3": pasillo1a3, "zona1": zona1,
                          "zona2": zona2, "zona3": zona3, "zona4": zona4}
                dic_camiones[f"{cami}"][f"{p}"].update(camion)
        contador += 1

    return dic_camiones