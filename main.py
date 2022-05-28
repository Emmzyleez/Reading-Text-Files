# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open("story.txt") as file_object:
        contents = file_object.read()
    
    return contents


output =read_file_content("./story.txt")
print(output)



def count_words():
    text = read_file_content("./story.txt")
    counts = {}
    words = text.split()

    for word in words:
        if word in counts:
            counts[word] +=1

        else:
            counts[word] = 1

    return counts


output =count_words()
print(output)
    
