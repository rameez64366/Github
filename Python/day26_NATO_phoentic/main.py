import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
dict={row.letter:row.code for (index,row) in data.iterrows()}
def generate():
    name=input("what is your name?:").upper()
    try:
        output = [dict[char] for char in name]
    except KeyError:
        print("sorry only alphabets allowed")
        generate()
    else:
        print(output)

generate()