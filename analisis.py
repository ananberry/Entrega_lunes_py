import funciones as pp


# Menu
def mostrar_menu():

    print("\n========== MENU ==========")

    print("1. Ver datos")
    print("2. Ver valores nulos")
    print("3. Encontrar errores")
    print("4. Realizar limpieza")
    print("5. Ver datos limpios")

    print("\n----- ANALISIS -----")

    print("6. Analisis de frecuencia")
    print("7. Analisis de agrupacion")
    print("8. Filtrado y conteo")
    print("9. Prestamos atrasados")

    print("\n0. Salir")


# Main
def main():

    # Cargar datos
    df_usuarios = pp.cargar_usuarios()

    df_prestamos = pp.cargar_prestamos()

    datos_limpios = False

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opcion: ")

        # Ver datos
        if opcion == "1":

            pp.ver_datos(df_usuarios, "USUARIOS")

            pp.ver_datos(df_prestamos, "PRESTAMOS")

        # Ver nulos
        elif opcion == "2":

            print("\nUSUARIOS")
            pp.ver_nulos(df_usuarios)

            print("\nPRESTAMOS")
            pp.ver_nulos(df_prestamos)

        # Encontrar errores
        elif opcion == "3":

            print("\nUSUARIOS")
            pp.encontrar_errores(df_usuarios)

            print("\nPRESTAMOS")
            pp.encontrar_errores(df_prestamos)

        # Realizar limpieza
        elif opcion == "4":

            df_usuarios = pp.manejar_nulos(
                df_usuarios,
                "rellenar"
            )

            df_usuarios = pp.limpiar_usuarios(
                df_usuarios
            )

            df_prestamos = pp.manejar_nulos(
                df_prestamos,
                "eliminar"
            )

            df_prestamos = pp.limpiar_prestamos(
                df_prestamos
            )

            datos_limpios = True

            print("\nDatos limpiados correctamente")

        # Ver datos limpios
        elif opcion == "5":

            if datos_limpios:

                pp.ver_datos_limpios(
                    df_usuarios,
                    "USUARIOS LIMPIOS"
                )

                pp.ver_datos_limpios(
                    df_prestamos,
                    "PRESTAMOS LIMPIOS"
                )

            else:

                print("\nPrimero realiza la limpieza")

        # Analisis de frecuencia
        elif opcion == "6":

            resultado = pp.frecuencia_objetos(
                df_prestamos
            )

            print("\n===== FRECUENCIA =====")

            print(resultado)

        # Analisis de agrupacion
        elif opcion == "7":

            resultado = pp.agrupacion_prestamos(
                df_prestamos
            )

            print("\n===== AGRUPACION =====")

            print(resultado)

        # Filtrado y conteo
        elif opcion == "8":

            df_merge = pp.unir_datos(
                df_prestamos,
                df_usuarios
            )

            filtrado = pp.filtrar_prestamos(
                df_merge,
                "Prestado"
            )

            print("\n===== FILTRADO =====")

            print(filtrado)

            print(f"\nTotal: {len(filtrado)}")

        # Prestamos atrasados
        elif opcion == "9":

            pp.prestamos_atrasados(
                df_prestamos
            )

        # Salir
        elif opcion == "0":

            print("\nHasta luego 👋")

            break

        else:

            print("\nOpcion invalida")


# Ejecutar programa
if __name__ == "__main__":

    main()