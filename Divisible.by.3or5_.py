#is the number divisible by 3 or 5 
#if, elif, elif, else 



usernum = input('Please input an integer:')
usernum = int(usernum)

if usernum % 3 == 0 and usernum % 5 == 0 :
    print ('Divisible by 3 and 5' )

elif usernum % 3 == 0 :
    print ("Divisible by 3")

elif usernum % 5 == 0 :
    print ("Divisible by 5")

else :
    print ("The integer is not Divisible by 3 or 5")