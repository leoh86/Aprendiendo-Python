

numero1 = int(input("Hola, este es mi primer programa de python, ¿Me harías el favor de introducir 3 números? Va,"
                    " elige un número entero no importa que tan grande o pequeño sea: "))
print("Tu primer número es: {}".format(numero1))

numero2 = int(input("Gracias, introduce un segundo número: "))
print("Tu segundo número es: {}".format(numero2))

numero3 = int(input("Perfecto, introduce un tercer número: "))
print("Tu tercer número es: {}".format(numero3))

print("Ahora, voy a hacer un poquito de magia de segundo de primaria y decirte el número mayor y menor, ¿Listo?")

print("El número máyor entre {}, {} y {} es: {}".format(numero1, numero2, numero3, max(numero1,numero2, numero3)))

print("El número menor entre {}, {} y {} es: {}".format(numero1, numero2, numero3, min(numero1,
                                                        numero2, numero3)))

print("Gracias por usar mi primer programa <3")