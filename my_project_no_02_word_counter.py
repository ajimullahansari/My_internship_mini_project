
#file_name = input("Enter the file name:")
#
#
#num_words = 0
#
#
#with open(file_name,'r') as f:
#    for line in f :
#        words = line.split()
#        num_words += len(words)
#print("Number of words : ")
#print(num_words)







                       #####    OR       ####





#my_file = open('my_file.txt','r')
#data = my_file.read()
#num_of_chars = len(data)
#num_of_words = len(data.split())
#num_of_line = len(data.splitlines())
#print(num_of_chars,num_of_words,num_of_line)







                         ###### function creation




file = open("my_file.txt",mode="r")
num_of_words = 0
num_of_chars = 0
num_of_lines = 0
for line in file:
    num_of_lines+=1
    line=line.strip()
    num_of_chars+=len(line)
    list1=line.split()
    num_of_words+=len(list1)
file.close()
print(num_of_lines,num_of_words,num_of_chars)






