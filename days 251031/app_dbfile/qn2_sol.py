 #Write a Python program that:

    #1. Reads a line of integers from the user (separated by spaces).
    #2. Stores them in a **list** and calculates the **sum and average**.
    #3. Saves the list, sum, and average into a text file named **`numbers_data.txt`**.
    #4. Reads the contents of the file and prints them back to the user.


integers_Seq=input('integers(separated by space):')
print(integers_Seq)
integers=integers_Seq.split()
print(type(integers))
total=0
for i in integers:
    total=total+int()
print(total)
average=total/len(integers)
print(average)
with open("qn2_data.txt","w")as output_file:
    output_file.write(f'list:{integers}\n')
    output_file.write(f'sum:{total}\n')
    output_file.write(f'average:{average}\n')

#output_file.close()
with open("qn2_data.txt","r")as input_file:
    file_integers_line = input_file.readline()
    file_sum_line = input_file.readline()
    file_average_line = input_file.readline()

    print(file_integers_line)
    print(file_sum_line)
    print(file_average_line)
    




 

