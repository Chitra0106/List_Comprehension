
import pandas
data = pandas.read_csv(r"C:\Users\mailc\PythonPractise\ListComperhension\NATO-alphabet-start\NATO-alphabet-start\nato_phonetic_alphabet.csv")
data_dict = data.to_dict(orient='records')
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for(index,row) in data.iterrows()}
print(phonetic_dict.values())
data_frame = pandas.DataFrame(data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ".upper())
output = [phonetic_dict[letter]  for letter in word]
print(output)
