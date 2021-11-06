#clases = inicial mayuscula
#atributos y metodos = inicial minuscula
#metodos el nombre se aconseja que inicie con un verto
import math


class ClaseEjemplo():
    #atributos
    valor1=0
    valor2=0
    multiplicar=0
    #metodos
    #metodo para asignar datos al atributo valor1
    def setValor1(self, valor1):
        self.valor1 = valor1

    #metodo para obtener el contenido del atributo valor1
    def getValor1(self):
        return self.valor1

    def setValor2(self, valor2):
        self.valor2 = valor2

    def calcularSuma(self):
        return "la suma es: ", self.valor1 + self.valor2

    def calcularMulti(self):
        return "La multiplicacion es: ", self.valor1 * self.valor2

    def calcularPromedio(self):
        return "el promedio es: ", (self.valor1 + self.valor2) / 2

    def verificarMayorMenor(self):
        respuesta=""
        if(self.valor1 > self.valor2):
            respuesta="el mayor es: ", self.valor1, " el menor es: ", self.valor2
        elif(self.valor2>self.valor1):
            respuesta="el mayor es: ", self.valor2, " el menor es: ", self.valor1
        else:
            respuesta="los numeros son iguales"

        return respuesta

    def verificarMayorMenor2(self):
        if(self.valor1 > self.valor2):
            return "el mayor es: ", self.valor1, " el menor es: ", self.valor2
        elif(self.valor2>self.valor1):
            return "el mayor es: ", self.valor2, " el menor es: ", self.valor1
        else:
            return "los numeros son iguales"

    def verificarMayorMenor3(self):
        if(self.valor1 > self.valor2):
            print("el mayor es: ", self.valor1, " el menor es: ", self.valor2)
        elif(self.valor2>self.valor1):
            print("el mayor es: ", self.valor2, " el menor es: ", self.valor1)
        else:
            print("los numeros son iguales")

    def verProducto(self):
        multiplicar=self.valor1*self.valor2
        if multiplicar%2==0:
            print("EL NUMERO: ", multiplicar, " ES NUMERO PAR")
        else:
            print("EL NUMERO: ", multiplicar, " ES NUMERO IMPAR")

    def verRaiz(self):
        suma=self.valor1+self.valor2
        raiz=math.sqrt(suma)
        print("LA RAIZ CUADRADA DE LA SUMA ES: ",raiz)
