#passCrack
#Alex Ross 1/3/19
#This program will attempt to brute force sha256 hashes read from an infile
#with 5 optional rules applied

import hashlib
from itertools import permutations

def option0(hashlist):
#   "option 0 : 7 letter word, first letter capitalized, 1-digit # is appended"
    wordfile = open("words.txt", "r",encoding='utf-8')
    outfile  = open("solved.txt", "w")
    i=0
    for line in wordfile:
        i+=1
        capital = (line.capitalize().rstrip())
# prints every thousandth value to demonstrate progress
        if i == 1000:
            i=0
            print(line)
        for val in range(10):
            capitaldigit = str(capital)
            capitaldigit+=(str(val))
            testhash = hashlib.sha256((str(capitaldigit)).encode('utf-8')).hexdigest()
            for element in hashlist:
                if testhash == element:
                    print("Solved password :", element, ":", capitaldigit, file=outfile)
                    print("Solved password :", element, ":", capitaldigit)
    outfile.close()
    wordfile.close()
def option1(hashlist):
#   "option 1 : A four digit password with at least one of the following special charactersin the beginning:(*,~,!,#)")
    outfile  = open("solved.txt", "w")
    symbol = list(permutations(["*","~","!","#"]))
    for val in range(10000, 20000):
        mystring = str(val)[1:]
#   prints every hundreth value to demonstrate progress
        if val%100 == 0:
            print(mystring)
        for chars in symbol:
            charval = mystring
            ''.join(chars) + charval
            testhash = hashlib.sha256((str(chars)).encode('utf-8')).hexdigest()
            for element in hashlist:
                if testhash == element:
                    print("Solved password :", element, ":", chars, file=outfile)
                    print("Solved password :", element, ":", chars)
    outfile.close()
def option2(hashlist):
#   "option 2 : 5 letter word, containing 'a' replaced with '@', containing 'l' replaced with '1'")
    wordfile = open("words.txt", "r",encoding='utf-8')
    outfile  = open("solved.txt", "w")
    i=0
    for line in wordfile:
        tempstr = line
        for char in tempstr:
            tempstr = tempstr.replace("a","@")
            tempstr = tempstr.replace("A","@")
            tempstr = tempstr.replace("l","1")
            tempstr = tempstr.replace("L","1")
            i+=1
            if i %2000 == 0:
                print(tempstr)
            testhash = hashlib.sha256((str(tempstr)).encode('utf-8')).hexdigest()
#   prints every thousandth value to demonstrate progress
            for element in hashlist:
                if testhash == element:
                    print("Solved password :", element,":", tempstr, file=outfile)
                    print("Solved password :", element, ":", tempstr)
                    
    outfile.close()
def option3(hashlist):
#   "option 3 : Any word that is made with digits up to 6 digits length"
#   im assuming this rule is supposed to be a string of 6 numbers, hence 'digits'
    outfile  = open("solved.txt", "w")
    for val in range(100000, 1000000):
        mystring = str(val)[1:]
        testhash = hashlib.sha256((str(mystring)).encode('utf-8')).hexdigest()
#   prints every thousandth value to demonstrate progress
        if val % 1000 == 0:
            print(mystring)
        for element in hashlist:
            if testhash == element:
                print("Solved password :", element, ":", mystring, file=outfile)
                print("Solved password :", element, ":", mystring)
def option4(hashlist):
#   "option 4 : Any number of chars single word from standard dictionary"
    wordfile = open("words.txt", "r",encoding='utf-8')
    outfile  = open("solved.txt", "w")
    i=0
    for line in wordfile:
        linetext = line.rstrip()
        testhash = hashlib.sha256((str(linetext)).encode('utf-8')).hexdigest()
        i+=1
#   prints every thousandth guess to demonstrate progress
        if i % 1000 == 0:
            print(linetext)
        for element in hashlist:
            if testhash == element:
                print("Solved password :", element, ":", linetext, file=outfile)
                print("Solved password :", element, ":", linetext)
def main():
    filename = input("what is the name of the file to be searched for hashes? eg: password.txt ")
    infile = open(filename, "r")
    
    userlist = [];
    hashlist = [];

    for line in infile:
        split = line.split(":")
        user = split[0]
        userlist.append(user)
        hashpass = split[1]
        hashlist.append(hashpass)
#        print("user is " + user)
#        print("hashpass is " + hashpass)

    print ("Recovered the following data from ", filename)
    i=0
    for index in userlist:
        print("user ", i, " is ", index)
        i+=1
    i=0
    
    for index in hashlist:
        print("hashed pass ", i, " is ", index)
        i+=1
    i=0
    infile.close()
    
    print("option 0 : 7 letter word, first letter capitalized, 1-digit # is appended")
    print("option 1 : A four digit password with at least one of the following special charactersin the beginning:(*,~,!,#)") 
    print("option 2 : 5 letter word, containing 'a' replaced with '@', containing 'l' replaced with '1'")
    print("option 3 : Any word that is made with digits up to 6 digits length")
    print("option 4 : Any number of chars single word from standard dictionary")
    option = eval(input("Which option would you like to select? "))
    if option == 0:
        option0(hashlist)
    if option == 1:
        option1(hashlist)
    if option == 2:
        option2(hashlist)
    if option == 3:
        option3(hashlist)
    if option == 4:
        option4(hashlist)
    print("Operation completed, thanks for using Pass.py")



    
    
main()

