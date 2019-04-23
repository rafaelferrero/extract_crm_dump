from getopt import getopt, GetoptError
from sys import argv, exit
from datetime import datetime as dt
from settings import lines_to_search


def get_save_name():
    return str(int(dt.timestamp(dt.now())))


def main(argument):
    path_to_ifile = ''
    path_to_ofile = ''
    try:
        opts, args = getopt(argument, "hi:o:", ["ifile=", "ofile="])
    except GetoptError:
        print(
             'Este script extrae las sentencias INSERT del archivo DUMP de SuiteCRM para el software de' +
             '\n' + ' comparación de bases de datos, para lo cual debe descargar el archivo del servidor web' +
             '\n' + ' vía FTP e ingresarlo así:'
             '\n' + 'Sugar4Compare.py -i <crm_dump_file>'
        )
        exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python Sugar4Compare.py -i <crm_dump_file>')
            exit()
        elif opt in ("-i", "--ifile"):
            path_to_ifile = arg
        elif opt in ("-o", "--ofile"):
            path_to_ofile = arg

    if not path_to_ofile:
        path_to_ofile = get_save_name() + '.sql'

    if path_to_ifile:
        lines = []
        outputfile = open(path_to_ofile, "w+", encoding="utf8")
        with open(path_to_ifile, "rt", encoding="utf8") as opened_file:
            for line in opened_file.readlines():
                for item in lines_to_search:
                    if item in line:
                        outputfile.write(line)
            outputfile.write('UNLOCK TABLES;')
    else:
        print(
             'Este script extrae las sentencias INSERT del archivo DUMP de SuiteCRM para el software de' +
             '\n' + ' comparación de bases de datos, para lo cual debe descargar el archivo del servidor web' +
             '\n' + ' vía FTP e ingresarlo así:'
             '\n' + 'Sugar4Compare.py -i <crm_dump_file>'
        )
        exit(2)


if __name__ == "__main__":
    main(argv[1:])
