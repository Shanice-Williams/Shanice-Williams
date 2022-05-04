#Author: Shanice Williams
#Date Created: May 2, 2022
#Course: ITT103
#Purpose: This program is to calculate the commission that was received by a salesperson. The rate of the commission is based on the sales amount and class.

salesperson = ''
while salesperson!= 'noname':

    salespersonnum = int(input("Please enter the salesperson number: "))
    salesamount = int(input("Enter the sales amount:"))
    Class = int(input("Enter the class:"))


    if Class==1:
        if salesamount <= 1000:
            commrate = 0.06
            commission= commrate * salesamount
            print("The Total commission for",salespersonnum, "is",commission)
            
        elif salesamount > 1000 < 2000:
            commrate= 0.07
            commission=commrate * salesamount
            print("The Total commission for",salespersonnum, "is",commission)
                    
        elif salesamount >=2000:
            commrate= 0.1
            commission=commrate * salesamount
            print("The Total commission for",salespersonnum, "is",commission)

    elif Class==2:
        if salesamount<1000:
            commrate=0.04
            commission= commrate * salesamount
            print("The Total commission for",salespersonnum, "is",commission)
                  
        elif salesamount >=1000:
             commrate=0.06
             commission=commrate * salesamount
             print("The Total commission for",salespersonnum, "is",commission)
                      
    elif Class==3:
            
                commrate=0.045
                commission= commrate * salesamount
                print("The Total commission for",salespersonnum, "is",commission)
    else:
        print("class and sales amount not found")

    stop=input("Do you wish to end the porgram? If so type Yes: ")

    if stop=="Yes":
        break






    
