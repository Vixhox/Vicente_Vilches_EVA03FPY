import json
import csv

def exportar(rutaj, rutac):
    if not rutaj.exists() or rutaj.stat().st_size == 0:
        print('la base de datos no existe o esta vacia')
    else:
        if not rutac.exists():
            rutac.touch()
        with open(rutaj, 'r') as stream:
            json_file = json.load(stream)
            for pintura in json_file:
                line = [pintura['Color de pintura'],
                        pintura['codigo']]
                with open(rutac, 'a', newline='') as cfile:
                    writer = csv.writer(cfile)
                    writer.writerow(line)