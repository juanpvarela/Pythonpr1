from random import choice, randrange
from datetime import datetime

#Operadores posibles. Genero dos listas, una con la división (Para el caso que el segundo número sea distinto de 0) y una para cuando sea igual.
operators = ["+", "-","*","/"]
operator2 = ["+", "-","*"]

#Cantidad de cuentas a resolver
times = 5

#Contador inicial de tiempo.
#Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
k=0
for i in range(0, times):

#Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)

#Hacemos un if para poner una condición si el número 2 es 0, ya que no está definida la división con denominador igual  a 0.
    if number_2 == 0:
        operator = choice(operator2)
    else:
        operator = choice(operators)
       
#Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
#Le pedimos al usuario el resultado
    result = float(input("resultado: "))

#Hacemos una sentencia if para que el programa realice las cuentas dependiendo del operador que se haya generado aleatoriamente 
    if operator == "+":
        resultado2 = number_1 + number_2
    elif operator == "-":
        resultado2 = number_1 - number_2
    elif operator == "*":
        resultado2 = number_1 * number_2
    else:
        resultado2 = number_1 / number_2



#Multiplico result y resultado2 por 10 así tengo en cuenta que el resultado este bien hasta el primer decimal.
    if result*10 == int(resultado2*10) :
        k=k+1
        print("El resultado es correcto")
    else:
        K=k
        print(f"\n Incorrecto. El resultado correcto es {resultado2}")


   

   
#Al terminar toda la cantidad de cuentas por resolver.
#Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()

#Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time

#Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos y tuviste {k} resultados correctos" )
