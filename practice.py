sports = ["Cricket", "Football", "Badminton"]
for index, sport in enumerate(sports, start=1):
         print(index,sport)

friends = ["Ushan", "Naofel"]
Passions = ["Ai Engineer", "Data Science Engineer"]
for friend in friends:
    for Passion in Passions:
        print(f"{friend} ekjon {Passion}")

nums = [ 33,44,67, 89, 90,100,337]
for num in nums:
    if num % 2 == 0:
        print(num,"Jor Shonkha")

sonkha = [3,6,9,27]
double_sonkha =[x * 2 for x in sonkha]
print(double_sonkha)

numbers = [5, 8, 10, 3, 7]
for nums in numbers:
    if nums % 2 == 0:
        print(nums , "even")
    else:
        print(nums,"odd")


for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()
