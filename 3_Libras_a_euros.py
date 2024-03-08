
print("Hola, esta es un programa para convertir libras esterlinas (£) a euros ()")

libra = float(input("Introduce la cantidad de libras esterlinas que deseas convertir"))

print("Introdujiste {} libra(s)".format(libra))

euro = 1.16837
conversion = libra * euro

print("{} libra(s) son {} euro(s)".format(libra,conversion))

print("Gracias por utilizar mi programa :)")