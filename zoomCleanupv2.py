import os
import re

#List of words to be replaced with blank/nothing. ensure to include a preceeding or trailing space so as not to leave an extra space in the doc
replacements = (' um', ' Um', ' ur', ' Ur', ' like', ' Like', '[\n\r]Um,' , '[\n\r]um,', ' uh', ' Uh', '[\n\r]Uh, ', '[\n\r]uh, ', '[\n\r]Oh, ', '[\n\r]oh, ', '[\n\r]uh ', '[\n\r]Uh ', ' kind of', ' you know', ' I I', 'Oh, ', 'oh, ')

#Add folder locations here

raw_folder = "***/raw/"# File location here
clean_folder = "***/clean/" # File location here

# Function to cleanup certain lines in one file:

def clean_data_file(file, newfile):
 f=open(file, "r")
 lines=f.readlines()
 f.close()
 #make array
 newlines=[]
 # loop through each line:
 for l in lines: 
    #Search for a line that contains only the phrase 'user avatar' and exclude it
  if re.search(r'user avatar', l):
    continue
    #Search for a line that only contains a timestamp and exclude it. e.g. 00:00
  elif re.search(r'[0-9][0-9]:[0-9][0-9]', l):
    continue
#Write all lines except above to the new file
  newlines.append(l)
# Save the file:
 f=open(newfile, "w")
 f.writelines(newlines)
 f.close()
#########

# Function to replace text elements 

def replacetext(file,search_text,replace_text):
  
    # Opening the file in read and write mode
    with open(file,'r+') as f:
  
        # Reading the file data and store
        # it in a file variable
        file = f.read()
          
        # Replacing the pattern with the string
        # in the file data
        file = re.sub(search_text, replace_text, file)
  
        # Setting the position to the top
        # of the page to insert data
        f.seek(0)
          
        # Writing replaced data in the file
        f.write(file)
  
        # Truncating the file size
        f.truncate()
  
    # Return "Text replaced" string
    return "Text replaced"
  

# Use the function on a bunch of files:
# wherever the location of your files are. make sure it's the right pathway


interview_file_list=os.listdir(raw_folder)
for fname in interview_file_list:
  if fname[-4:]==".txt":
    print("Cleaning "+fname+"...  ",end="\r\n")
  else:
    print("Skipping "+fname+"...")
  continue
person_name = fname[:-4]
 
newfile = clean_folder+person_name+'_clean.txt'

# Run first pass to remove timestamp and user avatar lines completely

clean_data_file(raw_folder+fname,newfile)
print("[Phase 1 Done]")

# Run second pass to do word replacement to replace anything in replacements list above with a blank character

for rep in replacements:
 replacetext(newfile,rep,'')

print("[Phase 2 Done]")

# Specific word replacements - no need to include preceeding or trailing spaces for these

replacetext(newfile,'gonna', 'going to')
replacetext(newfile,'the the the', 'the')
replacetext(newfile,'and and and', 'and')
replacetext(newfile,'and and', 'and')
replacetext(newfile,'the the', 'the')
replacetext(newfile,'The the', 'the')
replacetext(newfile,'Yeah', 'yes')
replacetext(newfile,'yeah', 'yes')
replacetext(newfile,'It\'s It\'s', 'Its')
replacetext(newfile,'It It', 'It')
replacetext(newfile,'I don\'t. I don\'t', 'I don\'t')


print("[Phase 3 Done]")
