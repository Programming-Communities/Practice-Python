# print("aamir")

Name : str = "MALIK Aamir shazadah "
# print(Name.upper())
# print(Name.upper())
# print(Name.capitalize())
# print(Name.casefold())
# Da sa simple example
# print(Name.center(10))  # "  Aamir   "

# # Da da "-" na di pad kolo example
# print(Name.center(10, '-'))  # "--Aamir---"

# print(Name.)



print(Name.upper())      # "AAMIR"
print(Name.lower())      # "aamir"
print(Name.capitalize()) # "Aamir"
print(Name.casefold())   # "aamir"

# Center the string
print(Name.center(10))         # "  Aamir   "
print(Name.center(10, '-'))    # "--Aamir---"

# Other string methods
print(Name.count('a'))         # 2
print(Name.find('m'))          # 2
print(Name.replace('A', 'O'))  # "Oamir"
print(Name.strip())            # "Aamir"
print(Name.split(' '))         # ['Aamir']
print(Name.startswith('Aa'))   # True
print(Name.endswith('r'))      # True
print(Name.isalpha())          # True
print(Name.isdigit())          # False
print(Name.isalnum())          # True
print(Name.islower())          # False
print(Name.isupper())          # False
print(Name.title())            # "Aamir"
