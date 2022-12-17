import webbrowser
from threading import Timer
from flask import Flask, render_template
import check_auto
import check_market
import check_shipments
import datos


app = Flask(__name__)

check_shipments.shipment_duplicados()
x = check_market.check_market_repo()
y = check_auto.camiones_auto()
lista = ["Menaje", "Textil 11", "Textil 12", "Orden", "Baños", "Iluminacion", "Deco", "Niños", "Actividades"]
listaauto = ["pares", "impares", "fondopar", "fondoimpar", "pax", "2426", "1a3", "zona1", "zona2", "zona3", "zona4"]
repo = datos.check_datos()
tied = datos.check_tie_dormunt()
aires = datos.aire_total()
repo_auto = check_auto.repo_auto()


@app.route("/")
def hello_world():
    return render_template("index.html", repo=repo, tied=tied, aire=aires)


@app.route("/MV0")
def metodoventa0():
    camion = x
    return render_template("MV0.html", camion=camion, lista=lista)


@app.route("/MV1")
def metodoventa1():
    camion = y
    return render_template("MV1.html", repo=repo_auto, lista=listaauto, camion=camion)


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run("0.0.0.0", 5000, debug=False)
