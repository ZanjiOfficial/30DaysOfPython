import math
name = "Jakob"
last_name = "Jensen"
country = "Denmark"

#Day 1 of 30 days of Python Challenge
print (2+2)
print (10-8)
print (2*9)
print (8%3)
print (42/2)
print (5**2)
print (20//6)

#family stuff
print ("name")
print ("last_name")
print ("country")
print ("I'm doing 30 days of Python challenge")


#types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabenet','Python','Finland']))
print(type("name"))
print(type("last_name"))
print(type("country"))

#examples of types, and finding Euclidean distance
#string
name = "Jakob"
#boolean
Earth_is_flat = False
#float
gravity = 9.81
#list
fruits = ['banana', 'orange', 'mango', 'lemon']
#dictionary
{"name": "Jakob", "age": 30, "country": "Denmark", "is_married": False}
#tuple
coordinates = (4, 5)
#set
unique_numbers = {1, 2, 3, 4, 5}

#Euclidean distance between (2.3) and (10.8)
p1=2
p2=3
q1=10
q2=8

dx = q1 - p1
dy = q2 - p2
distance = math.sqrt(dx**2 + dy**2)

print("Euclidean distance between (2,3) and (10,8) is: ", distance)

