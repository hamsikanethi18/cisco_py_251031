

numbers_input=input("Enter a sentence of numbers separated by spaces: ")
numbers_list=[]
for num in numbers_input.split():
    numbers_list.append(int(num))
min_num=min(numbers_list)
max_num=max(numbers_list)

