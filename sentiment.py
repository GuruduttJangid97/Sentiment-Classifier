punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', "~", "`"]

# To Remove The Punctuation from Tweet Text
def strip_punctuation(word):
    for char in punctuation_chars:
        word = word.replace(char, "")
    return word

print(strip_punctuation("This is the Test~~`!!!!!"))



# list of positive words to use
postive_word = []

with open("assets/positive_words.txt") as pos_f:
    for line in pos_f:
        if line[0]!= ";" and line[0]!="\n":
            postive_word.append(line.strip())
    #print(postive_word)

#get_pos function to calculate positive score
def get_pos(str):
    text = str.lower()
    words = text.split()
    count = 0

    for word in words:
        if word in postive_word:
            count += 1
    return count




# list of negative words to use
negative_word = []

with open("assets/negative_words.txt") as pos_f:
    for line in pos_f:
        if line[0]!=";"and line[0]!="\n":
            negative_word.append(line.strip())
    #print(negative_word)

#get_neg function to calculate negative score
def get_neg(str):
    text = str.lower()
    words = text.split()
    count = 0

    for word in words:
        if word in negative_word:
            count += 1
    return count
    
#Testing Function
print(get_neg('sad'))
print(get_pos('happy')) 