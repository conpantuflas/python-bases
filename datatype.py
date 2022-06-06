
"""
comprobar = [38,24,99,42,2,3,11,23,53,21,3,53,77,12,34,92,122,1008,26]
filt = filter(lambda x: x % 2 == 0, comprobar)
pares = list(filt)
print(pares)
"""

"""
mi_variable = lambda x: x % 2 == 0
print(mi_variable(7))
"""

"""
apodo = "ale"
apodo += "jandra"
print(apodo)
"""

"""
mensaje = "Hola Ernesto"
busqueda = mensaje.find("Ernesto") 
print(busqueda)
"""
"""
mensaje = "Hola Ernesto"
extraccion = mensaje[5:12]
print(extraccion)
"""

"""
rapid = lambda x: x[:-1]
print(rapid("bob")) 
"""

"""
def dollar_to_euro(dollar_value):
	return dollar_value * 0.89

def euro_to_yen(euro_value):
	return euro_value * 124.15

valor = dollar_to_euro(137)
valor2 = euro_to_yen(121.93)
valor3 = euro_to_yen(dollar_to_euro(137))
print(valor3)
"""


"""
render_person = "{0} is a {1} years old, {2} born in {3} with {4}"
print(render_person.format('Bob', '05/22/1983', 'green', '23', 'male'))
"""
   

"""
cadena = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}" 
cadena = cadena.format(100, 21, 121) 
print(cadena)
"""
"""
lista = ["z","a","b","k","j","s"]
lista.sort()
print(lista)
"""

"""
names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']
names.sort()
print(names)
"""

names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']
## CREATE YOUR FUNCTION HERE
def sort_names(li):
li.sort()

print(sort_names(names))

