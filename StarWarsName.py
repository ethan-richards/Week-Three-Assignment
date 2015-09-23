_author_ = "Ethan Richards"
# CIS 125 
# StarWarsName
#StarWarsName.py
#Gives you a star wars name based on your inputs

def main(): 
    
    #prompt the user
    
    lastName = input("Enter your last name: ")
    firstName = input("Enter your first name: ")
    maidenName = input("Enter your mothers maiden name: ")
    townName = input("Enter then name of the town where you were born: ")
    
    #calculate the star wars name
    
    starFirst = lastName[0:3] + firstName [0:2] + " " 
    starLast = maidenName[0:2] + townName[0:3]
    
    #print the star wars name
    
    print("Your Star Wars name is: " + starFirst + starLast)
main()