French_to_English_Dict={
        "BONJOUR":"Good morning",
        "MERCI":"Thank you",
        "OUI":"Yes",
        "NON":"No",
        "APRES":"After",
        "INTELLIGENT":"Intelligent",
        "VERT":"green",
        "ROUGE":"Red",
        "JAUNE":"Yellow",
        "ETOILE":"Star",
        "PRUNIER":"plum tree",
        "PRUNE":"Plum"
    }
English_to_french_Dict={
    "CAR":"voiture",
    "BROTHER":"Frere",
    "NAME":"Nom",
    "FIRST NAME":"Prenom",
    "FATHER":"Pere",
    "MOTHER":"Mere",
    "CAMEROON":"Cameroun"    
}
English_to_Bulgarian_Dict={
    "CAR":"Кола",
    "BROTHER":"брат",
    "NAME":"Име",
    "FIRST NAME":"първо име",
    "FATHER":"баща",
    "MOTHER":"просто",
    "CAMEROUN":"Камерун" 
}
def translator(language,word):
    if language== "ENG":
        if word in French_to_English_Dict:
            print(f"La traduction du mot {word_to_translate} en Anglais est: {French_to_English_Dict[word_to_translate]}")
            
        else:
            print("The word is not in the dictionary")
    elif language== "FR":
        if word in English_to_french_Dict:
            print(f"The translation of {word_to_translate} in french is: {English_to_french_Dict[word_to_translate]}")
        else:
            print("The word is not in the dictionary")
    elif language== "BUL":
        if word in English_to_Bulgarian_Dict:
            print(f"The translation of {word_to_translate} in Bulgarian is: {English_to_Bulgarian_Dict[word_to_translate]}")
        else:
            print("The word is not in the dictionary")
    else:
        print("!!!!!!  That is not a supported language. Please select 'Eng' for English or 'Fr' for French!!!!!!\n (!!!! La langue choisie est indisponible. Choisi 'Eng' pour L'Anglais ou 'Fr' pour le francais !!!!!!!!)")

                
dest_language=input("What language are you translating To? Enter 'Eng' for English, 'Fr' for French and 'Bul' for Bulgarian: ")
dest_language=dest_language.upper()
word_to_translate=input("Enter a word to translate: ")
word_to_translate=word_to_translate.upper()
translator(dest_language,word_to_translate)

        
        
        
    
