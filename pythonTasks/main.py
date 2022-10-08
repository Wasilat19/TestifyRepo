
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

print("functions\n")


def greet():
    print("Hello World from Python")


def goodbye():
    print("Thank you")
    print("Goodbye")    

def validate_username():
    pass


greet()
goodbye()
validate_username()


hello = lambda: print("Hello World Anonymously")    
hello()
    