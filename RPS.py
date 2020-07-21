import random
import time
import colorama
from colorama import init
from colorama import Fore, Back, Style
#import huyni



print (Back.WHITE)
print (Fore.BLACK)
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')



pla = 0
co = 0
e = 0
f = 0
c = ('string')



print ("Rock, papper, scisorss\n")



while True:

    while pla == 0:
        
        pla = input ("choose rock-1, papper-2 or scissors-3\n")


        
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')



        if pla == "konami":



            print (Back.RED)
            print ('ultimate mode turned on')
            print (Back.WHITE)

            plak = 0

            while True:

                while plak == 0:

                    plak = input ("choose rock-1, papper-2 or scissors-3\n")

                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                    
                    try:
                        plak = int(plak)
                        if plak == 1:
                            print ('Rock')
                        elif plak == 2:
                            print ('Papper')
                        elif plak == 3:
                            print ('Scissors') 
                        else:
                            print ('wrong input')
                            plak = 0

                    except:
                        plak = 0
                        print ('wrong input')
                    

                cok = 0


                time.sleep(1)


                if plak == 1:
                    cok = 3
                if plak == 2:
                    cok = 1
                if plak == 3:
                    cok = 2

                if int(cok) == 1:
                    ck = ("rock")
                elif int(cok) == 2:
                    ck = ("papper")
                elif (cok) == 3:
                    ck = ("scissors")


                print ("computer choise " + str (ck)) 


                time.sleep(1)


                if int(plak) == int(cok):
                    print ("draw")

                elif (int(plak) == 1 and int(cok) == 2):
                    print ("computer wins")
                    e += 1

                elif (int(plak) == 1 and int(cok) == 3):
                    print ("human wins")
                    f += 1

                elif (int(plak) == 2 and int(cok) == 1):
                    print ("human wins")
                    f += 1

                elif (int(plak) == 2 and int(cok) == 3):
                    print ("computer wins")
                    e += 1

                elif (int(plak) == 3 and int(cok) == 1):
                    print ("computer wins")
                    e += 1

                elif (int(plak) == 3 and int(cok) == 2):
                    print ("human wins")
                    f += 1


                plak = 0


                time.sleep(1)


                
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

                print ('SCORE:')
                print ('HUMAN   ',  f, 'COMPUTER   ', e) 



        try:

            pla = int(pla)
            if pla == 1:

                print ('Rock')
            elif pla == 2:

                print ('Papper')
            elif pla == 3:

                print ('Scissors') 
            else:

                print ('wrong input')
                pla = 0


        except:

            pla = 0
            print ('wrong input')



    time.sleep(1)



    co = (random.randint(1,3))
    

    if int(co) == 1:

         c = ("rock")


    elif int(co) == 2:

        c = ("papper")


    elif (co) == 3:

        c = ("scissors")

    
    print ("computer choise " + str (c)) 

    

    time.sleep(1)


    
    if int(pla) == int(co):

        print ("draw")

    elif (int(pla) == 1 and int(co) == 2):
        
        e += 1
        print ("human wins")
    
    elif (int(pla) == 1 and int(co) == 3):

        print ("human wins")
        f += 1

    elif (int(pla) == 2 and int(co) == 1):

        print ("human wins")
        f += 1

    elif (int(pla) == 2 and int(co) == 3):

        print ("computer wins")
        e += 1

    elif (int(pla) == 3 and int(co) == 1):

        print ("computer wins")
        e += 1

    elif (int(pla) == 3 and int(co) == 2):
        
        print ("human wins")
        f += 1


    pla = 0


    time.sleep(1)


    
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    print ('SCORE:')
    print ('HUMAN   ',  f, 'COMPUTER   ', e) 