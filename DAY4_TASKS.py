
# Taking user name and age as input and printing in form of f strings

name=input("enter user name:")
age=int(input("enter user age:"))

print(f"{name} age is {age}")


# membership operator 

list=[1,2,3,4,5,6,7,8,9,10]

print(5 in list)  # checking if 5 is present in the list sequence or not

print(15 not in list) # checkung 15 is not present in the list or not  


# dictionary

dict={"Product":"AC","price":20000,"company":"samsung"}

print(dict)

print(f"The product i am using is {dict["company"]} company {dict["Product"]} which worth around {dict["price"]}")


