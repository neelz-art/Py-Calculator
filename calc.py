i=1
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
while i==1:
    print("\n\nChoices \n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division\n 5.Exit\n ")
    c=int(input("Enter your choice: "))
    if c==1:
        print("\nsum=",n1+n2)
    elif c==2:
        print("\nsubstract=",n1-n2)
    elif c==3:
        print("\nmultiplication=",n1*n2)
    elif c==4:
        print("\ndivision=",n1/n2)
    elif c==5:
        break
    else:
        print("\nEnter valid choice!")
    
