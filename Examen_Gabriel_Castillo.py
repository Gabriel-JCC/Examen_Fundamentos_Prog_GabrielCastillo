
def menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("1. Cupos por genero")
    print("2. Busqueda de peliculas por rango de precio")
    print("3. Actualizar precio de pelicula")
    print("4. Agregar pelicula")
    print("5. Eliminar pelicula")
    print("6. Salir")
    print("=" * 36)


def leer_opc():
    opc_valida = False
    opc = 0
    while opc_valida == False:
        try:
            opc = int(input("Ingrese opcion: "))
            if opc >= 1 and opc <= 6:
                opc_valida = True
            else:
                print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")
    return opc

def validar_texto(valor):
    if valor.strip() == "":
        return False
    return True

def validar_entero_mayor_cero(valor_str):
    try:
        valor = int(valor_str)
        if valor > 0:
            return True
        return False
    except ValueError:
        return False

def validar_entero_mayor_igual_cero(valor_str):
    try:
        valor = int(valor_str)
        if valor >= 0:
            return True
        return False
    except ValueError:
        return False

def validar_clasificacion(valor):
    if valor in ("A", "B", "C"):
        return True
    return False

def buscar_codigo(codigo, cartelera):
    existe = False
    for clave in cartelera:
        if clave.upper() == codigo.upper():
            existe = True
    return existe

def cupos_genero(genero, peliculas, cartelera):
    total = 0
    for codigo in peliculas:
        if peliculas[codigo][1].lower() == genero.lower():
            total += cartelera[codigo][1]
    print(f"El total de cupos disponibles es: {total}")

def busqueda_precio(p_min, p_max, peliculas, cartelera):
    resultados = []
    for codigo in cartelera:
        precio = cartelera[codigo][0]
        cupos = cartelera[codigo][1]
        if precio >= p_min and precio <= p_max and cupos != 0:
            titulo = peliculas[codigo][0]
            resultados.append(f"{titulo}--{codigo}")
    resultados.sort()
    if len(resultados) == 0:
        print("No hay peliculas en ese rango de precios.")
    else:
        print(f"Las peliculas encontradas son: {resultados}")

def actualizar_precio(codigo, nuevo_precio, cartelera):
    if buscar_codigo(codigo, cartelera):
        for clave in cartelera:
            if clave.upper() == codigo.upper():
                cartelera[clave][0] = nuevo_precio
        return True
    return False

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion,
                      idioma, es_3d, precio, cupos, peliculas, cartelera):
    if buscar_codigo(codigo, cartelera):
        return False
    peliculas[codigo] = [titulo.strip(), genero.strip(), duracion,
                          clasificacion, idioma.strip(), es_3d]
    cartelera[codigo] = [precio, cupos]
    return True

def eliminar_pelicula(codigo, peliculas, cartelera):
    if buscar_codigo(codigo, cartelera):
        clave_encontrada = None
        for clave in peliculas:
            if clave.upper() == codigo.upper():
                clave_encontrada = clave
        del peliculas[clave_encontrada]
        del cartelera[clave_encontrada]
        return True
    return False

def main():
    peliculas = {
        'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
        'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
        'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
        'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
        'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
        'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    }
    cartelera = {
        'P101': [5990, 40],
        'P102': [7990, 0],
        'P103': [4990, 25],
        'P104': [6990, 12],
        'P105': [8990, 8],
        'P106': [7490, 3],
    }

    salir = False
    while salir == False:
        menu()
        opc = leer_opc()

        if opc == 1:
            genero = input("Ingrese genero a consultar: ")
            cupos_genero(genero, peliculas, cartelera)

        elif opc == 2:
            valores_validos = False
            while valores_validos == False:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    valores_validos = True
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, peliculas, cartelera)

        elif opc == 3:
            repetir = "s"
            while repetir == "s":
                codigo = input("Ingrese codigo de pelicula: ")
                precio_valido = False
                while precio_valido == False:
                    try:
                        nuevo_precio = int(input("Ingrese nuevo precio: "))
                        precio_valido = True
                    except ValueError:
                        print("El precio debe ser un numero entero")
                if actualizar_precio(codigo, nuevo_precio, cartelera):
                    print("Precio actualizado")
                else:
                    print("El codigo no existe")
                repetir = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()

        elif opc == 4:
            print("\n--- Agregar Pelicula ---")
            codigo = input("Ingrese codigo de pelicula: ")
            titulo = input("Ingrese titulo: ")
            genero = input("Ingrese genero: ")
            duracion_str = input("Ingrese duracion (minutos): ")
            clasificacion = input("Ingrese clasificacion: ")
            idioma = input("Ingrese idioma: ")
            es_3d_str = input("¿Es 3D? (s/n): ")
            precio_str = input("Ingrese precio: ")
            cupos_str = input("Ingrese cupos: ")

            if not validar_texto(codigo):
                print("El codigo no puede estar vacio ni ser solo espacios en blanco")
            elif buscar_codigo(codigo, cartelera):
                print("El codigo ya existe")
            elif not validar_texto(titulo):
                print("El titulo no puede estar vacio ni ser solo espacios en blanco")
            elif not validar_texto(genero):
                print("El genero no puede estar vacio ni ser solo espacios en blanco")
            elif not validar_entero_mayor_cero(duracion_str):
                print("La duracion debe ser un numero entero mayor que cero")
            elif not validar_clasificacion(clasificacion):
                print("La clasificacion debe ser exactamente 'A', 'B' o 'C'")
            elif not validar_texto(idioma):
                print("El idioma no puede estar vacio ni ser solo espacios en blanco")
            elif es_3d_str.strip().lower() not in ("s", "n"):
                print("Debe ingresar 's' o 'n'")
            elif not validar_entero_mayor_cero(precio_str):
                print("El precio debe ser un numero entero mayor que cero")
            elif not validar_entero_mayor_igual_cero(cupos_str):
                print("Los cupos deben ser un numero entero mayor o igual que cero")
            else:
                es_3d = True if es_3d_str.strip().lower() == "s" else False
                agregada = agregar_pelicula(
                    codigo, titulo, genero, int(duracion_str), clasificacion,
                    idioma, es_3d, int(precio_str), int(cupos_str),
                    peliculas, cartelera
                )
                if agregada:
                    print("Pelicula agregada")
                else:
                    print("El codigo ya existe")

        elif opc == 5:
            print("\n--- Eliminar Pelicula ---")
            codigo = input("Ingrese codigo de pelicula a eliminar: ")
            if eliminar_pelicula(codigo, peliculas, cartelera):
                print("Pelicula eliminada")
            else:
                print("El codigo no existe")

        elif opc == 6:
            salir = True
            print("Programa finalizado.")
main()
