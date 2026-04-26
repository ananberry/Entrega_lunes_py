import pandas as pd

# Cargar datos
def cargar_usuarios():
    df_archivo = pd.read_csv('data/raw/usuarios.csv')
    df_archivo.info()
    return df_archivo

def cargar_prestamos():
    df_prestamos = pd.read_csv('data/raw/prestamos.csv')
    df_prestamos.info()
    return df_prestamos


# Limpiar texto
def limpiar_usuarios(df_archivo):
    print("Limpiando datos de usuarios...")

    df_archivo['ID_usuario'] = df_archivo['ID_usuario'].astype(str).str.strip()
    df_archivo['nombre'] = df_archivo['nombre'].astype(str).str.strip().str.title()
    df_archivo['rol'] = df_archivo['rol'].astype(str).str.strip().str.title()
    df_archivo['correo'] = df_archivo['correo'].astype(str).str.strip().str.lower()

    return df_archivo


# Manejar nulos
def manejar_nulos(df_archivo, metodo="eliminar"):
    print("Manejo de valores nulos")

    print("Valores nulos por columna:")
    print(df_archivo.isnull().sum())

    if df_archivo.isnull().sum().any():
        print("Se encontraron valores nulos")

        if metodo == "eliminar":
            print("Eliminando filas...")
            df_archivo = df_archivo.dropna()

        elif metodo == "rellenar":
            print("Rellenando valores...")

            df_archivo["nombre"] = df_archivo["nombre"].fillna("desconocido")
            df_archivo["rol"] = df_archivo["rol"].fillna(
                df_archivo["rol"].mode()[0] if not df_archivo["rol"].mode().empty else "sin_rol"
            )
            df_archivo["correo"] = df_archivo["correo"].fillna("sin_correo")

        else:
            print("Método no válido")

    else:
        print("No se encontraron valores nulos.")

    return df_archivo