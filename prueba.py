# mi_archivo=open('texto.txt')
# print(mi_archivo.read())
# mi_archivo.close()

# from pathlib import Path
# carpeta=Path('C:\\Users\\uriel\\OneDrive\\Escritorio\\Python\\Curso\\dia6_recetario\\texto.txt')
# print(carpeta.read_text())

from os import system
nombre=input("Ingresa tu nombre: ")
system("cls")
print(f"Tu nombre es :{nombre}")