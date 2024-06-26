import json
import csv
import os

def Agregar(jsonf):
    if not jsonf.exists():
        jsonf.touch()
        print('la base de datos no existia y fue creada corectamente')
    if jsonf.stat().st_size == 0:
        json_file = []
        codp = 1
    else:
        with open(jsonf, mode='r') as stream:
            json_file = json.load(stream)
            codp = []
        for Pintura in  json_file:
            codp.append(Pintura['codigo'])
        codp = max(codp) + 1
    while True:
        print('ingresa el nombre de la pintura\n')
        nomp = input('Color de pintura: ').upper()
        ans = input(f'Color de pinrura: {nomp}\nes correcto el color?\n1.si\n2.no\n')
        if ans == '1':
            break
        else:
            os.system('Cls')
    data = {'codigo': codp,
            'Color de pintura' : nomp
            }
    json_file.append(data)
    with open(jsonf, mode='w') as stream:
        json.dump(json_file, stream)
    print('Color agregado con exito\n')