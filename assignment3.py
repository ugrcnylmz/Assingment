number=int(input("Please enter number : "))
if sayi > 1:
   
   for i in range(2,number):
       if (number % i) == 0:
           print(sayi," is not a prime number.")
           break
   else:
       print(number," is a prime number.")
 
else:
   print(number," is not a prime number.")