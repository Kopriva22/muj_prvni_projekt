# Deklarace proměnných
'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive
topographic feature that rises sharply some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad, which traverse the valley. ''',
'''At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation, which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils represent several varieties of perch, as well as
other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
ODDELOVAC = "-" * 40
uzivatele = dict(bob="123", ann="pass123", mike="password123", liz="pass123")
# Vyžádání přihlašovacích údajů (přihlašovacího jména a hesla) od uživatelů
# a kontrola, zda-li jsou v databazi uzivatelu.
jmeno = input("username: ")
password = input("password: ")
if (jmeno in uzivatele.keys()) and (password == uzivatele[jmeno]):
    print(ODDELOVAC)
    print(f"Welcome to the app, {jmeno}.\nWe have 3 texts to be analyzed.")
    print(ODDELOVAC)
else:
    print(f"Unregistered user {jmeno}. Terminating the program.")
    print(ODDELOVAC)
    exit()

# Nabídka analýzy jednoho ze tří textů pro registrovaného uživatele.
selected_number = input("Enter a number btw. 1 and 3 to select:")
if not selected_number.isnumeric():
    print(f"Entered sigh {selected_number} is not a number. Terminating the program!")
    exit()
elif selected_number.isnumeric() and (int(selected_number) in [1, 2, 3]):
    print(ODDELOVAC)

else:
    print(f"Entered number {selected_number} is not between 1 and 3. Terminating the program.")
    exit()


# Nabídka analýzy jednoho ze tří textů pro registrovaného uživatele.
selected_text = list(TEXTS[int(selected_number)-1].split())

ciste_slovo = ""
title_case = 0
upper_case = 0
lower_case = 0
numeric_case = 0
numeric_sum = 0

# Ocisteni slov od nepotrebnych znaku (.,;:!).
for slovo in selected_text:
    ciste_slovo = slovo.strip(".,;:!")
    if ciste_slovo.istitle():
        title_case += 1
    elif ciste_slovo.isupper():
        upper_case += 1
    elif ciste_slovo.islower():
        lower_case += 1
    elif ciste_slovo.isnumeric():
        numeric_case += 1
        numeric_sum += int(ciste_slovo)
    else:
        pass

print(
    f"There are {len(selected_text)} words in the selected text.",
    f"There are {title_case} titlecase words.",
    f"There are {upper_case} uppercase words.",
    f"There are {lower_case} lowercase words.",
    f"There are {numeric_case} numeric strings.",
    f"The sum of all the numbers {numeric_sum}.",
    ODDELOVAC,
    sep="\n"
)

# SLOUPCOVY GRAF - urceni nejdelsiho slova
nejdelsi = 0
list_text = []
calculator = {}
for slovo in selected_text:
    if len(slovo) > nejdelsi:
        nejdelsi = len(slovo)

for polozka in selected_text:
    if len(polozka) in calculator.keys():
        calculator[len(polozka)] += 1
    else:
        calculator[len(polozka)] = 1

print(f"Prehled poctu: {sorted(calculator.items())}")
print(
    ODDELOVAC,
    "LEN| OCCURENCES"+(" " * (nejdelsi-1))+"|NR.",
    ODDELOVAC,
    sep = "\n"
)
for radek in range(1,nejdelsi+1):
    if radek in calculator.keys():
        print(
            " " * (3-len(str(radek))),
            f"{radek}|",
            ("*" * calculator[radek]),
            (" " * (nejdelsi+10-calculator[radek])),
            f"|{calculator[radek]}",
            sep = ""
        )
    else:
        print(
            " " * (3 - len(str(radek))),
            f"{radek}|",
            " " * (nejdelsi + 10),
            f"|{0}",
            sep = ""
        )
