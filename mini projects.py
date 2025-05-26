#weight converter using functions
"""def lbs_to_kg():
    weight = float(input("weight in pounds: "))
    print(weight * 0.453592)
lbs_to_kg()

def kgs_to_lbs():
    weight = float(input("weight:"))
    print(weight / 0.453592)
kgs_to_lbs()




#weight converter using loops
def weight_converter():
    WEIGHT = int(input("weight: "))
    unit = input("(L)bs or (K)g: ")
    if unit.upper() == "L":
        converted = WEIGHT* 0.45
        print (f"you are {converted} kilos")
    else:
        converted = WEIGHT // 0.45
        print (f"you are {converted} pounds")

weight_converter()"""


#emoji converter
def emoji_converter(message):
    words = message.split(" ")
    emojis = \
        {"smile": "😊", "sad": "😒"}
    output = ""
    for word in words:
        output += emojis.get(word, word) + ""
    return output

message = input(">")
emoji_converter(message)
print(emoji_converter(message))