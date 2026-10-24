import os
#We will see some os functions
#First will be seeing if a file exists inside our folder
if os.path.exists('Text.txt'):
    print('Text.txt exists')

else:
    print('Text.txt does not exist')

#Now we will see how to remove a file from the folder
#os.remove('Text2.txt') #Text2 Have been removed