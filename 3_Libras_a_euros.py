
print("Hola, esta es un programa para convertir libras esterlinas (£) a euros ()")

libra = float(input("Introduce la cantidad de libras esterlinas que deseas convertir"))

print("Introdujiste {} libra(s)".format(libra))

euro = 1.16837
conversion = libra * euro

print("{} libra(s) son {} euro(s)".format(libra,conversion))

print("Gracias por utilizar mi programa :)")

"""
###
    Agrego aquí otra forma de hacerlo, en este el usuario introduce el valor de la moneda en ese día, lo ideal sería juntarlos por que,
    el otro tiene mejor interfaz con el usuario.

print("Hola!, este es un conversor de Libras esterlinas a euros")
l = float(input("¿Cuántas libras esterlinas quieres convertir a euros? "))
c = float(input("¿Cuál es el valor del euro respecto a la libra esterlina? "))

print("1 libra = {} euros".format(c))
conversión = l * c

print("{} libras son {} euros".format(l, conversión))

print("Gracias por usar este conversor :)")

"""