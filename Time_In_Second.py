Days=int(input("Enter Days:"))*3600*24 #To input day and convert it into second (day*3600*24)
Hours=int(input("Enter Hour:"))*3600 # To input hour and convert it into second
Minutes=int(input("Enter minute"))*60 #To input minute and convert into second
Second=int(input("Enter second")) #To input second
Time=Days+Hours+Minutes+Second
print("Total second=",Time)

