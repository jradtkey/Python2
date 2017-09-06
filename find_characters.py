word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []

for i in range(0, len(word_list)):
    for j in range(0, len(word_list[i])):
        if word_list[i][j] == 'o':
            new_list.append(word_list[i])
print (new_list)
