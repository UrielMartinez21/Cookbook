from pathlib import Path
from os import *

#---> Cambiar ruta de directorio
ruta = Path(Path.home(), "OneDrive", "Escritorio", "Python", "Curso", "dia6_recetario", "Recetas")
chdir(ruta)

#---> Conteo de recetas registradas
lista_recetas = [receta.stem for receta in Path(ruta).glob("**/*.txt")]

#---> Saludo al usuario
def saludar():
    print("[+] Bienvenido al recetario")

#---> Informacion de recetas
def informacion_recetas():
    print("[+] La ruta del recetario esta en: ", getcwd())
    print(f"[+] Hay un total de: {len(lista_recetas)} recetas\n")

#---> Menu de opciones
def elige_opcion():
    print("""Opciones de recetario:
    1)Leer receta
    2)Crear receta
    3)Crear nueva categoria 
    4)Eliminar receta
    5)Eliminar categoria
    6)Finalizar ejecucion
    """)
    opcion = int(input("Escoje una opcion: "))
    return opcion

#---> Categorias disponibles
def mostrar_categorias():
    categorias = listdir(ruta)
    print("Las categorias son: ")
    for categoria in categorias:
        print("\t[+]", categoria)
    return categorias

def categoria_valida(lista):
    while True:
        respuesta = input("[+]Escoje una categoria: ").title()
        if respuesta in lista:
            return respuesta
        else:
            print("-->Ingresa una categoria existente")

#---> Recetas por categoria
def mostrar_receta_categoria(ruta):
    lista_recetas = [receta for receta in Path(ruta).glob("**/*.txt")]
    print("Recetas encontradas:")
    for receta in lista_recetas:
        print("\t[+]", receta.stem)

#---> Leer recetas
def opcion_1():
    print("[+]Escogiste leer receta")
    categorias = mostrar_categorias()
    respuesta=categoria_valida(categorias)
    ruta_categoria = Path(ruta, respuesta)
    system("cls")
    mostrar_receta_categoria(ruta_categoria)
    ruta_receta = input("¿Que receta quieres leer?: ")
    receta = Path(ruta_categoria, ruta_receta+".txt")
    print(receta.read_text())

#---> Crear receta
def opcion_2():
    print("[+]Escogiste crear receta")
    categorias = mostrar_categorias()
    categoria = categoria_valida(categorias)
    ruta_categoria = Path(ruta, categoria)
    chdir(ruta_categoria)
    nombre_receta=input("[+]Nombre de la receta: ") + ".txt"
    contenido_receta=input("[+]Contenido de la receta: ")
    Path.write_text(Path(ruta_categoria,nombre_receta),contenido_receta)
    if path.exists(nombre_receta):
        print("[+]Se creo la receta")

#---> Crear nueva categoria
def opcion_3():
    print("[+]Escogiste crear nueva categoria")
    print("Recuerda: la nueva categoria no debe de existir en el recetario\n")
    categorias=mostrar_categorias()
    while True:
        categoria_nueva = input("Nombre de la nueva categoria: ").title()
        if not categoria_nueva in categorias:
            makedirs(categoria_nueva)
            if path.exists(categoria_nueva):
                print("Se creo la nueva categoria")
                break
        else:
            print("La categoria existe")

#---> Eliminar receta
def opcion_4():
    print("[+]Escogiste eliminar receta")
    categorias = mostrar_categorias()
    respuesta= categoria_valida(categorias)
    ruta_categoria = Path(ruta, respuesta)
    chdir(ruta_categoria)
    system("cls")
    mostrar_receta_categoria(ruta_categoria)
    receta_eliminar = input("¿Que receta quieres eliminar?: ")+".txt"
    remove(receta_eliminar)
    if not path.exists(receta_eliminar):
        print("Se elimino la receta")

#---> Eliminar categoria
def opcion_5():
    print("[+]Escogiste eliminar categoria")
    categorias = mostrar_categorias()
    categoria_eliminar=categoria_valida(categorias)
    rmdir(categoria_eliminar)
    if not path.exists(categoria_eliminar):
        print("Se elimino la categoria")

def seguir():
    input("\n[+]Presiona cualquier tecla para avanzar\t")
    system("cls")


while True:
    #---> Cambiar ruta de directorio
    ruta = Path(Path.home(), "OneDrive", "Escritorio", "Python", "Curso", "dia6_recetario", "Recetas")
    chdir(ruta)

    #---> Conteo de recetas registradas
    lista_recetas = [receta.stem for receta in Path(ruta).glob("**/*.txt")]

    saludar()
    informacion_recetas()
    opcion = elige_opcion()
    system("cls")
    if opcion == 1:           # Funciona
        opcion_1()
        seguir()
    elif opcion == 2:         # Pendiente
        opcion_2()
        seguir()
    elif opcion == 3:         # Funciona
        opcion_3()
        seguir()
    elif opcion == 4:         # Funciona
        opcion_4()
        seguir()
    elif opcion == 5:         # Funciona
        opcion_5()
        seguir()
    elif opcion == 6:         # Funciona
        print("[+]Saliendo del programa...")
        break
