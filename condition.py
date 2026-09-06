# maths = 40
# physics = 20
# chemistry = 36


# if ((maths >= 35 and physics >= 35) or
#     (maths >= 35 and chemistry >= 35) or
#     (physics >= 35 and chemistry >= 35)):
#     print("Pass")
# count=0
# if maths>=35 :
#     count+=1
#     print("pass",count)

# elif physics>=35:
#     count+=1
#     print("pass",count)
# elif chemistry>=35:
#     count+=1
#     print("pass",count)

# else:
#     print("fail")

# print(count)

# d="gnaneshwar"

## lopping:----------------------------------------------




# n="python"
# for i in n:
#     print(i)


# n={"python":20,10:20}
# for i in n:
#     print(n[i])


# python
# n={"python":20,10:20}
# for i in n:
#     print(i)


# 0-5
# n=5
# for i in range(0,n+1,1):
#     print(i)

# for even nums
# n=10
# for i in range(0,n+1,2):
#     print(i)


# 10-0
# n=10
# for i in range(n,0,-1):
#     print(i)

# n="python"
# for i in n[::-1]:
#     print(i)

# n="hello python"
# for i in n:
#     if i in "aeiouAEIOU":
#         print(i)


# print even value:
# l=[10,20,33,55]
# for i in l:
#     if i%2==0:
#      print(i)

# t=(20,304,57,99,77)
# count=0
# for i in t:
#     if i%2!=0:
#         count+=1
# # print(i)
# print(count)

# 5th table:
# t=5
# for i in range(1,11):
#     print(f'{t} x {i} = {t*i}')

# outpiut:
# # 5 x 1 = 5
# # 5 x 2 = 10
# # 5 x 3 = 15
# # 5 x 4 = 20
# # 5 x 5 = 25
# # 5 x 6 = 30
# # 5 x 7 = 35
# # 5 x 8 = 40
# # 5 x 9 = 45
# # 5 x 10 = 50


# practice:-------------------------------------
## 1
# n="gnaneshwar"
# for i in n:
#     print(i)

## 2
# n="sia ram"
# for i in n:
#     print(i)

## 3
# n=("python",1,2,4.4)
# for i in n:
#     print(i)

## 4
# n=("raji",8309914235,"age",22)
# for i in n:
#     print(i)

## 5
# n=100
# for i in range(0,n+1,5):
#         print(i)

## 6
# i=1684
# for i in range(0,i+1,100):
#     if i%5==0:
#      print(i)


## 7
# n={"python":10,10:20}
# for i in n:
#     print(i)           #keys only takes values does not takes


## 8
# n=88
# for i in range(0,n+1,2*2):
#     print(i)

## 9
# n=50
# for i in range(20,n+1):
#     if i%2==0:
#      print(i)


## 10
# word="hello python"
# for i in word:
#     if i in "aeiouAEIOU":
#         print(i)

## 11
# word="python is a programming language"
# count=0
# for i in word:
#     if i in "aeiouAEIOU":
#         count+=1
#         print(i)
# print(count)


## 12
# list=[10,20,33,55]
# for i in list:
#     if i%2==0:


##13
# list=[78,99,12,56,89,12,56,57,86,69,32,35.16]
# for i in list:
#     if i%2==0:
#         print(i)

## 14
# n=10
# for i in range(1,n+1):
#     print(f'{n} X {i} = {n*i}')

# n=5
# for i in range(1,10+1):
#     print(f"{n} x {i} = {n*i}")

# n=6
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")


# n=88
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Interview-Style Programming Questions: Loops, Strings, and Number Operations
# 1. Print Numbers from 1 to n
# Question: Write a program to print numbers from 1 to n. Explanation:
#  Use a loop starting from 1 to n and print each number. - Input: n = 5 - Output: 1 2 3 4 5

# n=5
# for i in range(1,n+1,1):
#     print(i)


# m=100
# n=159
# for i in range(m,n+1):
#     if i%4==0:
#         print(i)

# n=5
# for i in range(1,n+1):
#     res=1
#     for j in range(1,n+2):
#         res+=1
#     print(res)

# 2. Print Numbers from m to n
# Question: Write a program to print numbers from m to n. Explanation: 
# Loop from m to n and print values. - Input: m = 3, n = 7 - Output: 3 4 5 6 7

# m=3
# n=7
# for i in range(m,n+1,1):
#     print(i)


# 3. Print Numbers from n to 1 in Reverse
# Question: Write a program to print numbers in reverse from n to 1. Explanation: 
# Use a loop starting from n and decrement to 1. - Input: n = 5 - Output: 5 4 3 2 1

# n=5
# for i in range(n,1-1,-1):/
#     print(i)


# 4. Print Numbers from n to m in Reverse
# Question: Write a program to print numbers from n to m in reverse. Explanation: 
# Start from n and go down to m. - Input: n = 10, m = 6 - Output: 10 9 8 7 6

# n=10
# m=6
# for i in range(n,m-1,-1):
#     print(i)


# 5. Sum of n Natural Numbers
# Question: Write a program to calculate the sum of first n natural numbers. Explanation:
#  Use formula or loop to sum from 1 to n. - Input: n = 5 - Output: 15

# n=5
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print(sum)

# 6. Factorial of a Number
# Question: Write a program to find the factorial of a number. 
# Explanation: Multiply all numbers from 1 to n. - Input: n = 5 - Output: 120

# n=5
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
# print(factorial)

# n=15
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# 7. Sum of m to n Numbers
# Question: Write a program to find the sum of all numbers from m to n. Explanation: 
# Loop from m to n and add values. - Input: m = 3, n = 6 - Output: 18

# m=3
# n=6
# total=0
# for i in range(m,n+1):
#     total+=i
# print(total)

# n=65
# total=0
# for i in range(1,n+1):
#     total+=i
# print(total)

# n=15
# sum=0
# for i in range(1,n+1):
#     sum += i
# print(sum)


# 8. Product of m to n Numbers
# Question: Write a program to find the product of numbers from m to n. Explanation: 
# Loop from m to n and multiply values. - Input: m = 2, n = 4 - Output: 24

# m=2
# n=4
# product=1
# for i in range(m,n+1):
#     product*=i
# print(product)


# 9. Print Factors of a Number
# Question: Write a program to print all factors of a given number. 
# Explanation: Check divisibility of number from 1 to n. - Input: n = 6 - Output: 1 2 3 6

# n=6
# fact=0
# for i in range(1,n+1):
#     if n%i==0:
#      fact+=1
#      print(i)
# print(fact)


# 10. Count of Factors
# Question: Write a program to count how many factors a number has. Explanation: 
# Increment count when divisible. - Input: n = 6 - Output: 4

# n=6
# count=0
# for i in range(1,n+1):
#    if n%i==0:
#       count+=1
# print(count)



# 11. Prime Number Check
# Question: Check if a number is prime. Explanation: 
# A number is prime if it has exactly 2 factors. - Input: n = 7 - Output: Prime

# n=7
# prime=0
# for i in range(1,n+1):
#     if n%i!=2 or n%i!=3:
#         prime+=1
# print(i)


# 12. Even Numbers from m to n
# Question: Print all even numbers between m and n. Explanation: 
# Use loop and check if divisible by 2. - Input: m = 3, n = 10 - Output: 4 6 8 10

# m=3
# n=10
# for i in range(m,n+1):
#     if i%2==0:
#         print(i)


# 13. Odd Numbers from m to n
# Question: Print all odd numbers between m and n. Explanation: 
# Check if number % 2 != 0. - Input: m = 3, n = 10 - Output: 3 5 7 9

# m=3
# n=10
# for i in range(m,n+1):
#     if i%2!=0:
#         print(i)

# 14. Count of Even and Odd Numbers
# Question: Count how many even and odd numbers are in the range m to n. Explanation:
# Use counters for even and odd. - Input: m = 3, n = 7 - Output: Even = 2, Odd = 3

# m=3
# n=7
# count=1
# for i in range(m,n+1):
#     if i%2==0:
#         count+=1
#         if i%2!=0:
#                 count+=1
#                 print(count,"odd")
#         print(count,"even")



# 15. Reverse a String
# Question: Reverse a given string. Explanation: 
# Use slicing or loop. - Input: “hello” - Output: “olleh”

# s="hello"
# for i in s:
#     if i==s[::-1]:
#         print(i)
#     print()

# 16. Check for Palindrome String
# Question: Check if a string is a palindrome. Explanation: 
# Compare string with its reverse. - Input: “madam” - Output: Palindrome

# s="madam"
# for i in s:
#    if s == s[::-1]:
#       res="palindrom"
# print(res)
      
    

# 17. Sum of Digits
# Question: Calculate the sum of digits of a number. Explanation: 
# Use loop and % 10 to extract digits. - Input: 123 - Output: 6

   


# ________________________________________
# 18. Product of Digits
# Question: Calculate the product of digits. Explanation: 
# Multiply digits extracted from number. - Input: 123 - Output: 6

# n=123
# product=1
# for i in n:
#     product=product*i
#     print(product)


# ________________________________________
# 19. Armstrong Number Check
# Question: Check if a number is an Armstrong number. Explanation: 
# Sum of cube of digits equals the number. - Input: 153 - Output: Armstrong number

# num=153
# sum=1
# for i in num:
#     sum+=sum*i
#     print(sum)


# ________________________________________
# 20. Reverse a Number
# Question: Reverse the digits of a number. Explanation: 
# Use loop with % and // to reverse. - Input: 123 - Output: 321




# ________________________________________
# 21. Palindrome Number Check
# Question: Check if a number is a palindrome. Explanation: 
# Compare number with its reverse. - Input: 121 - Output: Palindrome

# n=121
# n=str(n)
# for i in n:
#     if n[::-1]==n:
#        res="palindrome"
# print(res)

# ________________________________________
# 22. Count Vowels in String
# Question: Count number of vowels in a string. Explanation: 
# Loop and check for a, e, i, o, u. - Input: “apple” - Output: 2

# w="apple"
# count=0
# for i in w:
#     if i in "aeiouAEIOU":
#         count+=1
# print(count)

# ________________________________________
# 23. Count Consonants in String
# Question: Count consonants in a string. Explanation: 
# Check for alphabetic characters not vowels. - Input: “apple” - Output: 3

# word="apple"
# count=0
# for i in word:
#     if i not in "aeiouAEOIU":
#         count+=1
# print(count)

# ________________________________________
# 24. Count Vowels and Consonants
# Question: Count vowels and consonants in input string. Explanation: 
# Maintain two counters. - Input: “apple” - Output: Vowels = 2, Consonants = 3

# word="apple"
# v_count=0
# c_count=0
# for i in word:
#     if i in "aeiouAEIOU":
#         v_count+=1
#     else:
#         c_count+=1
# print(v_count)
# print(c_count)

# ________________________________________
# 25. Perfect Number Check
# Question: Check if a number is perfect. Explanation: 
# Sum of proper divisors equals the number. - Input: 28 - Output: Perfect number



# ________________________________________
# 26. Neon Number Check
# Question: Check if a number is a neon number. Explanation: Square the number, sum digits, match original. - Input: 9 - Output: Neon number
# ________________________________________
# 27. Strong Number Check
# Question: Check if a number is a strong number. Explanation: Sum of factorial of digits equals the number. - Input: 145 - Output: Strong number
# ________________________________________
# 28. Harshad Number Check
# Question: Check if a number is divisible by the sum of its digits. 
# Explanation: Calculate digit sum and check divisibility. - Input: 18 - Output: Harshad number
# ________________________________________
# 29. Fibonacci Series
# Question: Print the Fibonacci series up to n terms. Explanation: Start with 0, 1 and continue with sum of last two. - Input: n = 5 - Output: 0 1 1 2 3
# ________________________________________
# 30. Check for Neon Number (Repeated)
# Question: Again, check for a neon number (example). Explanation: Square number and sum digits. - Input: 9 - Output: Neon number



# word="hello PYThon"
# for i in word:
#     if "A"<=i<="Z":
#         print(i)


# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# n=10
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# print(count)


# n=50
# count=0
# for i in range(1,n+1):
#     if n%i!=0:
#         count+=1
#     print(count)


# n=10
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"{i} x {j}={i*j}")


# # even tables:
# n=10
# for i in range(0,n+1,2):
#    for j in range(1,11):
#     print(f"{i} x {j} = {i*j}")

# print()


# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()


# n=3
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()


# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(" ",end="* ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# ========================================================================================================================================

# a=20
# b=20.67
# c=a+b
# print(c) 
# print(type(c))


# # conversions:
# int()
# float()
# complex()
# bool()
# set()
# tuple()
# set()
# dict()


# a=10.3+2j
# print(b)
# print(type(b))


# b=int(a)
# print(b)

# a=True
# b=float(a)
# print(b)
# print(type(b))


# a=True
# b=str(a)
# print(b)
# print(type(b))

# a=True
# b=list(a)
# print(b)
# print(type(b))                  #TypeError: 'bool' object is not iterable



# a="hello"
# b=list(a)
# print(b)                    #['h', 'e', 'l', 'l', 'o']


# b=dict(a)
# print(b)



# =========================================================================================
# 09/07/26

# n=2
# while n<=10:
#     print(n)
#     n+=2

# n=4
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {n * i}")
#     i += 1


## 1-5th table

# i=1
# while i<=5:
#    j=1
#    while j<=10:
#       print(f"{i}x{j}={i*j}")
#       j+=1
#    print()
#    i+=1
   
# # 1-10th table
# i=1
# while i<=10:
#    j=1
#    while j<=10:
#       print(f"{i}x{j}={i*j}")
#       j+=1
#    print()
#    i+=1

# n=2
# i=0
# while i<=10: 
#    print(f"{n}x{i}={n*i}")
#    i+=1

# # 1 2 3 
# # 1 2 3 
# # 1 2 3

# n=1
# while n<=3:
#    i=1
#    while i<=3:
#       print(i,end=" ")
#       i+=1
#    print()
#    n+=1


# i=1
# while i<=4:
#    j=1
#    while i<=1:
#       print(j,end=" ")
#       j+=1
#    print()
#    i+=1

# table=1
# while table<=3:
#     value=1
#     while value<=10:
#         print(f"{table}x{value}={table*value}")
#     value+=1
# print()
# table+=1


# l=[[10,20,30],
#    [40,20,50],
#    [10,20,10]]
# for i in l:
#     sum=0
#     for value in i:
#         sum+=value
#     print(sum)


# l = [
#     [10,20,15],
#     [8, 9, 10],
#     [6, 5, 8]
# ]

# product = 1
# for row in l:
#     for item in row:
#        product*= item
# print( product)

# for i in l:
#     sum=0
#     for value in i:
#         sum+=value
#     print(sum)

# for i in l:
#     product=1
#     for value in i:
#         product*=product
#     print(product)


# sum=0
# for i in l:
#     sum+=l
# print(sum)


# num=[10,20,30]
# sum=0
# for i in num:
#     sum+=1
# print("Sum =", sum(num))



# num=[10,20,30]
# product=1
# for i in num:
#     product=product*i
# print(product)



# factorial
# n=5
# fact=1
# count=0
# for i in range(1,6):
#    fact=fact*i
#    count+=1
#    print(count)
# print(fact)



# n=[10,8,9,7,5,6]
# evn_count=0
# odd_count=0
# for i in n:
#     if i%2==0:
#         evn_count+=1
#     else: odd_count+=1  
# print(evn_count)
# print(odd_count)


# l=[
#    [10,16,9],
#    [15,89,21],
#    [65,32,48]
#    ]

# for i in l:
#     product=1
#     for value in i:
#       product*i=product
# print(product)


# for i in l:
#     product=1
#     for value in i:
#         product=product*i
#     print(product)

