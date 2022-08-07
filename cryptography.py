# program that receives plain text as input encrypts it adding numbers
# and decrypts at the end of the program

text = str(input())
output = str()
for i in text:
    op = chr(ord(i)+4)  #ord gives the ascii value of word and chr gives the alphabetical value of number
    output = output+op

print('Encrypted text is ',output)

blank = str()
for i in output:
    dec = chr(ord(i)-4)
    blank=blank+dec
print('Decrypted text is ',blank)

#Note: use same number as addition and subtraction