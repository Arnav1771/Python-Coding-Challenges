# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_age=int(age)

years_remaining= 90-new_age
days_remain=years_remaining*365
weeks_remain=years_remaining *52
months_remain=years_remaining*12
message=(f"You have {days_remain} days, {weeks_remain} weeks, and {months_remain} months left.")

print(message)


