def break_words(stuff):
    """This function will break up for us"""
    words=stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word"""
    word=words.pop(0)
    return word
    
def print_last_word(words):
    """Prints the last word"""
    words=words.pop(-1)
    return word

def sort_sentence(sentence):
    """Takes full sentence and sorts the words"""
    words=break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Prints the first and the last words of a sentence"""
    words=break_words(sentence)
    first=print_first_word(words)
    last=print_last_word
    print first
    print last
    



        

    
    
