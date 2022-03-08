s = input("Text: ")
# indicating all variables to 0
letter, word, sentence = 0, 0, 0
# loop for determining how many letters, words and sentences the string includes.
for i in range(len(s)):
    
    # increase the value of letter by one if a character in the string is alphabetic.
    if s[i].isalpha():
        letter += 1
        
        # increase the value of word by 1 for each whitespace character.
    if s[i] == " ":
        
        word += 1
    
    # increase the value of sentence by one whenever the symbols below are exist  
    if (s[i] == "." or s[i] == "?" or s[i] == "!"):
        sentence += 1

# number of whitespace characters plus one equals to number of words.
word += 1
    
L = (100 * letter) / word
S = (100 * sentence) / word

index = round(0.0588 * L - 0.296 * S - 15.8)
    
if index < 1:
    print("Before Grade 1", end="")
    
elif index >= 16:
    print("Grade 16+", end="")
    
else:
    print("Grade {}".format(index), end="")
        
print("\n", end="")