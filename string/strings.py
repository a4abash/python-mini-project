#Program that takes input from user create and saves it in file counts lowerCase,UpperCase,Digits and vowel letters in it

string1=str(input('Enter a sentence: '))
f = open('demofile.txt','w') # opens file in read mode
f.write(string1) # write the input txt onto the demofile.txt
f.close() #in some cases, due to buffering, changes made to a file may not show until you close the file.

file = open('demofile.txt','r') # open same file in read mode
lower,upper,digit,vowel = 0,0,0,0 #initializing each of them

for s in file.read():   # reading each character form file line by line using loop
    if s.islower():
        lower=lower+1
    elif s.isupper():
        upper=upper+1
    elif s.isdigit():
        digit=digit+1
    elif 'a'or'e'or'i'or'o'or'u' in s:
        vowel = vowel+1  

print('Lowercase letter:',lower,'\nUpper case letter:',upper,'\nNumber of digits:',digit,'\nNumber of vowel letters:',vowel)

