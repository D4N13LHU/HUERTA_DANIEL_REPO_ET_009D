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

def busqueda_planes_rango_precio():
    print('=' * 60)
    print('***** BUSQUEDA DE PLANES POR RANGO DE PRECIO *****')
    print('=' *60, '\n')
    precio_min, precio_max = filtro_planes_rango_precio()
    if precio_min is None:
        print("Operacion cancelada \n")
        return
    planes_en_rango = []
    for codigo,(precio_cupo) in inscripciones, items():
        if (precio_min <= precio <= precio_max) and (cupo > 0):
            planes_en_rango.append((codigo,planes[codigo][0], precio_cupo))
    if planes_en_rango:
        print (f'planes disponibles en el rango de precio ${precio_min} - {precio_max}: ')
        for codigo, plan, precio, cupo, in planes_en_rango:
            print(f'codigo: {codigo}, Plan: {plan}, precio: ${precio}, Cupo: {cupo} ')
        print('\n')
    else:
        print(f'No se encontraron planes disponibles en el rango de precio ${precio_min} - {precio_max}. \n')

def buscar_codigo_plan():
    while True:
        codigo_plan = input('Ingrese el codigo del plan a buscar (O "Salir" para cancelar)')
        if codigo_plan.lower() == "Salir":
            return False, ""
        elif codigo_plan.strip == "":
            print('Error, el codigo no puede quedar vacio o contener solo espacios blancos. \n')
        elif codigo_plan not in inscripciones:
            print(f'El codigo {codigo_plan} no se encuentra en el diccionario. \n')
        else:
            print(f'El codigo {codigo_plan} se encuentra en el diccionario. \n')
            print(f'Detalles: {planes[codigo_plan]}')
            print(f'Precio: ${inscripciones[codigo_plan][0]}, stock: {inscripciones[codigo_plan][1]} \n')
            return True, codigo_plan

def validar_precio_plan():
    estado_busqueda, codigo_plan = buscar_codigo_plan()
    if estado_busqueda == False:
        return False, codigo_plan
    else:
        while True:
            respuesta = input(f'¿Desea actualizar el precio del plan {codigo_plan} (S/N)?: ').lower
            if respuesta == 'N':
                return False, codigo_plan
            elif respuesta == 'S':
                precio_nuevo = input(f'Ingrese el nuevo precio para el plan {codigo_plan}: ')
                if precio_nuevo.strip() == "":
                    print('Error, el precio no puede quedar vacio. \n')
                else:
                    try:
                        precio_nuevo = int(precio_nuevo)
                        if precio_nuevo < 0:
                            print('Error, el precio no puede ser negativo, por favor ingrese un numero valido. \n')
                        else:
                            inscripciones[codigo_plan][0] = int(precio_nuevo)
                            return True, codigo_plan
                    except ValueError as e:
                        print('Error, el valor ingresado no es valido. Por favor, ingrese un numero valido. \n')
                        print('Detalle del error: ', e)

            else:
                print('opcion invalida. Por favor ingrese "S" para sí, o "N" para no. \n')

def actualizar_precio_plan():
    estado_actualizacion, codigo_plan = validar_precio_plan()
    if estado_actualizacion:
        print(f'El precio del plan {codigo_plan} ha sido actualizado a: {inscripciones[codigo_plan][0]}\n')
    else:
        print('Se ha cancelado la operación. \n')


#validaciones

def validar_codigo(codigo_nuevo):
    if codigo_nuevo.strip() == "":
        print('Error: el codigo del nuevo plan no puede quedar vacio. \n')
        return False
    return True

def validar_plan(plan_nuevo):
    if plan_nuevo.strip() == "":
        print('Error: el nombre del nuevo plan no puede quedar vacio. \n')
        return False
    return True

def validar_duracion(duracion_nueva):
    if duracion_nueva.strip() == "":
        print('Error: la nueva duracion del nuevo plan no puede queedar vacia. \n')
        return False
    return True

def validar_acceso_piscina(acceso_piscina_nuevo):
    if acceso_piscina_nuevo.strip() == "":
        print('Error: el nuevo acceso a la piscina del nuevo plan no puede quedar vacio. \n')
        return False
    return True

def validar_clases(clases_nueva):
    if clases_nueva.strip() == "":
        print('Error: Las clases nuevas al nuevo plan no puede quedar vacio. \n')
        return False
    return True

def validar_horario(nuevo_horario):
    if nuevo_horario.strip() == "":
        print('Error: El nuevo horario al nuevo plan no puede quedar vacio. \n')
        return False
    return True

def validar_precio(precio_nuevo):
    if precio_nuevo.strip() == "":
        print('Error: El precio nuevo del nuevo plan no puede quedar vacio. \n')
        return False
    else:
        try:
            precio_nuevo = int(precio_nuevo)
            if precio_nuevo <= 0:
                print('Error: El precio no puede ser igual o menor a 0 \n')
                return False
            return True
        except ValueError as e:
            print('Error: El precio debe ser un valor numerico entero \n')
            return False

def validar_cupos(nuevo_cupo):
    if nuevo_cupo < 0:
        print('Error: El cupo no puede ser menor a cero. \n')
        return False
    return True

def agregar_plan():
    print('=' * 60)
    print('***** AGREGAR NUEVO PLAN *****')
    print('=' * 60, '\n')

    codigo_nuevo = (input('Ingrese el codigo del nuevo plan: '))
    plan_nuevo = (input('Ingrese el nombre del nuevo plan: '))
    duracion_nueva = (input('Ingrese la nueva duracion del plan'))
    acceso_piscina_nuevo = (input('Ingrese el acceso a la piscina nuevo'))
    clases_nueva = (input('Ingrese las clases nueva al nuevo plan'))
    nuevo_horario = (input('Ingrese el nuevo horario al plan'))
    precio_nuevo = (input('Ingrese el precio del nuevo plan'))
    nuevo_cupo = (input('Ingrese el nuevo cupo del nuevo plan'))

    bool_codigo = validar_codigo(codigo_nuevo)
    bool_plan_nuevo = validar_plan(plan_nuevo)
    bool_duracion_nueva = validar_duracion(duracion_nueva)
    bool_acceso_piscina_nuevo = validar_acceso_piscina(acceso_piscina_nuevo)
    bool_clases_nueva = validar_clases(clases_nueva)
    bool_nuevo_horario = validar_horario(nuevo_horario)
    bool_precio_nuevo = validar_precio(precio_nuevo)
    bool_nuevo_cupo = validar_cupos(nuevo_cupo)

    #verificar validaciones

    if (bool_codigo and bool_plan_nuevo and bool_duracion_nueva and bool_acceso_piscina_nuevo and bool_clases_nueva and bool_nuevo_horario and bool_precio_nuevo and bool_nuevo_cupo):
        if codigo_nuevo in planes 





def eliminar_planes():
    print('=' *60)
    print('***** ELIMINAR PLANES *****')
    print('=' *60)
    bool_codigo, codigo_plan = buscar_codigo_plan()



def main():
    while True:
        Menu_principal()
        opcion = leer_opcion()
        if opcion == 1
        elif opcion == 2
        elif opcion == 3
        elif opcion == 4
        elif opcion == 6
        print ('Muchas gracias!')
        exit(0)

    else:
        return False
    
    main()


