_author_ = "Ethan Richards"
# CIS 125 
# PigLatin
#PigLAtin.py
#Converts words to pig latin

def main():
    #create a variable to hold Vowels
    
    Vowels = "aeiouAEIOU"
    
    #create a variable to hold the original word
    
    originalWord = input("Input an English word to translate to pig latin: ")
    
    #create a variable to hold the translated word and Initialize it with an empty string
    
    transWord = ""
    
    #create a variable to hold the first letter of the original word.
    
    firstLetter = originalWord[0]
    
    #Test the first letter to see if it is a vowel or consonant
    
    if firstLetter in Vowels:
        transWord = originalWord + "yay"
    else: 
        transWord = originalWord[1:] + firstLetter + "ay"
        
    print(transWord)
main()