
names=input("Enter the list of names(seperated by spaces) : ")
new_names=names.split()
List_of_names=[]
for names in new_names:
    names=names.capitalize()
    List_of_names.append(names)
List_of_names.sort()
Tuple_of_names=tuple(List_of_names)
print(List_of_names)
print(Tuple_of_names)
with open("names_data.txt","w") as output_file:
    output_file.write(f"List:{List_of_names}\n")
    output_file.write(f"Tuple:{Tuple_of_names}\n")
with open("names_data.txt","r") as input_file:
    file=input_file.read()
    print(file)