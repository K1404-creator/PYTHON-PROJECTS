with open("story.txt", "r") as f:
    story = f.read()


words  = set()  #as we need unique

start_ofword =  -1

target_start = "<"
target_end = ">"

# for index, value in enumerate(iterable, start = 0)
#  index recieve the current counter value for each iteration while the value will receive corresponding item
#  from the iterable.

for i  , char in enumerate(story):   #enumerate gives access to the position as well as the element at that position
    if char == target_start:
        start_ofword = i


    if char == target_end and start_ofword != -1:
        word = story[start_ofword : i +1]
        words.add(word)
        start_ofword = -1

# if found the ending bracket and we
# should have the starting angle bracket # marked by start_ofword: if it is = -1 we havent found the starting bracket
# if it is equal to anything else it means we did find the starting bracket


answers = {}


for word in words:
    answer = input("Enter a word for" + word + " " )
    #answer[key] = [value]
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
    #replaces all words with user input story.replace generates a new string

print(story)


