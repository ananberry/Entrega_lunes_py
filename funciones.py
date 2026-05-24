import pandas as pd # type: ignore


# Cargar datos

def cargar_usuarios():
    df_usuarios = pd.read_csv("data/raw/usuarios.csv")
    return df_usuarios


def cargar_prestamos():
    df_prestamos = pd.read_csv("data/raw/prestamos.csv")
    return df_prestamos


# Ver datos

def ver_datos(df, nombre):

    print(f"\n===== {nombre} =====")
    print(df.head())


# Ver nulos
def ver_nulos(df):

    print("\n===== VALORES NULOS =====")
    print(df.isnull().sum())


# Encontrar errores

def encontrar_errores(df):

    print("\n===== POSIBLES ERRORES =====")

    duplicados = df.duplicated().sum()

    print(f"Filas duplicadas: {duplicados}")


# Manejar nulos

def manejar_nulos(df, metodo):

    if metodo == "eliminar":

        df = df.dropna()

    elif metodo == "rellenar":

        for columna in df.columns:

            if df[columna].dtype == "object":

                df[columna] = df[columna].fillna("desconocido")

    return df


# Limpiar datos de usuarios

def limpiar_usuarios(df):

    print("\nLimpiando usuarios...")

    df.columns = df.columns.str.lower()

    df["id_persona"] = df["id_persona"].astype(str).str.strip()

    df["nombre"] = df["nombre"].astype(str).str.strip().str.title()

    df["rol"] = df["rol"].astype(str).str.strip().str.title()

    df["correo"] = df["correo"].astype(str).str.strip().str.lower()

    return df

# Limpiar datos de prestamos

def limpiar_prestamos(df):

    print("\nLimpiando prestamos...")

    df.columns = df.columns.str.lower()

    df["id_prestamo"] = df["id_prestamo"].astype(str).str.strip()

    df["id_persona"] = df["id_persona"].astype(str).str.strip()

    df["objeto"] = df["objeto"].astype(str).str.strip().str.title()

    df["estado"] = df["estado"].astype(str).str.strip().str.title()

    return df


# Ver datos limpios

def ver_datos_limpios(df, nombre):

    print(f"\n===== {nombre} =====")
    print(df.head())


# Frecuencia

def frecuencia_objetos(df):

    resultado = df["objeto"].value_counts()

    return resultado


#Agrupación

def agrupacion_prestamos(df):

    resultado = df.groupby("estado")["id_prestamo"].count()

    return resultado


# Unir datos

def unir_datos(df_prestamos, df_usuarios):

    df_merge = pd.merge(
        df_prestamos,
        df_usuarios,
        on="id_persona"
    )

    return df_merge



# Filtrar prestamos por estado


def filtrar_prestamos(df, estado):

    filtrado = df[df["estado"] == estado]

    return filtrado



# Funcion especial


def prestamos_atrasados(df):

    print("\n===== PRESTAMOS ATRASADOS =====")

    if "dias_prestamo" in df.columns:

        atrasados = df[df["dias_prestamo"] > 30]

        print(atrasados)

    else:

        print("No existe la columna dias_prestamo")