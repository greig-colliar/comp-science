#!/usr/bin/env python

import sys                              #sys module in order to ensure cross compatibility of the arguments parsing through the various operating systems
import random                           #implements a random number generator
import time                             #Import the time to start - stop clock

# Insertion Sort
def insertion_sort(target, list):       #python fuction will take in a list and cast as an argument
    for index in range(1,len(list)):    #len means length meaning length of the list. Starts index for length that is in list 'elements 0 +' index will look through the list for these indencies. 1 means starts to left most element which is 0 = 1st item
        value = list[index]             #value is the item the index.
        i = index - 1                       #define variable i. i should have a lower index than index.
        while i>=0 and (value < list[i]):   #keep comparing i to number to list all the way to 0.
            list[i+1] = list[i]             #shift number in slot i right to slot +1
            list[i] = value                 #shift value left into slot i
            i = i - 1                       #perform loop over again
        
# Start of main program

# Grab the command line args
filename = sys.argv[1]                      #contains the name of the script you're calling. (main Function) Insert value omtp square brackets
repeats = int(sys.argv[2])                  #2nd command line argument. Repeats for random targets = how many times to repeat search 

# Read the data from the file, convert to ints and stick in a list
lines = open(filename, "r").readlines()     #open the filename - set as read only and read lines in file in one go. lines = string
list = []                                   #Empty list to hold the string
for line in lines:                          #loop through list of strings called lines
    list.append(int(line))                  #convert to a int for the new list

# Create a list of random targets to search for
min = min(list) - 1                         #mimimum of the smallest number in the list.
max = max(list) + 1                         #maximum of the highest number in the list.
target = []                                 #set target to search for as empty. 
for i in range(repeats):                    #loop takes takes i variable which is in range and takes repeat from cmd
    target.append(random.randint(min, max)) #append the target and use min and max on random intergers.

# Boolean Function to test if list sorted or not

# Insertion sort time search
start_time = time.process_time()                   #Start the clock
for i in range(repeats):                    #Loop for variable 'i' in range for repeat
    result = insertion_sort(target[i], list)#loop through result of sort, show target integer in the list
stop_time = time.process_time()                    #Stop the cock
insertion_sort = stop_time - start_time     #stop insertion sort time


# Print results
print (list), insertion_sort                #print length of the list
