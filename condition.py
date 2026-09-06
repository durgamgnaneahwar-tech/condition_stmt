# condition:
# age=18
# if age>18:
#     print("eligible")
# else:
#     print("not eligible")



#     print("if block end")
# else:
#     print("not eligible")

# signal="green"
# if signal=="red":
#     print("wait")
# else:
#     print("go")

# signal="green"
# if signal=="yellow":
#     print("go")
# else:
#     print("wait")


# signal=input("enter the color: ")
# if signal=="green":
#     print("go")
# elif signal=="orange":
#     print("slow")
# else:
#     print("stop")
# if signal=="red":
#     print("stop")



# grades: a-f
# marks=int(input("enter your marks: "))
# if marks>90:
#     print("grade A")
# if marks>80:
#     print("grade B")
# if marks>60:
#     print("grade C")
# if marks>50:
#     print("grade d")
# if marks>35:
#     print("grade e")
# else:
#     print("grade f")


# grades: a-f
# marks=int(input("enter your marks: "))
# if marks>=90:
#     print("grade A")
# if marks>=80:
#     print("grade B")
# if marks>=60:
#     print("grade C")
# if marks<=50:
#     print("grade d")
# if marks>=35:
#     print("grade e")
# else:
#     print("grade f")

# nested if


# bill=11000
# payment="UPI"
# if bill>10000:
#     discount=(bill*(5/100))
#     bill= bill-discount
#     if payment=="credit card":
#         if card=="HDFC":
#             Card_discount=bill*(5/100)
#             print("final amount: " , bill-price_discount -Card_discount)
#         elif card=="SBI":
#             Card_discount=bill*(3/100)
#             print("final amount: " , bill-price_discount -Card_discount)   
        

#     else:
#         print("final amount", bill-discount )


# bill=55000
# payment="credit card"
# card="ICICI"
# if bill>=50000:
#     price_discount=(bill*(5/100))
#     if payment=="credit card":
#         card_discount= bill*(5/100)
#         print("final amount: " , bill-price_discount-card_discount)
#     if payment=="upi":
#         print("final amount: " , bill-price_discount)


# print("1")

# bill=5600
# payment="debit card"
# card="SBI"
# if bill>=5500:
#     price_discount=(bill*(3.8/100))
#     if payment=="debit card":
#         card_discount=(bill*(2.5/100))
#         print("final amount: " ,bill-price_discount-card_discount)
#     if payment=="UPI":
#         upi_discount=(bill*(2/100))
#         print("final amount: " ,bill-price_discount-upi_discount)
    

bill=11000
payment="hdfc credit card"
if payment=="hdfc credit card":
    discount=bill*(3.5/100)
    print(bill+discount)
else:
    print(bill)








    