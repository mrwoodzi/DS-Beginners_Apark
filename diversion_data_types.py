#these examples were from progamiz.com but I added my own personalization
s = 'Hello World!'
print("\n\t\tTuples!")
print("\tTuples exist inside ( , , , )")                          # Tuples
print("\tThey can be nested.")
print("\tNested items can be modified.")
print("\tTuples are immutable.")
print("\tThey are generally used when the types of data are different, heterogeneous.")
print("\tHello World!")

print("\ts[4] = ", s[4])

print("\ts[6:11] = ", s[6:11])
                                                 # Sets
a = {5, 2, 3, 1, 4}

print("\n\t\tSets!")
print("\tSets exist inside { , , ,}")
print("\ta = ", a)

print("\t",type(a))#prints data type of variable "a"
                                               # String
print("\n\t\tStrings!")
print('''\tStrings are made with ' or \" \n\tand contain Unicode characters''')
print("\tYou can concatenate a string with a function.")
print("\tMake it look something like below.")
function = """\t(f"....curly brackets } will bracket the function....)"""
print(f"{function}")
print("The line above is a function.")
my_string = '\tHello'
print(my_string)

my_string = "\tHello"
print(my_string)

my_string = '''\tHello'''
print(my_string)

my_string = """\tHello! Welcome to
\tthe world of Python!!!"""
print(my_string)
#When I started writing this I go confused and did the totally wrong thing FAIL I was orginally writing about list and got the webpage mixed up
print("\n\t\tNumbers!")
print("\tNumbers exist inside ()")
print("\tNumbers can be any length, you can have floats up to 15 decimals,")
print("\tand even complex nubmers. ;) ")
print("\tVariables can even be truncated! Wait??!! What does that mean?")
b = 123456789
c = 0.1234567890123456789 # it didn't print numbers that already exsited
d = 1 + 2j
print("\t", b)
print("\t", c)
print("\t", d)
print("\tThe second number is truncated, still trying to get a clear \n\tunderstanding of that.")
print("\tLook CLOSER.")
print("\tThe original value of the second item is,")
print("\t0.01234567890123456789.")

print("\n\t\tLists!")
print("\tThey exist in these [, , , ]")
print("\tThey are mutable.")
