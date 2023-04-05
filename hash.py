import numpy as np
import sys
import os

symbol = "X"

def displayhash(hash):
    os.system('cls')
    print("TIC-TAC-TOE:")
    print(" ")
    for i in range(len(hash)):
        print(end="|")
        for j in range(len(hash[0])):
            print(hash[i][j], end=""+"|")
        print()

def verification(hash):
    if hash[0][0] == symbol and hash[1][0] == symbol and hash[2][0] == symbol:
        print("You are Winner!")
        question()
    elif hash[0][0] == symbol and hash[0][1] == symbol and hash[0][2] == symbol:
        print("You are Winner!")
        question()
    elif hash[0][2] == symbol and hash[1][2] == symbol and hash[2][2] == symbol:
        print("You are Winner!")
        question()
    elif hash[2][0] == symbol and hash[2][1] == symbol and hash[2][2] == symbol:
        print("You are Winner!")
        question()
    elif hash[0][0] == symbol and hash[1][1] == symbol and hash[2][2] == symbol:
        print("You are Winner!")
        question()
    elif hash[0][2] == symbol and hash[1][1] == symbol and hash[2][0] == symbol:
        print("You are Winner!")
        question()

def menuHash(hash):
    option = int(1) 
    while option > 0:
        option = int(input("\nChoose a number to put the simbol: "))
        symbol = input("Type your symbol: ").upper()
        if option  == 1:
            hash[0][0] = symbol
            displayhash(hash)
            verification(hash)
        elif option == 2:
            hash[0][1] = symbol
            displayhash(hash)
            verification(hash)
        elif option == 3:
            hash[0][2] = symbol
            displayhash(hash)
            verification(hash)
        elif option == 4:
            hash[1][0] = symbol
            displayhash(hash)
            verification(hash)
        elif option == 5:
            hash[1][1] = symbol
            displayhash(hash)
            verification(hash)
        elif option == 6:
            hash[1][2] = symbol
            displayhash(hash)
            verification(hash)
        elif option == 7:
            hash[2][0] = symbol
            displayhash(hash)
            verification(hash)
        elif option == 8:
            hash[2][1] = symbol
            displayhash(hash)
            verification(hash)
        elif option == 9:
            hash[2][2] = symbol
            displayhash(hash)
            verification(hash)

def question():
    option = input("would you like to play again?"+" Yes or Not? ").upper()
    if option == "YES":
        os.system('cls')
        main()
    else:
        os.system('cls')
        sys.exit()

def main():
    hash = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
    displayhash(hash)
    menuHash(hash)
    
main()