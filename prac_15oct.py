# a=int(input())
# if a%2==0:
#     print("Its a Even no.")
# else:
#     print("ITS a Odd no.")    



sal=int(input("Enter Your salary:"))
timespnt=int(input("Enter Your Timespent in company:"))
if timespnt>=10:
    print("Your salary:", sal+ sal/10)
elif timespnt>=6 and timespnt<10:
    print("Your salary:", sal+ sal*8/100)    
elif timespnt<6:
    print("Your salary:", sal+ sal*5/100)       
else:
    print("Enter a valid no. again", sal)    