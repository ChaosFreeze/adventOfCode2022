# Calorie Counting

with open('inputs/day1.in') as input_file:
    elf_calories = [[int(calory) for calory in calories.split('\n')] for calories in input_file.read().split('\n\n')]

sum_of_calories = [sum(i) for i in elf_calories]
max_calory = max(sum_of_calories)
elf_with_max_calory = sum_of_calories.index(max_calory)
print(f"The elf carrying most calories is elf no {elf_with_max_calory} which is carrying {max_calory} calories.")
sum_of_three_elves = sum(sorted(sum_of_calories, reverse=True)[:3])
print(sum_of_three_elves)
