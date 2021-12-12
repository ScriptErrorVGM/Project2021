import string
def main():
    def isPangram(sentence, alphabet=string.ascii_lowercase): 
        return set(alphabet) <= set(sentence.lower()) 

    print(isPangram(input('Sentence: '))) # set (alphabet) creates a set of all characters in the given alphabet.
    #set (sentence.lower ()) creates a lowercase set of all characters in the input sentence.
    #The comparison set (alphabet) <= set (sentence.lower () tests whether the characters in the sentence are at least alphabetical characters.

if __name__ == "__main__":
    main()    