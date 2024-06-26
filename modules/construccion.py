from os import system
from pathlib import Path
import json
import csv

def limpiar_pantalla():
    '''
    Limpia los output de la terminal
    '''
    system('Cls')
    return limpiar_pantalla()

def listar(literable):
    for ind, opt in enumerate(literable):
        print(F'{ind + 1}. {opt}')

def sol_ans():
    resp = input('Ingresa una opción:\n')
    return resp

def existencia(archivo):
    if not archivo.exists():
        archivo.touch()

def extracion(archivo):
    if '.json' in str(archivo):
        if archivo.stat().st_size == 0:
            return None
        with open(archivo, 'r') as stream:
            contenido = json.load(stream)
            return contenido
    elif '.cvs' in str(archivo):
        with open(archivo, 'r') as stream:
            contenido = csv.load(stream)
            return contenido
    else:
        return None
    
def verificacion_cont(contenido):
    if contenido == None:
        print('El formato del archivo es invalido\n')
        return None
    elif len(contenido) == 0:
        print('No hay contenido\n')
        return None
    return contenido

def listar_json(contenido):
    if contenido == None:
        print('Ha ocurrido un error inesperado')
        print('Verifica la valides del archivo origen o su contenido\n')
    else:
        for elemento in contenido:
            listar(elemento)

def sol_data():
    resp = input('Ingresa el parametro de la busqueda\n')
    return repr

def buscar(contenido, parametro):
    for elemento in contenido:
        for valor in elemento.values():
            if parametro.upper() in str(valor).upper():
                listar(elemento)

                