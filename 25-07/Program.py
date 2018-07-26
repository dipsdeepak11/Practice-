#learn about split(),sort(),join() function
#program to sort words in a given input sentence in given order

def sortSentence(sentence,order=0):
    #extracting the words out of the sentence
    words=sentence.split(" ")

    #sorting the words now in given order
    words.sort(order)

    #jonining the words to make the sentence again\
    new_Sentence=" ".join(words)

    return new_sentence


#main program
input_sentence=raw_input("Enter any sentence you want to sort")
print ("you have printed %s ",input_sentence)
input_order=raw_input("Input order :0 for increasing and 1 for descentding order")

result=sortSentence(input_Sentence,order)
print("sorted sentence is %s",result)