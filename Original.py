import math

file = open("text.txt", "r")
#here are the two dictionaries
#the one for the sender which is updated as it reads the txt file
#and the one for the counter which updates aswell but with 0 instead of the character


dictionary = []

dictionary_counter = []

dictionary_codes = []


x = "a" #start with arbitrary value, will get overwritten
total = 0

#this loop counts how characters are in the txt file
while(1):
  
  if x != "": #continues if we are not at the end of the txt file
    x = file.read(1) #reads the next character

    #this just checks for certain character not yet in the orinal alphabet
    #moreso unique icons like '/', '>' and most importanly ''' which i couldnt add
    if (x not in dictionary):
      dictionary.append(x)
      total = total + 1
  else:
    

    break


#there are 75 total character in the text file
#using boring orignal coding we can have each character be 7 bits since 
#2^7 envelopes 77 (log(2)(77) = 7 rounding up)
print("total character: " + str(total))
n = math.ceil((math.log(77, (2))))
print("bits per char: " + str(n))



#so since every character will be 7 bits long
#i wont bother creating a unique codeword for everyone and unstead send 7 bits arbitrary
#since im only doing this to find the length of the code


x = "a" #start with arbitrary value, will get overwritten
total_char = 0
file.seek(0)

#this loop rereads the txt file to count the amount of character in are in it 
while(1):
  if x != "": #continues if we are not at the end of the txt file
    x = file.read(1) #reads the next character
    total_char = total_char + 1 #adds to total char
  else:
    break

print("total characters sent: " + str(total_char))
print("total bits sent: " + str(total_char*n)) #this is the total bits sent assuming all char have the same codeword length of 7 bits