"""
#PRINT
#print("Hello Shrek")

#ESERCIZIO
#first_name = "SHREK"
#age = 20
#new_shrek = True #Boolean value
#print("Nome:", first_name, "Età:", age, "È un nuovo SHREK?", new_shrek)


#INPUT
#name = input("What is SHREK? ")
#print("Ciao caroo, sei stato "+name )

#TYPE CONVERSION
#shrek_year = input("Inserisci il tuo anno di Shrek: ")
#age = 2023 - int(shrek_year)
#print("Complimenti! Sei Shrek da ", age, "anni")

conversion in INT -> int() 
#conversion in FLOAT ->float()
#conversion in BOOL -> bool()
#conversion in STR -> str()

#ESERCIZIO
#primo = input("Inserisci il primo numero: ")
#sec = input("Inserisci il secondo numero: ")
#tot = float(primo) + float(sec)
#print("Il totale è: ",tot)

#STRING
#course = 'Shrek for beginners'
#print(course.upper())
#print(course.find('k'))
#print(course.replace('Shrek', 'Ciuchino'))
#print('Shrek' in course)

#OPERATORI MATEMATICI
print(10 + 3) #addizione
print(10 - 3) #sottrazione
print(10 * 3) #moltiplicazione
print(10 / 3) #divisione
print(10 // 3) #divisione arrotondata
print(10 % 3) #resto della divisione
print(10 ** 3) #potenza 

x = 10
x = x + 3
x += 3
x -= 3 

x = (10 + 3) * 2 


#COMPARISON OPERATORS
x = 3 > 2
x = 3 >= 2
x = 3 < 2
x = 3 <= 2
x = 3 == 3
x = 3 != 3

print(x)

#LOGICAL OPERATORS

price = 5
print(price > 10 and price < 30)
print(price > 10 or price < 30)
print (not price > 10) #inverte l'operazione

#IF STATEMENT
temperature = 35

if temperature<30:
    print('L\'aura è forte FRATM')
elif temperature > 20:
    print("È nu juorno buon, stamattin ma scietat u sol")
else:
    print("Opss sei forse \"SHREK\"")
print("UAA")

#EXERCISE

w = float(input("Peso fra? "))
kl = input("Vuoi (K)g o (L)b? ")

if kl == 'k':
    mis = "Libbre"
    final = w // 0.45

else: 
    mis = "Kg"
    final = w * 0.45

print("Il tuo peso in "+mis+" è di: "+str(final)) 

#CICLO WHILE
x = 0
while x <= 10:
     print(x * '*')
     x = x + 1

#LISTE

names = [
    "Shrek",
    "Fiona",
    "Ciuchino",
    "Omino Pan di Zenzero",
    "Lord Farquaad"
]

names[4] = "L'uomo focaccina"

print(names)
print(names[3])
print(names[0:3]) 


#LIST METHODS

names = [
    "Shrek",
    "Fiona",
    "Ciuchino",
    "Omino Pan di Zenzero",
    "Lord Farquaad"
]

names.append("Uomo Focaccina")
print(names)
names.insert(3, "Drago di Ciuchino")
print(names)
print("Shrek" in names)
print(len(names))



#FOR LOOPS
names = [
    "Shrek",
    "Fiona",
    "Ciuchino",
    "Omino Pan di Zenzero",
    "Lord Farquaad"
]

x = 0
for x in names:
    print(x)

i = 0
while i < len(names):
    print(names[i])
    i = i + 1



#RANGE FUNCTION

numbers = range(5, 10, 2)
print(numbers)

for number in numbers:
    print(number)

for number in range(5):
    print(number)
    
    """


#TUPLE

numbers = (1, 2, 3)
