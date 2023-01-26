file = open("text.txt", "r")
file_encoded = open("encoded.txt", "a")
file_decoded = open("decoded.txt", "a")


file_encoded.truncate(0)
file_decoded.truncate(0)


#here are the two dictionaries
#the one for the sender which is updated as it reads the txt file
#and the one for the decoder which updates after and reacts to whats being sent in

#66 total initial in dictionary => 2^7
#a = 0000000
#67= 1000011

dictionary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','.','','\n','0','1','2','3','4','5','6','7','8','9']

dictionary_decoder = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','.','','\n','0','1','2','3','4','5','6','7','8','9']

counter = 0


decoded_message = ""

w = file.read(1) # reads teh first character which gives starting point
x = "a" #start with arbitrary value, will get overwritten


while(1):
  
  if x != "": #contniues if we are not at the end of the txt file
    x = file.read(1) #reads the next character

    #this just checks for certain character not yet in the orinal alphabet
    #moreso unique icons like '/', '>' and most importanly ''' which i couldnt add
    if (x not in dictionary):
      print
      dictionary.append(x)
      dictionary_decoder.append(x)


    if (w + x not in dictionary): #each times checks if w  and x are yet in the alphabet
      #if they are not, we add them to the dictionary, and then send their iteration from before
      dictionary.append(w + x)

      #this segment here is the decoder, which adds the new codeword to their dictionary also
      b = dictionary[dictionary.index(w)] #retireves the sent word
      decoded_message = decoded_message + b  
      c = dictionary[dictionary.index(x)] #and retreives the next character

      code = (bin(dictionary_decoder.index(w))[2:]) #the[2:] removes he '0b' at front so we can see the real number of bits being sent later on 
      code_dec = (bin(dictionary_decoder.index(w))) #we are converting to inary so the LZW can dictionary decoder can recorrect it the binary to an index place and find the corresponf character


      file_encoded.write(str(code))# print all the encoded words into a txt file to be able to read the length of the total message sent
      
      file_decoded.write(str(dictionary_decoder[int(code_dec, 2)]))  #it then checks the code it recieved which is the index of the code sent by encoder and since the dictionaries are almost the same except a step behind it will be able to make a match
      #it prints it into anoter text file
      #file_decoder.write(str(dictionary_decoder.index(w)))
      dictionary_decoder.append(b + c)  #and adds the new codeword to its own dictionary after recieving the message codeword


      counter = counter + 1

      w = x #the starts from the last character
    else:
      w = w + x #if in dictionary, we add to it
  else:
    #here we are at the end of the file but still yet too send the last remaaing character which we do now
    #file_decoder.write(str(dictionary_decoder.index(w)))
    file_decoded.write(str(dictionary_decoder[dictionary.index(w)]))
    file_decoded.close()
    break


file_encoded.close()
file_decoded.close()

file_encoded = open("encoded.txt", "r")

#this part is used to calculate the total amount of bits in the encoded txt file to be compared with the orininal encoding of 169526 bits
x = "a" #start with arbitrary value, will get overwritten
total_bits = 0
file_encoded.seek(0)
characters = 0

for line in file_encoded:
    characters = characters + len(line)


print("total bits sent: " + str(characters))
print("LZW/original coding: " + str(100*(characters/169526)) + "%")

  