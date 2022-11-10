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

French_or_english= input("What language are you translating To? Enter 'Eng' for English and 'Fr' for French: ")


if French_or_english.upper()== "ENG":
    mot=input("Entrez le mot a traduire: ")

    if mot.upper() in French_to_English_Dict:
        mot_traduit=French_to_English_Dict[mot.upper()]
        print("La traduction du mot "+mot+" en Anglais est: "+mot_traduit)
    else:
        print("Le mot n'existe pas dans le dictionnaire!")
        
elif French_or_english.upper()== "FR":
    word=input("Enter the word to translate: ")

    if word.upper() in English_to_french_Dict:
        word_translated=English_to_french_Dict[word.upper()]
        print("The translation of "+word+" in french is: "+word_translated)
    else:
        print("This word does not exist in the Dictionary!")

else:
    print("!!!!!!  That is not a supported language. Please select 'Eng' for English or 'Fr' for French!!!!!!\n (!!!! La langue choisie est indisponible. Choisi 'Eng' pour L'Anglais ou 'Fr' pour le francais !!!!!!!!)")
