{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b27a2c41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "¡Veremos cuanto tardas en responder estas 5 operaciones!\n",
      "1- ¿Cuánto es 8 / 6?\n",
      "resultado: 1\n",
      "el resultado es correcto\n",
      "2- ¿Cuánto es 1 + 1?\n",
      "resultado: 1\n",
      "\n",
      " el resultado correcto es 2\n",
      "3- ¿Cuánto es 2 - 3?\n",
      "resultado: 1\n",
      "\n",
      " el resultado correcto es -1\n",
      "4- ¿Cuánto es 8 / 7?\n",
      "resultado: 1\n",
      "el resultado es correcto\n",
      "5- ¿Cuánto es 7 + 2?\n",
      "resultado: 1\n",
      "\n",
      " el resultado correcto es 9\n",
      "\n",
      " Tardaste 3 segundos y tuviste 2 resultados correctos\n"
     ]
    }
   ],
   "source": [
    "from random import choice, randrange\n",
    "from datetime import datetime\n",
    "\n",
    "#Operadores posibles\n",
    "operators = [\"+\", \"-\",\"*\",\"/\"] \n",
    "operator2 = [\"+\", \"-\",\"*\"]\n",
    "\n",
    "#Cantidad de cuentas a resolver\n",
    "times = 5\n",
    "\n",
    "#Contador inicial de tiempo.\n",
    "#Esto toma la fecha y hora actual.\n",
    "init_time = datetime.now() \n",
    "print(f\"¡Veremos cuanto tardas en responder estas {times} operaciones!\")\n",
    "k=0 \n",
    "for i in range(0, times):\n",
    "\n",
    "#Se eligen números y operador al azar\n",
    "    number_1 = randrange(10)\n",
    "    number_2 = randrange(10)\n",
    "    \n",
    "    if number_2 == 0:\n",
    "        operator = choice(operator2)\n",
    "    else:\n",
    "        operator = choice(operators)\n",
    "        \n",
    "#Se imprime la cuenta.\n",
    "    print(f\"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?\")\n",
    "#Le pedimos al usuario el resultado\n",
    "    result = float(input(\"resultado: \"))\n",
    "    if operator == \"+\":\n",
    "        resultado2 = number_1 + number_2\n",
    "    elif operator == \"-\":\n",
    "        resultado2 = number_1 - number_2\n",
    "    elif operator == \"*\":\n",
    "        resultado2 = number_1 * number_2\n",
    "    else:\n",
    "        resultado2 = number_1 / number_2\n",
    "\n",
    "\n",
    "\n",
    "   # resultado = float(result)\n",
    "\n",
    "    if result == int(resultado2) :\n",
    "        k=k+1\n",
    "        print(\"el resultado es correcto\")\n",
    "    else:\n",
    "        K=k\n",
    "        print(f\"\\n el resultado correcto es {resultado2}\")\n",
    "\n",
    "\n",
    "    \n",
    "\n",
    "    \n",
    "#Al terminar toda la cantidad de cuentas por resolver.\n",
    "#Se vuelve a tomar la fecha y la hora.\n",
    "end_time = datetime.now()\n",
    "\n",
    "#Restando las fechas obtenemos el tiempo transcurrido.\n",
    "total_time = end_time - init_time\n",
    "\n",
    "#Mostramos ese tiempo en segundos.\n",
    "print(f\"\\n Tardaste {total_time.seconds} segundos y tuviste {k} resultados correctos\" )"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09fad0eb",
   "metadata": {},
   "source": [
    " "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
