"""
Univesidad del valle de Guatemala
Seccion 10 - MM2015
Matematica discreta

Mario Perdomo 18029
Josue Sagastume 18173
Christopher Barrios 18207
Proyecto 1: Particion de un entero
"""

#Son todas las posibles respuestas respecto al numkero 'k'
particiones = [] 
num = 0
particiones = gen_particiones(num)
def print_particiones(particiones):
    # Es lo que separa las respuesta
    string_particiones = ''
    for serie in particiones:
        #Muestra la n cantidad de respuestas que sumados dan el numero "k"

        #5 = 1 + 1 + 3
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


"""
 public class IntegerPartition
{
    public static int[,] Result = new int[100,100];

    private static int Partition(int targetNumber, int largestNumber)
    {
        for (int i = 1; i <= targetNumber; i++)
        {
            for (int j = 1; j <= largestNumber; j++)
            {
                if (i - j < 0)
                {
                    Result[i, j] = Result[i, j - 1];
                    continue;
                }
                Result[i, j] = Result[i, j - 1] + Result[i - j, j];
            }
        }
        return Result[targetNumber, largestNumber];
    }

    public static int Main(int number, int target)
    {
        int i;
        for (i = 0; i <= number; i++)
        {
            Result[i, 0] = 0;
        }
        for (i = 1; i <= target; i++)
        {
            Result[0, i] = 1;
        }
        return Partition(number, target);
    }
}

function p(sum,largest): 
    if largest==0: 
        return 0 
    if sum==0: 
        return 1 
    if sum<0: 
        return 0
    return p(sum, largest-1) + p(sum-largest, largest)

    Otra manera de partir el número con una funcion recursiva


Fuente: https://www.i-ciencias.com/pregunta/31123/como-puedo-explicar-esto-entero-particiones-funcion-de-la-recursividad

"""