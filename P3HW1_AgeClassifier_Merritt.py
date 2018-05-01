# CTI-110 
# P3HW1 - Age Classifier 
# Marcus Merritt
# 4/30/2018
#

age = int(input("Please enter a person's age."))

if age <= 1:
    print("You are an infant.")

elif age > 1 and age < 13:
    print("You are a child")

elif age >= 13 and age < 20:
    print("You are a teenager.")

else:
    print("You are an adult.")
