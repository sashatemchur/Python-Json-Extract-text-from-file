import os
import json

with open("data.json", "r", encoding="UTF-8") as text_file: # Opens the file to be read
    text = json.load(text_file) # Jason is reading the file
    
index1 = 0

for i in range(len(text)): # Cycles through the open file
    output_text = text[index1] # Passes through the main list and enters the second list, generally extracts the necessary information from the lists
    index1 += 1 
    print("Player : {0} \n" "Games : {1} \n" "Wins : {2}\n".format(output_text[0], output_text[1], output_text[2]))
            

