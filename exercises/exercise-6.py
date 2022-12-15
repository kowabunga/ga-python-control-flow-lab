# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

month = input("Enter the month as three characters, e.g. Jan, Feb, Aug, Sep > ").lower().strip()

while month not in months:
    month = (
        input("Please make sure you enter a correct month in the following three letter format, e.g. Jan or Mar > ")
        .lower()
        .strip()
    )

day = int(input("Enter the day of the month > "))

while day > 31 or day < 1:
    day = int(input("Months have at least one day and 31 days at most. Please put in a correct date. > "))

# Check if in WINTER
if (month == "jan" or month == "feb") or (month == "dec" and day >= 21) or (month == "mar" and day <= 19):
    print(f"{month.capitalize()} {day} is in Winter")
# Check if in SPRING
elif (month == "apr" or month == "may") or (month == "mar" and day >= 20) or (month == "jun" and day <= 20):
    print(f"{month.capitalize()} {day} is in Spring")
# Check if in SUMMER
elif (month == "jul" or month == "aug") or (month == "jun" and day >= 21) or (month == "sep" and day <= 21):
    print(f"{month.capitalize()} {day} is in Summer")
# If all others fail, its FALL!
else:
    print(f"{month.capitalize()} {day} is in Fall")
