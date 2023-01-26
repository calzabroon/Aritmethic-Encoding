import math

file = open("text.txt", "r")
file_encoder = open("encoded.txt", "a")


file_encoder.truncate(0)

#here are the two dictionaries
#the one for the sender which is updated as it reads the txt file
#and the one for the counter which updates aswell but with 0 instead of the character


dictionary = []

dictionary_counter = []

dictionary_codes = []

x = "a" #start with arbitrary value, will get overwritten

#this loop counts how many of each character are in the txt file
while(1):
  
  if x != "": #continues if we are not at the end of the txt file
    x = file.read(1) #reads the next character

    #this just checks for certain character not yet in the orinal alphabet
    #moreso unique icons like '/', '>' and most importanly ''' which i couldnt add
    if (x not in dictionary):
      dictionary.append(x)
      dictionary_counter.append(int(0))

    
    dictionary_counter[dictionary.index(x)] = dictionary_counter[dictionary.index(x)] + 1
  else:
    #here we are at the end of the file but still yet too read the last remaning character which we do now
    dictionary_counter[dictionary.index(x)] = dictionary_counter[dictionary.index(x)] + 1

    break


total = 0

#the total is used for the probability of a word in the document
for i in range(len(dictionary_counter)):
  total = total + dictionary_counter[i]
  

#prints out all the words and the number of them occuring and their probability
for i in range(len(dictionary_counter)):
  print(dictionary[i] + ": " + str(dictionary_counter[i]) + ": " + str(dictionary_counter[i]/total))


entropy = 0
#this caluclates the entropy
#it uses the simple entropy equation given in the notes
for i in range(len(dictionary_counter)):
  entropy = entropy + (dictionary_counter[i]/total)*math.log(1/(dictionary_counter[i]/total), (2))

print("entropy: " + str(entropy))
  

#arithmetic coding
a = 0
np = 0
n = 0
P = 0
P_div = 0
power_counter = 0
#in this loop we cycle through each charcter in the array and by looking at its probability we build a code word for it prefix free
for i in range(len(dictionary)):
  P = dictionary_counter[i]/total
  P_div = 1/P

  while(1):
    if (2**power_counter > P_div):
      n = power_counter + 1
      break
    else:
      power_counter = power_counter + 1
  
  #this is the equation "c-1<2^n(a)<c" and then converted to binary with the front 0s intact
  code = (bin(round((2**n)*(a)))[2:].zfill(n))
  #new dictionary to store all the codes
  dictionary_codes.append(code)
  print(dictionary[i] + ": " + str(code) + ", length: " + str(n))
  #dictionary_codes.append(bin(round(code)))

  a = a + P

  n = 0
  P = 0
  P_div = 0
  power_counter = 0



#this part here re reads the file and applies each character its code word and then writes it into the decoder.txt file
x = 'a'
file.seek(0)

while(1):
  
  if x != "": #continues if we are not at the end of the txt file
    x = file.read(1) #reads the next character

    
    file_encoder.write(str(dictionary_codes[dictionary.index(x)]))

    
  else:
    #here we are at the end of the file but still yet too read the last remaning character which we do now
    file_encoder.write(str(dictionary_codes[dictionary.index(x)]))

    break


#finally this loop reads teh encoded txt file and then decodes it printing it into decoded.txt
file_encoder.close()
file_encoder = open("encoded.txt", "r")

file_decoded = open("decoded.txt", "a")
file_decoded.truncate(0)

x = 'a'
file.seek(0)

for i in range(total):
  if x != "": #contniues if we are not at the end of the txt file
    x = file.read(1) #reads the next character

    #checks if its a codeword
    if (x in dictionary):
      #if it it converts it back and writes to decoded.txt
      file_decoded.write(x)
      x = "0"
    else:
      #if not adds the next bit
      x = x + file.read(1)

file_decoded.close()

#this part is used to calculate the total amount of bits in the encoded txt file to be compared with the orininal encoding of 169526 bits
x = "a" #start with arbitrary value, will get overwritten
total_bits = 0
file_encoder.seek(0)
characters = 0

for line in file_encoder:
    characters = characters + len(line)


print("total bits sent:" + str(characters))
print("arithmetic/original coding: " + str(100*(characters/169526)) + "%")
