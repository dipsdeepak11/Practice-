#program to capitalize the first word of each words in given sentence ans print
#the total number of words in the sentence
def capitalize_first_word(input_sen):
    words=input_sen.split(" ")
    new_words=[]
    total_words=len(words)
    for word in words:
        new_word=word.capitalize()
        new_words.append(new_word)
    
    new_sent=" ".join(new_words)
    return new_sent,total_words



print("enter any sentence which you want to capitalize")
input_sent=raw_input()
new_sent,total_word=capitalize_first_word(input_sent)
print("New sentence is %s and total number of words is %d",(new_sent,total_word))
