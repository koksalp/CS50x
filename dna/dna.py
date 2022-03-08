import sys
import re

if len(sys.argv) != 3:
    sys.exit("Usage: python dna.py data.csv sequence.txt")

# function to find max consecutive repeats for all STR
def max_repeat(STR: list, DNA_sample: str):

    answer=[]

    for i in STR:
        groups = re.findall(r'(?:{})+'.format(i), DNA_sample)

        # error handling in case STR not found in DNA sample
        try:
            largest = max(groups, key=len)
            answer.append(len(largest) // len(i))
        except:
            answer.append(0)

    return answer

database_info = []

# get database info from csv file and store each person's data in a
# dictionary and store each dictionary in the list called database_info
with open(sys.argv[1]) as file:
    line = file.readlines()
    STR = line[0][5:].rstrip("\n").split(",")

    for i in range(1, len(line)):
        divided = line[i].rstrip("\n").split(",")
        name = divided[0]
        divided.pop(0)
        temp = {}

        try:
            temp[name] = list(map(int, divided))
        except:
            temp[name] = divided
        database_info.append(temp)

# getting DNA sample from txt file
with open(sys.argv[2]) as file2:
    DNA_sample = file2.readlines()[0].rstrip("\n")

# find max number of consecutive repetation for each STR in DNA sample
repeat = max_repeat(STR, DNA_sample)

is_found = 0

# compare the result found above with each person's STR in the database #and if found print out the name who matches
for i in database_info:
    if list(i.values())[0] == repeat:
        print(list(i.keys())[0])
        is_found = 1

# if no matches exist print no match
if is_found == 0:
    print("No match")