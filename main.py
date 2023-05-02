from signalsProcessing import getSignals
from signalsProcessing import getSignal
import hashlib
import sys


cpt = 0
while True:
    if len(sys.argv) != 3:
        print("Please indicate the  signal and keyword files paths in csv format ...!!!")
        break
    else:
        if cpt == 0:
            print('Argument List:', str(sys.argv))
            digest_signals = hashlib.md5(
                open(sys.argv[1], 'rb').read()).hexdigest()
            digest_keywords = hashlib.md5(
                open(sys.argv[2], 'rb').read()).hexdigest()
            if digest_signals != 'b4394a28720b8173372b0ce2e0352be2':
                print(
                    "The signal file should not be modified, please give the source file\n")
            if digest_keywords != 'ca8a9c8aff57261fb798e9c33367ce6c':
                print(
                    "The keyword file should not be modified, please give the source file\n")
            print("The digest of your files is correct. \n  Signal file digest:" +
                  digest_signals+"\n keywords file digest:" + digest_keywords)
            print("---------------------------------------------\n"
                  + "==============processing files ==============\n"
                    + "---------------------------------------------\n")
            cpt = 1

        choice = input(
            "\n Please enter your choice:\n Tape 1 to get all signals  \n Tape 2 to get the signal that you want. \n Tap q to quit \n")

        if choice == '1':
            print("-------------------------------------------------\n"
                  + "============== getting all signals ==============\n"
                    + "-------------------------------------------------\n")
            print(getSignals(sys.argv[1], sys.argv[2]))

        elif choice == '2':
            node_id = input("Please enter the node id: \n").replace(' ', '')
            print("---------------------------------------------\n"
                  + "============= getting signal: ===============\n"
                    + "---------------------------------------------\n")
            print(getSignal(sys.argv[1], sys.argv[2], node_id))

        elif choice == 'q':
            break
