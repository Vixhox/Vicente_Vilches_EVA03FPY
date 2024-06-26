

from modules.construccion import  listar, sol_ans, existencia, extracion, verificacion_cont,limpiar_pantalla, listar_json, sol_data, buscar
from modules.data import menup,jfile,cfile
from modules.agregar import Agregar
from modules.eliminar import borrar,slt_code
from modules.exportar import exportar



while True:
    listar(menup)
    ans = sol_ans()
    limpiar_pantalla
    if ans == '1':
        existencia(jfile)
        content = verificacion_cont(extracion(jfile))
        listar_json(content)
    elif ans == '2':
        existencia(jfile)
        content = verificacion_cont(extracion(jfile))
        buscar(content, sol_data())
    elif ans == '3':
        Agregar(jfile)
    elif ans == '4':
        borrar(slt_code, jfile)
    elif ans == '5':
        exportar(jfile, cfile)
    else:
        print('Error: Opción inválida!')

