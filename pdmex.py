# Python creator of lists for messages in Pure Data

# Import the random library
import random

# Scenes and Interpolation  
#   (fixed values)
interpolation = print("interpolation 10000;")

# octospace 
#   (while)
contatore = 1004
while contatore <= 1023:
    print(contatore, "-octospace", sep="") 
    print("8", ";", sep="")
    contatore += 1

#grainpitch 
#   (while)
contatore = 1004
while contatore <= 1023:
    print(contatore, "-grainpitch", sep="") 
    print(random.randint(1000,10000)/1000, ";", sep="")
    contatore += 1
    
#grainenv 
#   (while)
contatore = 1004
while contatore <= 1023:
    print(contatore, "-grainenv", sep="") 
    print(random.randint(1,100), ";", sep="")
    contatore += 1

#grainamp 
#   (while)
contatore = 1004
while contatore <= 1023:
    print(contatore, "-grainamp", sep="") 
    print(random.randint(1,100)/100, ";", sep="")
    contatore += 1
