# This program is used to translate English to french and vice-versa
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
    "CAMEROUN":"Cameroun"    
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

French_or_english_or_bulgarian= input("What language are you translating To? Enter 'Eng' for English, 'Fr' for French and 'Bul' for Bulgarian: ")

French_or_english_or_bulgarian = French_or_english_or_bulgarian.upper()

if French_or_english_or_bulgarian== "ENG":
    mot=input("Entrez le mot a traduire: ")
    mot=mot.upper()

    if mot in French_to_English_Dict:
        mot_traduit=French_to_English_Dict[mot]
        print("La traduction du mot "+mot+" en Anglais est: "+mot_traduit)
    else:
        print("Le mot n'existe pas dans le dictionnaire!")
        
elif French_or_english_or_bulgarian== "FR":
    word=input("Enter the word to translate: ")
    word=word.upper()

    if word in English_to_french_Dict:
        word_translated=English_to_french_Dict[word]
        print("The translation of "+word+" in french is: "+word_translated)
    else:
        print("This word does not exist in the Dictionary!")

elif French_or_english_or_bulgarian =="BUL":
    word=input("Enter the word to translate to bulgarian: ")
    word=word.upper()
    
    if word in English_to_Bulgarian_Dict:
        word_translated=English_to_Bulgarian_Dict[word]
        print("The translation of "+word+" in Bulgarian is: "+word_translated)
    else:
        print("This word does not exist in the Dictionary!")
else:
    print("!!!!!!  That is not a supported language. Please select 'Eng' for English or 'Fr' for French!!!!!!\n (!!!! La langue choisie est indisponible. Choisi 'Eng' pour L'Anglais ou 'Fr' pour le francais !!!!!!!!)")

