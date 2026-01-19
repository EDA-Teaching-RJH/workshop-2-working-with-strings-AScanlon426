import math  

def main():
 A = int(input("What is the length of side a?"))
 B = int(input("What is the length of side b?"))
 pythag(A,B)  

def pythag(A,B):
 C = math.sqrt((A**2 + B**2))
 print ("The hypotenuse is", C)

main()
