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

<<<<<<< HEAD
    df_archivo['ID_usuario'] = df_archivo['ID_usuario'].astype(str).str.strip()
    df_archivo['nombre'] = df_archivo['nombre'].astype(str).str.strip().str.title()
    df_archivo['rol'] = df_archivo['rol'].astype(str).str.strip().str.title()
    df_archivo['correo'] = df_archivo['correo'].astype(str).str.strip().str.lower()
=======
    df_archivo['ID_Persona'] = df_archivo['ID_Persona'].astype(str).str.strip()
    df_archivo['Nombre'] = df_archivo['Nombre'].astype(str).str.strip().str.title()
    df_archivo['Rol'] = df_archivo['Rol'].astype(str).str.strip().str.title()
    df_archivo['Correo'] = df_archivo['Correo'].astype(str).str.strip().str.lower()
>>>>>>> 69345f2563ce315b5f2b4913b66339633e7ba677

    return df_archivo


<<<<<<< HEAD
=======
# Limpiar texto de préstamos (eliminar espacios y normalizar mayúsculas)
def limpiar_prestamos(df_prestamos):
    print("Limpiando datos de préstamos...")

    df_prestamos['ID_Prestamo'] = df_prestamos['ID_Prestamo'].astype(str).str.strip()
    df_prestamos['ID_Persona'] = df_prestamos['ID_Persona'].astype(str).str.strip()
    df_prestamos['Objeto'] = df_prestamos['Objeto'].astype(str).str.strip().str.title()
    df_prestamos['Estado'] = df_prestamos['Estado'].astype(str).str.strip().str.title()

    print("Datos de préstamos limpios:")
    print(df_prestamos.head())

    return df_prestamos


>>>>>>> 69345f2563ce315b5f2b4913b66339633e7ba677
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

<<<<<<< HEAD
            df_archivo["nombre"] = df_archivo["nombre"].fillna("desconocido")
            df_archivo["rol"] = df_archivo["rol"].fillna(
                df_archivo["rol"].mode()[0] if not df_archivo["rol"].mode().empty else "sin_rol"
            )
            df_archivo["correo"] = df_archivo["correo"].fillna("sin_correo")
=======
            df_archivo["Nombre"] = df_archivo["Nombre"].fillna("desconocido")
            df_archivo["Rol"] = df_archivo["Rol"].fillna(
                df_archivo["Rol"].mode()[0] if not df_archivo["Rol"].mode().empty else "sin_rol"
            )
            df_archivo["Correo"] = df_archivo["Correo"].fillna("sin_correo")
>>>>>>> 69345f2563ce315b5f2b4913b66339633e7ba677

        else:
            print("Método no válido")

    else:
        print("No se encontraron valores nulos.")

<<<<<<< HEAD
    return df_archivo
=======
    return df_archivo


# Filtrar préstamos por estado
def filtrar_por_estado(df_prestamos, estado):
    print(f"\nFiltrando préstamos con estado: '{estado}'...")
    df_filtrado = df_prestamos[df_prestamos['Estado'].str.lower() == estado.lower()]
    print(f"Se encontraron {len(df_filtrado)} préstamos con estado '{estado}':")
    print(df_filtrado.to_string(index=False))
    return df_filtrado


# Combinar (merge) usuarios y préstamos
def combinar_datos(df_usuarios, df_prestamos):
    print("\nCombinando datos de usuarios y préstamos...")
    df_combinado = pd.merge(
        df_prestamos,
        df_usuarios,
        on='ID_Persona',
        how='inner'
    )
    print(f"Total de registros combinados: {len(df_combinado)}")
    print(df_combinado[['ID_Prestamo', 'Nombre', 'Rol', 'Objeto', 'Estado']].to_string(index=False))
    return df_combinado


# Agrupar préstamos por rol de usuario
def agrupar_por_rol(df_combinado):
    print("\nAgrupando préstamos por rol de usuario...")
    agrupado = df_combinado.groupby('Rol').agg(
        total_prestamos=('ID_Prestamo', 'count')
    ).reset_index()
    print(agrupado.to_string(index=False))
    return agrupado


# Frecuencia de objetos prestados
def frecuencia_objetos(df_prestamos):
    resultado = df_prestamos['Objeto'].value_counts()
    return resultado


# Agrupación de préstamos por estado
def agrupacion_prestamos(df_prestamos):
    resultado = df_prestamos.groupby('Estado')['ID_Prestamo'].count().reset_index()
    resultado.columns = ['Estado', 'Total']
    return resultado


# Unir usuarios y préstamos
def unir_datos(df_prestamos, df_usuarios):
    df_merge = pd.merge(df_prestamos, df_usuarios, on='ID_Persona', how='inner')
    return df_merge


# Filtrar préstamos por estado
def filtrar_prestamos(df_merge, estado):
    df_filtrado = df_merge[df_merge['Estado'].str.lower() == estado.lower()]
    return df_filtrado
>>>>>>> 69345f2563ce315b5f2b4913b66339633e7ba677
