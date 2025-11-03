

    ### Problem 3

   # Write a Python program that:

    #1. Accepts a sentence from the user.
    #2. Splits the sentence into words and stores them in a **list**.
    #3. Converts all words to **uppercase** and stores them in a **tuple**.
    #4. Saves both the list and tuple into a file named **`sentence_data.txt`**.
    #5. Reads back the data from the file and displays it on the screen.


sentence=input("enter the sentence:")
words_list =sentence.split()
upper_list=[]
for word in words_list:
    upper_word=word.upper()
    upper_list.append(word.upper())
words_tuple=tuple(upper_list)
print(words_list,type(words_list))
print(words_tuple,type(words_tuple))
with open("sentence_data.txt","w") as output_file:
    output_file.write(f'List:{words_list}\n')
    output_file.write(f'tuple:{words_tuple}\n')

with open("senetnce_data.txt","r") as input_file:
    file=input_file.read()
    print(file)





