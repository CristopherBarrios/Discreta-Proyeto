"""
Univesidad del valle de Guatemala
Seccion xx - MM2015
Matematica discreta

Mario Perdomo 18029
Josue Sagastume 18173
Christopher Barrios 181xx
Proyecto 1: Particion de un entero
"""

#Son todas las posibles respuestas respecto al numkero 'k'
particiones = [] 
num = 0
particiones = __gen_particiones(num)
def print_particiones(particiones):
    # Es lo que separa las respuesta
    string_particiones = ''
    for serie in particiones:
        #Muestra la n cantidad de respuestas que sumados dan el numero "k"
        string_particiones += str(num) + ' = ' + ' + '.join([str(num) for num in serie]) + '\n'
        print (string_particiones)
 
def order_particiones(particiones):
    order_particiones = []
    for serie in gen_particiones(num):
        order_particiones.append(sorted(serie, reverse=True))
        particiones = order_particiones
 
def gen_particiones(particiones, num, limit = False):
    # Es cuanto el limite sea 0
    if limit == False: limit = num
        if num == 1:
            yield [1]
        elif num < 1:
            yield []
        else:
            for x in range(min(num, limit), 0, -1):
                if num == x: continue
                for i in gen_particiones(num - x, x):
                    i.append(x)
                    yield i