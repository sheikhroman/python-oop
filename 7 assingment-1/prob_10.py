#open the file
text_file = open('/Users/pankaj/file.txt','w')

#initialize an empty list
word_list= []

#iterate 4 times
for i in range (1, 5):
    print("Please enter data: ")
    line = input() #take input
    word_list.append(line) #append to the list


text_file.writelines(word_list) #write 4 words to the file

text_file.close() #don’t forget to close the file