import json

def slt_code():
    code = input('Ingresa el codigo del color a eliminar:\n')
    if code.isnumeric():
        return int(code)
    
def borrar(dato, rutaj):
    if dato == None:
        print('El fromato del codigo no es correcto')
    else:
        with open(rutaj, 'r') as stream:
            json_file = json.load(stream)
            for pintura in json_file:
                if pintura['codigo'] == dato:
                    json_file.remove(pintura)
                    print('Color eliminado correctamente\n')
            with open(rutaj, 'w') as stream:
                json.dump(json_file, stream)