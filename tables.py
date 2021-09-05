n=int(input("Till what number would you like to print the multiplication tables")) #say if input is 10 then 0 to 10 tables will be printed
for i in range(n+1):       #since range would only consider to n-1 values I have given n+1 to get input n
    print("Multiplication table for",i)
    for j in range(1,11):   #printing multiplication values from 1 to 10 range(1,11)---is 1,2,3,4,5,6,7,8,9,10
        print(i,"x",j,"=",i*j)
    print("\n")           # new line added to separate each multiplication table
    