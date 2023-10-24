import sys

print("Command line input file name: ",sys.argv[0])
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
s = n1+n2
print("Command Line Input Sum : ",s)

name = input("what is Your Name ? : ")

print("Hemlo, "+name+"\nIt's a pleasure to meet you <3")

print("::::::::Swap Numbers:::::")
a = int(input("a: "))
b = int(input("b: "))

a = a+b
b = a-b
a = a-b

print("a: ",a)
print("b: ",b)
