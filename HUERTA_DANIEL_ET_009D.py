#GIMNASIO FITPASS

#Diccionario 1
planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}

#Diccionario 2
inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15]
}

#CREACION DEL MENU
def Menu_principal():
    print('=' * 60)
    print('***** BIENVENIDO A GIMNASIO FITPASS *****')
    print('=' * 60, '\n')
    print('1. Cupos por tipo de plan')
    print('2. Búsqueda de planes por rango de precio')
    print('3. Actualizar precio de plan')
    print('4. Agregar plan')
    print('5. Eliminar plan')
    print('6. Salir')

def leer_opcion():
    while True:
        opcion = input('Ingrese una opcion (De la 1 a la 6): ')
        if opcion.strip() == "":
            print("Error, la opcion no puede quedar vacía, ingrese un numero entre 1 y 6")
        else:
            try:
                opcion = int(opcion)
                if opcion not in (1,2,3,4,5,6):
                    print('Error la opcion ingresada no es valida, Por favor ingrese un número entre 1 y 6: ')
                else:
                    return opcion
            except ValueError as e:
                print('Error, la opcion ingresada no es valida. Por favor ingrese un número entre 1 y 6')
                print('Detalle del error:', e)


