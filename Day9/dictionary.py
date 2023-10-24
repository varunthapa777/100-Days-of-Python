# Dictionaries : Collection of key value pairs.


#Creating dictionary

my_dictionary = {
  "fruit" : "Apple",
  "Vegies": "Tomato",
  "budget" : 2000,
  "greet" : "Hello! This is Varun",
}

#Access Values

#print entire dict
print("My Dictionary :",my_dictionary)

#print single item
print("Greet:",my_dictionary["greet"])

#Adding new item
my_dictionary["hobby"] = "Coding"

#Create Empty Dictionary

empty_dict = {}
print("Empty Dict: ",empty_dict)

#Edit on item Dictionary
my_dictionary["fruit"] = "Mango"
print("Fruit:",my_dictionary["fruit"])

#Loop through Dictionary
print("My Dictiory Key values:\n")
for key in my_dictionary:
  print(key,":",my_dictionary[key])