import re, sys, os

# Check if cmd line args are inputted
def check_args_values():
    if len(sys.argv) is not 2:
        print("Correct usage: wordCount.py <input text file>")
        print("NOTE: If you are testing with wordCountTest.py then please ignore this message")
        exit()

# Check if the file exits
def check_file_exists(fname):
    if not os.path.exists(fname):
        print ("File %s doesn't exist! Exiting" % fname)
        exit()

# Read in file
def read_file(fname):
    input_file = open(fname, "r")
    word_string = input_file.read()
    input_file.close() 
    return word_string

# Strip string of punctuation and create sorted dictionary
# dictionary structure: {word : count}
def process_str(string):
    proc_strlist = re.sub(r'[^\w\s]',' ',string.lower() ).split()
    proc_strlist.sort()

    for s in proc_strlist:
        if s not in word_dict:
            word_dict[s] = 1
        else:
            word_dict[s] += 1
    return word_dict

# Write dictionary values line by line 
def write_into_file(fname, word_dict):
    output_file = open( fname[ : len(fname)-4] + "Output.txt", "w")

    for k in word_dict:
        output_file.write(k + " " + str(word_dict[k]) + "\n")

    output_file.close()

if __name__ == "__main__":
    word_dict = {}
    check_args_values()

    fname = sys.argv[1]
    check_file_exists(fname)

    word_string = read_file(fname)
    word_dict = process_str(word_string)
    write_into_file(fname, word_dict)

    print("File creation successful")


