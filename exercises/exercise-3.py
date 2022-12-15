# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

dog_age_in_human_years = int(input("Input a dog's age in human years. > "))
dog_age_in_dog_years = 0

for years_lived in range(0, dog_age_in_human_years):
    if years_lived <= 1:
        dog_age_in_dog_years += 10
    else:
        dog_age_in_dog_years += 7

print(f"The dog's age in dog years is {dog_age_in_dog_years}")
