def no_dups(s):
    # Your code here
    # the sentence will go into a dictionary like they were in the word_count problem, except I'll just put the 'keys' into a new sentence
    counts = {}
    # new_string = ""
    # split up 's', so that I can iterate through each word in the sentence easier
    new_sentence = s.split()
    # print(new_sentence)
    # loop through the split up words to add the word into the dictionary
    for word in new_sentence:
        # if the individual word isn't in the dictionary, then add it 
        # new_string = ""
        if word not in counts:
            counts[word] = 0
            # new_string + f'{word}'
        else:
            counts[word] += 1

    # once I'm done, join them up again to return a new sentence
    list_of_keys = (list(counts.keys()))
    new_string = ' '.join(list_of_keys)
    return new_string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))