import json,os
from difflib import get_close_matches

data = json.load(open("dictionary.json"))



def word_search():

    word = input("Search here")
    os.system('cls')
    print("The word is: ",word)
    word = word.lower()
    if word in data.keys():
        print(data[word])
    else:
        closematches = get_close_matches(word, data.keys())

        if len(closematches) == 0:
            print("INVALID INPUT, PLEASE TRY AGAIN")
            return
        else:
            for i in closematches:
                print(i)
            print(f"If the suggestion {closematches[0]} is correct, press 1")
            print(f"If the suggestion {closematches[1]} is correct, press 2 ")
            print(f"If the suggestion {closematches[2]} is correct press 3") 
            print("If none of the suggestions are correct, please try again")
            userinput = int(input())
            if userinput == 1:
                print(data[closematches[0]])
            elif userinput == 2:
                print(data[closematches[1]])
            elif userinput == 3:
                print(data[closematches[2]])
            else:
                print("INVALID INPUT, PLEASE TRY AGAIN")
                return
    

while True:
    word_search()
    