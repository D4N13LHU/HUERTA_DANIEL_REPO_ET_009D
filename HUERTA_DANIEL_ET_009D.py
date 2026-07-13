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

def detalle_plan(codigo_plan):
    print('=' * 60)
    print(f'el codigo {codigo_plan} se encuentra en el diccionario de planes. \n')
    print('=' * 60)
    print(f'Detalles del plan: {planes[codigo_plan]}')
    print(f'Precio plan: ${inscripciones[codigo_plan][0]}')
    print(f'stock disponible de inscripciones: {inscripciones[codigo_plan][1]}')
    print('=' * 60, '\n')

def stock_planes():
    print('=' * 60)
    print('***** STOCK DE PLANES *****')
    print('=' * 60, '\n')
    plan_buscado = input('Ingrese el plan a buscar(ej: Plan basico, plan full, plan estudiante, etc) o escriba "Salir" para cancelar')
    if plan_buscado.lower() == 'Salir':
        print("operacion cancelada. \n")
        return
    if plan_buscado.strip() == "":
        print("Error, el nombre no puede quedar vacío. \n")
        return
    encontrados = False
    for codigo, detalles in planes.items():
        if plan_buscado.lower() in detalles[4].lower():
            detalle_plan(codigo)
            encontrados = True
    if not encontrados:
        print(f'No se encontraron planes con el nombre: {plan_buscado}\n')

def filtro_planes_rango_precio():
    while True:
        print("(Escriba 'Salir' en cualquier momento para cancelar)")
        precio_min = input('Ingrese el precio mínimo: ')
        if precio_min.lower() == 'Salir': return None,None
        precio_max = input('Ingrese el precio máximo: ')
        if precio_max.lower() == 'Salir': return None,None

        if precio_min.strip() == "" or precio_max.strip() == "":
            print('Error, los precios no pueden quedar vacíos o contener solo espacios. \n')
            continue
        try:
            precio_min = float(precio_min)
            precio_max = float(precio_max)

            if precio_min < 0 or precio_max < 0:
                print('Error, los precios no pueden ser negativos. Por favor ingrese valores válidos. \n')
                continue
            if precio_min > precio_max:
                print('Error, el precio minimo no puede ser mayor que el precio máximo, ingrese valores validos')
                continue
            return precio_min, precio_max
        except ValueError as e:
            print('Error, los valores ingresados no son validos. Por favor, ingrese números validos. \n')
            print('Detalle del error:', e)

            
