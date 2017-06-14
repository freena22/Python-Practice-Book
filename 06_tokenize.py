
# <Tokenizaiton>: the process of converting text into a set of individual components 
# This is an important step when working with any text data
# The goal of tokenization is to convert a large body of text into smaller tokens, or components, that we can work with. 
# In this case, each token is a word in the vocabulary.

text = "Howdy,my,name"
text = text.replace(",",'')  #(1,2,3) 1:old 2:new 3:maxnumber replace
print(text)

family = 'Apple loves luka luka is cute, and I love luka!'
family = family.replace(',', '')
family = family.replace('!', '')
family = family.replace('luka','lumi',2)
print(family)

# example: create the function -- tokenize()

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

clean_chars = [",", ".", "'", ";", "\n"]
cleaned_story = clean_text(story_string, clean_chars)
def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

tokenized_story = tokenize(story_string, clean_chars)
print(tokenized_story[0:10])