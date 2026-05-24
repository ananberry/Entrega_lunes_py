import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import BytesIO


def graficar_frecuencia(df):

    frecuencia = df["objeto"].value_counts()

    datos = pd.DataFrame({
        "objeto": frecuencia.index,
        "cantidad": frecuencia.values
    })

    lista_colores = ["red", "blue", "green", "orange"]

    fig, ax = plt.subplots(figsize=(8, 6))

    datos.plot(
        kind="bar",
        x="objeto",
        y="cantidad",
        color=lista_colores,
        legend=False,
        ax=ax
    )

    ax.set_title("Objetos más prestados")
    ax.set_xlabel("Objetos")
    ax.set_ylabel("Cantidad")
    ax.tick_params(axis='x', rotation=45)

    buffer = BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)

    imagen = base64.b64encode(buffer.read()).decode("utf-8")

    plt.close(fig)

    return imagen


def graficar_estados(df):

    agrupado = df["estado"].value_counts()

    datos = pd.DataFrame({
        "estado": agrupado.index,
        "cantidad": agrupado.values
    })

    colores = ["blue", "green", "orange"]

    fig, ax = plt.subplots(figsize=(8, 6))

    datos.plot(
        kind="bar",
        x="estado",
        y="cantidad",
        color=colores,
        legend=False,
        ax=ax
    )

    ax.set_title("Estados de préstamos")
    ax.set_xlabel("Estado")
    ax.set_ylabel("Cantidad")

    buffer = BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)

    imagen = base64.b64encode(buffer.read()).decode("utf-8")

    plt.close(fig)

    return imagen