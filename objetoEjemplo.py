#hacer referencia a un archivo en python
from ClaseEjemplo import ClaseEjemplo

#instanciar la clase o crear un objeto
ejemplo = ClaseEjemplo()

#llamar al metodo para asignar un dato al valor1
ejemplo.setValor1(float(input("INGRESE UN VALOR NUMERICO: ")))
ejemplo.setValor2(float(input("INGRESE OTRO VALOR NUMERICO: ")))

#llamando al metodo que retorna el contenido valor1
#MUESTRA LA SUMA
print(ejemplo.calcularSuma())
print()
#MUESTRA LA MULTIPLICACION
print(ejemplo.calcularMulti())
print()
#MUESTRA EL PROMEDIO
print(ejemplo.calcularPromedio())
print()
#MUESTRA SI ES MAYOR O MENOR
print(ejemplo.verificarMayorMenor())
print(ejemplo.verificarMayorMenor2())
ejemplo.verificarMayorMenor3()
print()
#MUESTRA SI EL PRODUCTO ES PAR O IMPAR
print(ejemplo.verProducto())
print()
#MUESTRA LA RAIZ CUADRADA DE LA SUMA
print(ejemplo.verRaiz())

