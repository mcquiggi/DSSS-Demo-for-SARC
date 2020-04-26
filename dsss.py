#**********************************************************************
#   Direct Sequence Spread Spectrum Demonstration Program
#
#   K. McQuiggin VE7ZD
#   2020.04.24
#**********************************************************************


# Necessary imports:
import numpy as np


# Introductory messages:
print "Direct Sequence Spread Spectrum (DSSS) Test Program"
print "Based on SARC Communicator Article, May 2020 by K. McQuiggin VE7ZD\n"
print "Use and modify as you wish!\n"


# Define two messages and two spreading codes as per the article:
messages = [ [1, 0, 1, 1], [0, 0, 1, 1] ]
spread = [ [1, 0], [1, 1] ]
print "There are", np.shape(messages)[0], "messages:", messages
print "There are", np.shape(spread)[0],"spreading codes:", spread, "\n"

# Display each message and the spreading code that will be used for it:
for n in range(np.shape(messages)[0]):
    print "Message", n, ":", messages[n], "will use spreading code:", spread[n]
print ""


# Iterate over each message to convert it from (0, 1) format to (-1, 1) format:
messagesCalc = []
for n in messages:    
    calc = []
    for i in n:
        if i == 0:
            calc.append(-1)
        else:
            calc.append(1)
    messagesCalc.append(calc)
print "Messages converted to calculation (-1, 1) format:", messagesCalc


# Iterate over each spreading code to convert it from (0, 1) format to (-1, 1) format:
spreadCalc = []
for n in spread:   
    calc = []
    for i in n:
        if i == 0:
            calc.append(-1)
        else:
            calc.append(1)
    spreadCalc.append(calc)
print "Spreading codes converted to calculation (-1, 1) format:", spreadCalc, "\n"



#********************************************************************************
#   Spread each message and combine them into the overall interference pattern
#********************************************************************************


# Now replace each bit in each message with the associated proper spreading code:
ssl=[]
dsss=[]
n=0
for m in messagesCalc:
    ssl=[]
    for i in m:
        for j in spreadCalc[n]:
            ssl.append(j*i)
    
    print "Spread message ", n+1, "is:", ssl
    dsss.append(ssl)
    n=n+1

# Compute the interference pattern by adding up all the rows of the array:
interferencePattern = (np.shape(dsss)[1])*[0]
for n in dsss:
    interferencePattern = np.add(interferencePattern, n)
print "\nInterference pattern containing all messages is:", interferencePattern
      


#********************************************************************************
#   Now de-spread each message from the overall interference pattern
#********************************************************************************

# To be written later!


print("\nDone!")
