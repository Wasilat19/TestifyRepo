
# integer

# number1 = 12345
# number2 = 12365
# long_number = 1233445668767567461256472848475689057

# print(type(number1))   # <... int>
# print(type(number2))   # <... int>
# print(type(long_number))   # <... int>

# floating-point numbers

# float1 = 12.55
# float2 = 12.     # 12.0
# float3 = .34     # 0.34
# float4 = 12e7

# print(type(float1))
# print(type(float2))
# print(type(float3))
# print(type(float4))


# complex number

# complex_num = 2+1j

# print(type(complex_num))

# string

# testify = 'Testify'
# language = 'Python'

# print(type(testify))
# print(type(language))

# boolean

# is_java = False
# is_python = True

# print(type(is_java))
# print(type(is_python))


# name = 12         # int
# print(type(name))

# name = "testify"  # str
# print(type(name))

# name = False      # bool
# print(type(name))

# Escape sequence

article = "This is an article\na multiline article\n\tEach text.\b"
#print(article)

article = r"This is an article\na multiline article\n\tEach text.\b"

# concatenation

group = "wood"
attr = "peckers"
bird = group + attr

#print(bird)

# conditional statements

#if statement
#number = 5
#if number == 5:
    #print("Number is 5")

#if_else
#if 5 == 1:
    #print("5 is equal to 1")
#else:
    #print("5 is not eual to 1")

#elif
#if number == 1:
    #print("5 == 1")
#elif number == 3:
    #print("5 == 3")
#elif number == 5:
    #print("Number is 5")    
#elif number == 6:
    #print("Number is 6")    


# functions

#print("functions\n")


#def greet():
    #print("Hello World from Python")


#def goodbye():
    #print("Thank you")
    #print("Goodbye")    

#def validate_username():
    #pass


#greet()
#goodbye()
#validate_username()


#hello = lambda: print("Hello World Anonymously")    
#hello()
    

#Basic string operations

#name = "testify for testing and automation school, with testify"

# len => to get the size of a string
#size = len(name)
#print("size:", size)

# upper => converts a string to upper case
#upper_value = name.upper()
#print("upper:", upper_value)

# lower => converts a string to lower case
#lower_value = name.lower()
#print("lower:", lower_value)

# capitalize => converts the first character to upper case
#capitalzed_value = name.capitalize()
#print("capitalized:", capitalzed_value)

# count => counts the occurence of a value in a string
#testify_count = name.count("testify")
#print("testify count:", testify_count)

#t_count = name.count("t")
#print("t count:", t_count)

# find => get the position of a value in the string, if the value is not in the string it returns -1
#for_position = name.find("for")
#print ("for position:", for_position)

# index => get the position of a value in the string, if the value is not in the string it throws an exception
#for_index = name.index("for")
#print("for index:", for_index)


# Basic List Operations
#languages = ["python", "java", "C#"]
#print("list:", languages)

# append -> add new item at the end of a list
#languages.append("javascript")
#print("append:", languages)

# insert -> add new item at any position ina list
#languages.insert(0, "c")
#languages.insert(2, "php")
#print("insert:", languages)

# pop -> remove an item from the specified position
#languages.pop(0)
#languages.pop()
#print("pop:", languages)

# remove -> remove an by value
#languages.remove("php")
#print("remove:", languages)

#count -> returns the number of occurrence of an item in a list
#languages.append("java")
#count_java = languages.count("java")
#print('list:', languages)
#print("count:", count_java)

# clear -> deletes all items from a list
#languages.clear()
#length = len(languages)
#print("clear:", languages,length)

#languages = ["python", "java", "C#"]
# copy -> returns a copy of a list
#languages_copy = languages.copy()
#print("copy:", languages_copy)

# reverse -> reverses the order of a list
#before_reverse = languages.copy()
#languages.reverse()
#print("before reverse:", before_reverse, " after reverse:", languages)

#languages = ["python", "java", "C#", "smalltalk", "ruby"]
# sort -> sort the items in the list by values in ascending or descending order
#languages.sort()
#print("sort-asc:", languages)
#languages.sort(reverse=True)
#print("sort-decs:", languages)

# extend -> add the content of the specified list to the current list
#languages.extend(["visual basic", "brainfuck", "ring", "sql", "powershell"])
#print("extend:", languages)


# Basic Dictionary Operations

#animals = {
 #   "bird": "Parrot",
  #  "mammal": "Cow",
   # "fish": "Titus"
#}
#print("dictionary:", animals)

# get -> fetch a value using specifid key
#bird = animals.get("bird")
#print("get-1:", bird)
#mammal = animals.get("mammal")
#print("get-2:", mammal)

# items ->list of the dictionary key-value pair
#animals_items = animals.items()
#print("items:", animals_items)

# key -> return the keys as a list
#animals_keys = animals.keys()
#print("keys:", animals_keys)

# values -> return the values as a list
#animals_values = animals.values()
#print("values:", animals_values)

# pop -> remove a key-value pair using a specified key
#animals.pop("mammal")
#print("pop:", animals)

# update -> add more key-value pairs into a dictionary
#animals.update({"mammal": "Goat"})
#animals.update({"insect": "ant", "reptile": "snake"})
#print("update:", animals)

# popitem -> remove the last key-value pair from the dictionary
#animals.popitem()
#print("popitem:", animals)

# copy -> return a copy of a dictionary
#copied_animals = animals.copy()
#print("copy:", copied_animals)

# clear -> removes all the elements, items, key-value pairs from the dictionary
#animals.clear()
#print("clear:", animals)



# OOP
# Class

class Animal:     # Class

    name = "cow"      # Attribute
    group = "Mammal"   # Attribute

    def get_name_group(self):                  # Method
        return self.name + ":" + self.group        

#object
cow = Animal()
print(cow.name, cow.group, cow.get_name_group()) 



# Attributes

class Animal:

    group = "Mammal"        # group is a class variable
    can_walk = True

    def __init__(self, name):
        self.name = name           # name is an instance variable

cat = Animal("Cat")
dog = Animal("Dog") 

print(cat.name)
print(dog.name)