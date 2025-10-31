salaries =[] #list()

salaries.append(39000)
salaries.append(43000)
salaries.append(56000)
print(salaries)


#to remove salary based on the index
#salaries.remove(43000)



search = 43000
I = 0
search_index = 1
for salary in salaries:
    if salary == search:
        search_index = I
        break
    I+= 1

print(search_index)






