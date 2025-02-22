print("Welcome to the tip calculator")
total_bill=float(input("What was the total bill :"))
       # float is added because to get float number 1.202
per_astip=int(input("How much tip would like to give?:"))
split_bill=int(input("How many people would like to split the bill:"))
tb_tip=((total_bill+per_astip)/split_bill)
    # here the round(tb_tip,2) this gives decimal points upto 2
    #or the "{:.2f}".format(which ever you what)
print("your share is:",tb_tip)
# tb=(f"your share is:{tb_tip}")
# print(tb)




# print("What was the total bill:",total_bill)
# print("How much tip would like to given:",split_bill)
# print("How many people would like to split the bill:",tb_tip)

