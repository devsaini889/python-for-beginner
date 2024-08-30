A simple program to remove the punctuation in a string 

punc = '''!@#$&*/.,';`~'''

string = str(input("Enter the string: "))

new_str= ''

for i in string:
    if i not in punc:
        new_str+=i


print(new_str)