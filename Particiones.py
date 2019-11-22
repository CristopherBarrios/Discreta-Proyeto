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
particiones = [[]]  #result
num = 0
longitud = 0
particiones = 0
opcion = ""

def particion(entero,longitud):
    for i in range(len(entero)):
            for j in range(longitud):
                if(i - j < 0):
                    particiones [i,j] = particiones [i,j -1]
                else:
                    particiones [i,j] = particiones [i,j -1] + particiones[i - j, j]
    return particiones[entero,longitud]

def imprimir_particiones(numero, objetivo):
    for x in :
        pass
    pass
print("Proyecto de discreta - Particion de un entero \n" + "Integrantes: Mario Perdomo 18029\nJosue Sagastume 18173\nChristopher Barrios 18207")
while(opcion != "2"):
    opcion = input("1. Particion de un entero\n2. Salir")
    if(opcion == "1"):
        num = int(input("Ingrese el numero entero a partir: "))
        longitud = int(input("Ingrese la longitud de las particiones(escriba 0 para todas las particiones): "))

    elif(opcion == "2"):
        print("nucnadadad")

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