from data_stark import lista_personajes

#A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
def mostrar_nombres(lista:list):
    '''
    Brief:
    - Muestra por terminal todos los nombres que se encuentren en una lista
    Param:
    - lista: La lista de donde debe iterar en busca de los nombres
    Return: 
    - No tiene return
    '''
    for i in range(len(lista)):
        print(f"{(lista[i]['nombre'])}\n")

#B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
def mostrar_mayor_fuerza(lista:list)->list:
    '''
    Brief:
    - Muestra por terminal la identidad y peso del heroe mas fuerte de la lista
    Param:
    - lista: La lista de donde debe iterar para encontrar al mas fuerte
    Return: 
    - Devuelve una lista con la identidad y peso del heroe
    '''
    primera_flag = True
    heroe_mas_fuerte = []
    for heroe in lista:
        peso_float = float(heroe["peso"])
        if primera_flag == True or peso_float > peso_mayor:
            peso_mayor = peso_float
            identidad_heroe_fuerte = heroe["identidad"]
            primera_flag = False
    heroe_mas_fuerte.append(peso_mayor)
    heroe_mas_fuerte.append(identidad_heroe_fuerte)
    return heroe_mas_fuerte

#C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)
def mostrar_menor_altura(lista:list)->list:
    '''
    Brief:
    - Muestra por terminal la identidad y el nombre del heroe mas bajo de la lista
    Param:
    - lista: La lista de donde debe iterar para encontrar al mas bajo
    Return: 
    - Devuelve una lista con la identidad y el nombre del heroe
    '''
    primera_flag = True
    heroe_mas_bajo = []
    for heroe in lista:
        altura_float = float(heroe["altura"])
        if primera_flag == True or altura_float < menor_altura:
            menor_altura = altura_float
            identidad_heroe_bajo = heroe["identidad"]
            nombre_heroe_bajo = heroe["nombre"]
            primera_flag = False
    heroe_mas_bajo.append(identidad_heroe_bajo)
    heroe_mas_bajo.append(nombre_heroe_bajo)
    return heroe_mas_bajo


def calcular_promedio(numero_1, numero_2)->float:
    '''
    Brief:
    - Divide dos numeros que se les pase por parametro y lo devuelve
    Param:
    - numero_1: el dividendo
    - numero_2: el divisor
    Return: 
    - Devuelve el resultado de la division
    '''
    if numero_2 == 0:
        print("No se puede dividir por 0")
    else:
        promedio = numero_1 / numero_2
        return promedio

#D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
def mostrar_promedio_masculinos(lista:list)->float:
    '''
    Brief:
    - Muestra por terminal el promedio de peso de los heroes masculinos
    Param:
    - lista: La lista de donde debe iterar para encontrar los pesos de los heroes masculinos
    Return: 
    - Devuelve una lista con el promedio de peso de heroes masculinos
    '''
    acumulador_peso = 0
    contar_heroes = 0
    for heroe in lista:
        if heroe["genero"] == "M":
            peso_float = float(heroe["peso"])
            contar_heroes += 1
            acumulador_peso += peso_float
    promedio = calcular_promedio(acumulador_peso, contar_heroes)
    return promedio

#E
def mostrar_promedio_femenino(lista:list)->float:
    '''
    Brief:
    - Muestra por terminal el promedio de peso de los heroes femeninos
    Param:
    - lista: La lista de donde debe iterar para encontrar los pesos de los heroes femeninos
    Return: 
    - Devuelve una lista con el promedio de peso de heroes femeninos
    '''
    acumulador_fuerza = 0
    contar_heroes = 0
    for heroe in lista:
        if heroe["genero"] == "F":
            fuerza_float = float(heroe["fuerza"])
            contar_heroes += 1
            acumulador_fuerza += fuerza_float
    promedio = calcular_promedio(acumulador_fuerza, contar_heroes)
    return promedio

#E. Recorrer la lista y mostrar nombre y peso de los superhéroes (de cualquier género), los cuales su fuerza 
#   supere a la fuerza promedio de todas las superhéroes de género femenino
def mostrar_fuertes_al_promedio(lista:list)->list:
    '''
    Brief:
    - Muestra por terminal el nombre y peso de los heroes que superen la fuerza promedio de los heroes femeninos
    Param:
    - lista: La lista de donde debe iterar para encontrar y comparar los pesos de los heroes 
    Return: 
    - Devuelve una lista con el nombre y peso de los heroes que superan el promedio de heroes femeninos
    '''
    promedio = mostrar_promedio_femenino(lista)
    heroes_mas_fuertes = []
    print(f"El promedio de fuerza de los heroes femeninos es de: {promedio:.2f}\n")
    for heroe in lista:
        fuerza_float = float(heroe["fuerza"])
        if fuerza_float > promedio:
            peso_float = float(heroe["peso"])
            nombre_heroe = heroe["nombre"]
            heroes_mas_fuertes.append({
                "Nombre": nombre_heroe,
                "Peso": peso_float,
            })
    return heroes_mas_fuertes