import random


class Numbers:

    def __init__(self):
        pass

    def guessed_number(self):
        given = random.randint(2, 100)
        return given

    def hints(self, given):
        print("let's play a gameee.... guess the number strudi picked for you... ")

        while True:
            guess = int(input("give number: "))

            if guess == given:
                print("YOU'VE IT G*D DAMN RIGHT HUN!")
                break


            elif any(guess ** i == given for i in range(2, 71)):
                print("OEHHH.. WRONG GUESS.. \ntip: how many times is it worth???")

            elif given - 3 == guess:

                print("WRONG WRONG WRONGGG.. \ntip: up to some more years together, hunbunnn")


            elif given - 36 == guess:

                print("EHHHHHH! \ntip: OLDIEEE!!!")


            elif given - 30 == guess:

                print("NOPE \ntip: round is not always funn..")


            elif guess >= given and guess <= given +5:
                print("""
                oeeeeeehhhhh super close.. 
                I am always coming but never arrive
                I am always leaving but never left
                I can be hot or cold, or even in between
                I am essential to life, but also a danger unseen
                What am I? """)




            elif guess <= given and guess >= given - 5:
                    print("""

                    close close closee.. 
                    I am a word with six letters
                    Remove one letter and I'm twelve
                    Remove another and I'm fifteen
                    What am I? """)


            elif guess >= given and guess <= given + 10:

                print("getting closee.. drop me from the ceiling")



            elif guess <= given and guess >= given - 10:
                print("getting close.. my balloon ")



            elif guess >= given and guess <= given + 20:
                print("hmm.. lower moesk.. dummie")


            elif guess <= given and guess >= given - 20:
                print("hmm.. higher moesk.. dummie")

            elif guess >= given and guess <= given + 30:

                print("shawty go lowlowlow hunbun")



            elif guess <= given and guess >= given - 30:
                print("Bring me higher, love")




            elif guess >= given and guess <= given + 50:
                print("lower, lower, a lot lowerrrr")


            elif guess <= given and guess >= given - 50:

                print("guess a lot higher dude")


            else:

                print('idk')




