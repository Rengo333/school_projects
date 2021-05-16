'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
TEXTS[0] = TEXTS[0].replace(',', '').replace('.', '').replace("-","")
TEXTS[1] = TEXTS[1].replace(',', '').replace('.', '').replace("-","")
TEXTS[2] = TEXTS[2].replace(',', '').replace('.', '').replace("-","")
texts1 = [TEXTS[0].split(), TEXTS[1].split(), TEXTS[2].split()]
words = 0
title_case = 0
upper_case = 0
lower_case = 0
num_strings = 0
sum_nums = 0
oddelovac = "-"*15
graf = "*"
counts_words = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0}
users = {"USERS": {"bob": "123", "ann": "pass123", "mike": "password123", "Liz": "pass123"}}
user_name = str(input("username: "))
user_pass = str(input("password: "))
if users["USERS"].get(user_name) == user_pass:
    print(oddelovac)
    print("Welcome to the app, ",user_name)
    print("We have 3 texts to be analyzed.")
    print(oddelovac)
    users_choice = (int(input("Enter a number btw. 1 and 3 to select: "))-1)
    print(oddelovac)
    if users_choice in range(len(TEXTS)):
        for i1 in texts1[users_choice]:
            if i1.isalpha():
                words += 1
                if i1[0].isupper():
                    title_case += 1
                if i1.isupper():
                    upper_case += 1
                if i1.islower():
                    lower_case += 1
            elif i1.isdigit():
                num_strings += 1
                sum_nums += int(i1)
            if str(len(i1)) in counts_words:
                counts_words[str(len(i1))] += 1

        print("There are", words, "words in the selected text.")
        print("There are", title_case, "titlecase words.")
        print("There are", upper_case, "uppercase words.")
        print("There are", lower_case, "lowercase words.")
        print("There are", num_strings, "numeric strings.")
        print("The sum of all the numbers", sum_nums)
        print(oddelovac)
        print("LEN | OCCURENCES | NR.")
        print(oddelovac)
        for cislo1 in counts_words:
            print(str(cislo1) + "|", graf * int(counts_words[cislo1]), "|", str(counts_words[cislo1]))
    else:
        print("Wrong choice!")
        exit()
else:
    print("Wrong password or username!")
    exit()
