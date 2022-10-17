phy = int(input("Enter your Physics Marks:"))
chem = int(input("Enter your Chemistry Marks:"))
math = int(input("Enter your Mathematics Marks:"))
eng = int(input("Enter your English Marks:"))
hin= int(input("Enter your Hindi Marks:"))

total = phy+chem+math+eng+hin

per = (total/500)*100
print(per,"%")
if per >= 90 and per <= 100:
    print("Your Grade is A+")
elif per < 90:
    print("Your Grade is B.")    
