#these examples were from progamiz.com but I added my own personalization
nest = []
s = 'Hello World!'###################################### # Tuples
print("\n\t\tTuples!")
print("\tTuples are immutable.")
print("\tTuples exist inside  parenthesis ( , , , )")        
print(f"\tThey can be nested with {nest}.")
print("\tNested items can be modified.")

print("\tThey are generally used when the types of data are different, heterogeneous.")
print("\tHello World!")

print("\ts[4] = ", s[4])

print("\ts[6:11] = ", s[6:11])
############################################################### # Sets
a = {5, 2, 3, 1, 4}

print("\n\t\tSets!")
print("\tSets exist inside { , , ,}")
print("\tSets are unordered.")
print("\ta = ", a) # this put the data set in numerical order
# I tried it a different way and it still put them in numerical order
print("\t",type(a))#prints data type of variable "a"
#####################################################  # String
curly_brackets = {}
print("\n\t\tStrings!")
print('''\tStrings are made with ' or \" \n\tand contain Unicode characters''')
print("\tYou can concatenate a string with a function.")
print("\tMake it look something like below.")
function = f"""\t(f"....curly brackets {curly_brackets} will bracket the variable....")"""
print(f"{function}")
print("\tThe line above is a function.")
my_string = '\tHello'
print(my_string)
print(my_string[0:5])
print("\tHell, you can even slice a string!")
print(f"{my_string[0:5]}, you can concatenate and slice at the same time!")
print("""\tThis is what it looks like print(f"{my_string[0:5]}, you can concatenate and slice at the same time!")""")

my_string = "\tHello"
print(my_string)

my_string = '''\tHello'''
print(my_string)

my_string = """\tHello! Welcome to
\tthe world of Python!!!"""
print(my_string)

########################################## # Numbers

#When I started writing this I go confused and did the totally wrong thing 
# FAIL I was orginally writing about list and got the webpage mixed up

print("\n\t\tNumbers!")
print("\tNumbers exist inside ()")
print("\tNumbers can be any length, you can have floats up to 15 decimals,")
print("\tand even complex nubmers. ;) ")
print("\tVariables can even be truncated! Wait??!! What does that mean?")
b = 123456789
c = 0.1234567890123456789 # it didn't print numbers that already exsited
d = 1 + 2j
print("\t", b, "This is an integer.")
print("\t", c, "This is a float.")
print("\t", d, "This is a complex number.")
print("\tThe second number is truncated, still trying to get a clear \n\tunderstanding of that.")
print("\tLook CLOSER.")
print("\tThe original value of the second item is,")
print("\t0.01234567890123456789.")



print("\n\t\tLists!")
print("\tThey exist in these [, , , ]")
print("\tThey are mutable.")
print("\tYou can pull items from lists in or out of order by calling {thing[]}.")
print("\tPy reads the list the same way as a list.")


print("\n\t\tTHE ABOVE DATA TYPES USE INDEXING TO ACCESS VALUES.")


############################################ #Dictionary

print("\n\t\t Dictionarys!")
print("\tDICTIONARYS USE KEYS TO ACCESS VALUES.")
print("\tDictionarys are an unordered pair.")
print("\tDictionaries are optimized to retrieve values when the key is known.")
print('''\tkey/value''')
print(f"\tTo create a dictionary use curly brackets {curly_brackets}.")
print("\tValues can be of any data type and can repeat.")
print("\tKeys must be of an immutable type (string, number or tuple with immutable elements) and must be unique.")
print("\tThere is a built in dict() function which lets you create a dictionary.")
print("\tAfter reading up on dictionaries they may require their own .py file.")