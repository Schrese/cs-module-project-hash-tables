import re

def word_count(s):
    counts = {}
    # def count_inner(s):
    new_sentence = (re.split(' |,|_|-|!|\+|\.| |\"|\:|\;|\=|\/|\\*|\||\[|\]|\{|\}|\(|\)|\*|\^|\&', s))
    # new_sentence = (re.split(' |,|_|-|!|\+|\.| |\"|\:|\;|\=|\/|\\|\\r|\\n|\\t|\||\[|\]|\{|\}|\(|\)|\*|\^|\&', s))
    # print(len(new_sentence))

    if len(new_sentence) <= 1:
        return counts
    elif s == '":;,.-+=/\\|[]{}()*^&':
        return counts
    
    new_sentence = [x for x in new_sentence if len(x) > 0]
    for word in new_sentence:
        word = word.lower()
        print(len(word), 'oaisjdf;oija;oijef')
        if len(word) == 0:
            # counts.popitem()
            print('found a word')
        # print(len(word))
        # if (word in counts) or (len(new_sentence) > 1):
        # if word in counts and word != '':
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    # print(f'{word}: {counts[word]}')
    # print(counts, counts['hello'], 'from here')
    # print(counts.keys())
    # return f'{word}: {counts[word]}'
    print(counts)
    return counts

# def ignore_chars(word):
#     ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '|', '[', ']', '{', '}', '(', ')', '*', '*', '^', '&']
#     # print(ignore)
#     word = re.findall('', word)
#     print(word)
#     for l in word:
#         print(l, 'from ignore function')
#         if l in ignore:
#             l = l.replace(l, '')
#         return word

# print(ignore_chars('potato.'))
# def word_count(s):
#     # Your code here
#     # Create a dictionary that stores individual words as the key and the count as the value

#     # I'll need to use the "re" library for ignoring erronious characters using the findall method OR I can just specify which ones to ignore using its split method
#     # I need to set the split to a variable 
#     # new_split = re.findall(r'[\w]+', s) # didn't work because it was splitting on quotes too...

#     # For each word in the variable, I need to check if it is not in the cache 
#         # If it isn't there, 
#             # then add that word to the dictionary and initialize its count at 0
#         # increase the count of the word by 1 each time it comes up
#     # return the dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'), 'hello')
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))