from pathlib import Path
import json
import csv

home = Path(__file__).parent.parent
jfile = Path(home/'dato.json')
cfile = Path(home/'exportar.csv')
menup = ['Ver Listado de Pinturas',
         'Buscar Pintura',
         'Agregar Pintura',
         'Eliminar Pintura',
         'Exportar Pinturas']