"""
edad = 0
while edad <= 10:
    if edad == 6:
        edad = edad + 1
        continue

    print('tu edad es:'+str(edad))
    edad = edad + 1
"""

"""
my_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

# 1. print the item here
print(my_list[2])
# 2. change the position were 'thursday' is to None
my_list[2] = "thursday"
# 3. print that position now here
print(my_list[2])
"""

"""
lista = ["camilo","patricio"]
lista[0] = "yoselin"
print(lista[0]) 
"""

"""
my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45,3,100,4,56,23]
print(len(my_list))
"""

""""
import random

def generate_random_list():
    aux_list = []
    randonlength = random.randint(1, 100)

    for i in range(randonlength):
        aux_list.append(randonlength)
        i += i
    return aux_list
my_stupid_list = generate_random_list()

the_last_one = generate_random_list()
print(the_last_one[-1])
"""


"""
import random 

aleatorio = random.randrange(0, 100, 1)
arr = []
for i in aletorio:
    print(aleatorio[i])

"""
"""
class Car:
    def __init__(self,cantidad_de_puertas,color,marca,modelo):
        self.puertas = cantidad_de_puertas
        self.color = color
        self.marca = marca
        self.modelo = modelo

    def obtener_modelo(self):
        return self.modelo 
    

carro1 = Car(4,"red","nissan","350z")
carro2 = Car(2,"blue","ford","Explorer")

#print(carro1.marca)
print(carro1.obtener_modelo())
"""


"""
import random

my_list = [4,5,734,43,45]
aleatorio = random.randint(1,100)
for i in range(11):
    my_list.insert(5,aleatorio)


print(my_list)
"""

"""
import random
#Remember import random function here:
my_list = [4,5,734,43,45]
#The magic is here:
for i in range(11):
    my_list.append(i) 

print(my_list)    
"""

"""
lista = []
for i in range(1,18):
    lista.append(i)

print(lista) 
"""

"""
my_list = [232,32,1,4,55,4,3,32,3,24,5,5,5,34,2,35,5365743,52,34,3,55]

#Your code go here:
for i in reversed(range(len(my_list))):
    print(my_list[i])
"""    

"""
names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
names[1] = "Steven"
names[-1] = "Pepe"
concat = names[2] + names[4]
names[0] = concat
print(names[0])

for i in reversed(names):
    print(i)

"""



"""
people = [ 'Lebron','Aaliyah','Diamond','Dominique','Aliyah','Jazmin','Darnell','Hatfield','Hawkins','Hayden','Hayes','Haynes','Hays','Head','Heath','Hebert','Henderson','Hendricks','Hendrix','Henry','Hensley','Henson','Herman','Hernandez','Herrera','Herring','Hess','Hester','Hewitt','Hickman','Hicks','Higgins','Hill','Hines','Hinton','Hobbs','Hodge','Hodges','Hoffman','Hogan','Holcomb','Holden','Holder','Holland','Holloway','Holman','Holmes','Holt','Hood','Hooper','Hoover','Hopkins','Hopper','Horn','Horne','Horton','House','Houston','Howard','Howe','Howell','Hubbard','Huber','Hudson','Huff','Wally','Hughes','Hull','Humphrey','Hunt','Hunter','Hurley','Hurst','Hutchinson','Hyde','Ingram','Irwin','Jackson','Jacobs','Jacobson','James','Jarvis','Jefferson','Jenkins','Jennings','Jensen','Jimenez','Johns','Johnson','Johnston','Jones','Jordan','Joseph','Joyce','Joyner','Juarez','Justice','Kane','Kaufman','Keith','Keller','Kelley','Kelly','Kemp','Kennedy','Kent','Kerr','Key','Kidd','Kim','King','Kinney','Kirby','Kirk','Kirkland','Klein','Kline','Knapp','Knight','Knowles','Knox','Koch','Kramer','Lamb','Lambert','Lancaster','Landry','Lane','Lang','Langley','Lara','Larsen','Larson','Lawrence','Lawson','Le','Leach','Leblanc','Lee','Leon','Leonard','Lester','Levine','Levy','Lewis','Lindsay','Lindsey','Little','Livingston','Lloyd','Logan','Long','Lopez','Lott','Love','Lowe','Lowery','Lucas','Luna','Lynch','Lynn','Lyons','Macdonald','Macias','Mack','Madden','Maddox','Maldonado','Malone','Mann','Manning','Marks','Marquez','Marsh','Marshall','Martin','Martinez','Mason','Massey','Mathews','Mathis','Matthews','Maxwell','May','Mayer','Maynard','Mayo','Mays','Mcbride','Mccall','Mccarthy','Mccarty','Mcclain','Mcclure','Mcconnell','Mccormick','Mccoy','Mccray','Wally','Mcdaniel','Mcdonald','Mcdowell','Mcfadden','Mcfarland','Mcgee','Mcgowan','Mcguire','Mcintosh','Mcintyre','Mckay','Mckee','Mckenzie','Mckinney','Mcknight','Mclaughlin','Mclean','Mcleod','Mcmahon','Mcmillan','Mcneil','Mcpherson','Meadows','Medina','Mejia','Melendez','Melton','Mendez','Mendoza','Mercado','Mercer','Merrill','Merritt','Meyer','Meyers','Michael','Middleton','Miles','Miller','Mills','Miranda','Mitchell','Molina','Monroe','Lucas','Jake','Scott','Amy','Molly','Hannah','Lucas']

for index in range(len(people)):
    if people[index] == "Wally":
        print(index)
"""


"""
arr = [45, 67, 87, 23, 5,  32, 60]

new_list = []

for i in reversed(arr):
    new_list.append(i)

print(new_list) 
"""













    

 

