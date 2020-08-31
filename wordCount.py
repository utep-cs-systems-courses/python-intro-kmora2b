import re, sys

word_dict = {}

input_file = open(sys.argv[1], "r")
word_string = input_file.read()
input_f.close() 

#TEST
#print(word_string)

proc_strlist = re.sub(r'[^\w\s]','',word_string.lower() ).split()
proc_strlist.sort()

for s in proc_strlist:
    if s not in word_dict:
        word_dict[s] = 1
    else:
        word_dict[s] += 1
#TEST
#print(word_dict)

for k in word_dict:
    print(k + " " + str(word_dict[k]))



