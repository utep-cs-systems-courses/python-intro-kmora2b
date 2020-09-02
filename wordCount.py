import re, sys

word_dict = {}

input_file = open(sys.argv[1], "r")
word_string = input_file.read()
input_file.close() 

#TEST
#print(word_string)

proc_strlist = re.sub(r'[^\w\s]',' ',word_string.lower() ).split()
proc_strlist.sort()
print(proc_strlist)

for s in proc_strlist:
    print(s)
    if s not in word_dict:
        word_dict[s] = 1
    else:
        word_dict[s] += 1
#TEST
#print(word_dict)

output_file = open(sys.argv[1][:len(sys.argv[1])-4] + "Output.txt", "w")


for k in word_dict:
    output_file.write(k + " " + str(word_dict[k]) + "\n")

output_file.close()




