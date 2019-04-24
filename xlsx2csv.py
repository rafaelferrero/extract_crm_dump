from getopt import getopt, GetoptError
from sys import argv, exit
from datetime import datetime as dt
import pyexcel as pe


def get_save_name():
    return str(int(dt.timestamp(dt.now())))


def get_help():
    ayuda = 'Este script recibe un archivo xlsx y lo exporta a csv en formato UTF8.'
    ayuda += '\n' + ' como paso previo a la exportación, elimina todo salto de linea dentro de una celda'
    ayuda += '\n' + ' ejecútelo así: python xlsx2csv.py -i <xlsx_file>'
    ayuda += '\n'
    ayuda += '\n' + ' -i o ifile: Indique la ruta al archivo xlsx ejemplo /path/to/file.xlsx'
    ayuda += '\n' + ' -o u ofile: Indique la ruta al archivo csv resultante ejemplo /path/to/file.csv'
    ayuda += '\n' + '   si omite el nombre y la ruta del archivo resultante el sistema creara un nombre'
    ayuda += '\n' + '   basado en la fecha actual del sistema y lo colocará en el directorio local.'
    ayuda += '\n' + ' -h: Imprime esta ayuda.'

    return ayuda


def main(argument):
    path_to_ifile = ''
    path_to_ofile = ''
    try:
        opts, args = getopt(argument, "hi:o:", ["ifile=", "ofile="])
    except GetoptError:
        print(get_help())
        exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(get_help())
            exit()
        elif opt in ("-i", "--ifile"):
            path_to_ifile = arg
        elif opt in ("-o", "--ofile"):
            path_to_ofile = arg

    if not path_to_ofile:
        path_to_ofile = get_save_name() + '.csv'

    if path_to_ifile:
        contenido = pe.get_sheet(file_name=path_to_ifile, start_row=0, row_limit=30)
        import pdb
        pdb.set_trace()
        contenido.save_as(filename=path_to_ofile, delimiter=':', encoding='utf-8-sig')

        # items = []
        # lines = []
        # claves = []
        #
        # for clave in contenido[0].keys():
        #     claves.append(clave)
        #
        # for x in range(15, 18):
        #     for index, registro in enumerate(contenido):
        #         for clave in claves:
        #             items.append(contenido[index][clave])
        #         lines.append(items)
        #         items.clear()
        # import pdb
        # pdb.set_trace()
        #
        # outputfile = open(path_to_ofile, "+", wencoding="utf8")
        # with open(path_to_ifile, "rt", encoding="utf8") as opened_file:
        #     pass


if __name__ == "__main__":
    main(argv[1:])
