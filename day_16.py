# Maths case
x = int(input("Enter the number"))
match x:
    case 0 :
         print("it's 0")
    case 9 :
        print("it's 9")
    case 11 :
        print("it's 11")
    case _ if x!=80:
        print("it's not 80")
    case _ if x!=90:
            print("it's not 90")  
    case _ :
            print(x)