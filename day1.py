# Calorie Counting

with open('inputs/day1.in') as input_file:
    elf_calories = [[int(calory) for calory in calories.split('\n')] for calories in input_file.read().split('\n\n')]

sum_of_calories: list[int] = [sum(i) for i in elf_calories]
max_calory = max(sum_of_calories)
elf_with_max_calory = sum_of_calories.index(max_calory)
print(elf_with_max_calory, max_calory)
