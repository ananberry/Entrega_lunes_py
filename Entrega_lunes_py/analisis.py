# analisis.py
import funciones as pp


def mostrar_menu():
    print("\n===== MENÚ DE ANÁLISIS =====")
    print("1. Análisis de frecuencia")
    print("2. Análisis de agregación")
    print("3. Análisis con filtrado y conteo")
    print("4. Salir")
    print(30 * "=")


def main():

    df_usuarios = pp.cargar_usuarios()
    df_prestamos = pp.cargar_prestamos()

    df_usuarios = pp.manejar_nulos(df_usuarios, "rellenar")
    df_usuarios = pp.limpiar_usuarios(df_usuarios)

    df_prestamos = pp.manejar_nulos(df_prestamos, "eliminar")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "1":
            print("\n--- Análisis de Frecuencia ---")

            resultado = pp.frecuencia_objetos(df_prestamos)

            for objeto, cantidad in resultado.head(5).items():
                print(f"{objeto} - {cantidad}")

        elif opcion == "2":
            print("\n--- Análisis de Agregación ---")

            resultado = pp.agrupacion_prestamos(df_prestamos)

            print("Total de préstamos por categoría:")
            print(resultado)

        elif opcion == "3":
            print("\n--- Análisis con Filtrado y Conteo ---")

            df_merge = pp.unir_datos(df_prestamos, df_usuarios)

            filtrado = pp.filtrar_prestamos(df_merge, "prestado")

            print(f"Préstamos en estado 'prestado': {len(filtrado)}")

        elif opcion == "4":
            print("Hasta luego 👋")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()