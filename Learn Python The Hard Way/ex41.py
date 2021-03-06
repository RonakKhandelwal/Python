import random
from urllib import urlopen
import sys

WORD_URL="http://learncodethehardway.org/words.txt"
WORDS=[]

PHASES={
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self,***)":
        "class %%% has-a __init__ that takes self and *** as parameters",
    "class %%%(object):\n\tdef ***(self,@@@)":
        "class %%% has a function named *** which takes self and @@@ as parameters",
    "***=%%%()":
        "Set *** to instantiate from class %%%",
    "***.***(@@@)":
        "from *** get the function *** ,and call it with parameter self and @@@",
    "***.***='***'":
        "from *** get the *** attribute and set it to '***'."
}

#do they want the drill phases first

PHASE_FIRST=False
if len(sys.argv)==2 and sys.argv[1]=="english":
    PHASE_FIRST=True
#load up words from website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet, phase):
    class_names=[w.capitalize() for w in 
                 random.sample(WORDS,snippet.count("%%%"))]
                 
    other_names=random.sample(WORDS,snippet.count("***"))
    results=[]
    param_names=[]
    
    for i in range(0,snippet.count("@@@")):
        param_count=random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS,param_count)))
    for sentence in snippet, phase:
         result=sentence[:]
         for word in class_names:
            result=result.replace("%%%",word,1)
            
         for word in other_names:
            result=result.replace("***",word,1)
        
         for word in param_names:    
            result=result.replace("@@@",word,1)
    
         results.append(result)

    return results
        
        
    
        
        
     
    

try:
    while True:
        snippets=PHASES.keys()
        random.shuffle(snippets)
        
        for snippet in snippets:
            pharse=PHASES[snippet]
            question,answer=convert(snippet,pharse)
            if PHASE_FIRST:
                question,answer=answer,question
                
            print question
            
            raw_input('> ')
            print "Answer :",answer

except EOFError:
    print"Bbye"
