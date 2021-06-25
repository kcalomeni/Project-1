# Program Name: Treasure Hunt
# Developer Name: ITCS 1950 (Kailey Calomeni)
# Date: 06/11/2021
# Description: This game is a treasure hunting game that involves picking many
# different treasure chests to find the golden gem!

def displayIntro():
    print('''Welcome to Redwood Mansion! My name is Kailey, and I am so glad you
could join me. I need your help searching through treasure chests to find the
golden gem. Once found, I will be able to travel freely on my own. Well, no time
to lose! Let's get started, shall we?''')
    print()

def chooseChest():
    chest = ''
    while chest != '1' and chest != '2' and chest != '3' and chest != '4':
        print('Which chest should we pick first?')
        chest = input()

    return chest

def checkChest (chosenChest):
    print('You see a chest with a lock...')
    time.sleep(2)
    print('It is very dusty and covered in webs...')
    time.sleep(2)
    print('The key is nowhere to be found...')
    time.sleep(2)
    print('Something falls on your head!')
    time.sleep(2)
    print('The key! It fits the lock!')
    time.sleep(2)
    print('Open it and see what you found!')
    time.sleep(2)

    woodenChest = random.randint (1, 4)
    forestChest = random.randint (1, 4)
    flowerChest = random.randint (1, 4)
    cherryChest = random.randint (1, 4)

    if chosenChest == str(woodenChest):
        print('Uh oh, a bunch of spiders!')
    elif chosenChest == str(forestChest):
        print('Another key? Weird...')
    elif chosenChest == str(flowerChest):
        print('A box full of costumes!')
    elif chosenChest == str(cherryChest):
        print('A compass...really!')

print('''So far, we haven't had much luck. It seems as though this task is
tricker than I had hoped. If we don't find the chest with the golden gem soon,
I am going to be stuck in this castle forever! Let's keep looking.''')

    print()

def chooseChest1 ():
    chest1 = ''
    while chest1 != '5' and chest1 != '6' and chest1 != '7' and chest1 != '8':
        print('Which chest should we check next?')
        chest1 = input()

    return chest1

def checkChest1 (chosenChest1):
    print('You see a chest covered by a carpet...')
    time.sleep(2)
    print('It has a big lock on the top...')
    time.sleep(2)
    print('The key is on the floor...')
    time.sleep(2)
    print('It is covered in dust and debris...')
    time.sleep(2)
    print('Clean the key and see what you found!')
    time.sleep(2)

    oceanChest1 = random.randint (5, 8)
    fairyChest1 = random.randint (5, 8)
    heartChest1 = random.randint (5, 8)
    branchChest1 = random.randint (5, 8)

    if chosenChest1 == str(oceanChest1):
        print('Another key again...seriously...')
    elif chosenChest1 == str(fairyChest1):
        print('Three boxes full of feathers...')
    elif chosenChest1 == str(heartChest1):
        print('This chest is empty!')
    elif chosenChest1 == str(branchChest1):
        print('Books, books, and more books!')

print('''Okay, no luck yet. This is our last batch of chests. We have only four
left that we did not go through. The golden gem has to be in one of these! Let
the searching begin...again!''')

     print()

def chooseChest2 ():
    chest2 = ''
    while chest2 != '9' and chest2 != '10' and chest2 != '11' and chest2 != '12':
        print('Which chest should we check last?')
        chest2 = input()

    return chest2

def checkChest2 (chosenChest2):
    print('You find a gold chest...')
    time.sleep(2)
    print('The chest has two locks...')
    time.sleep(2)
    print('There is a key on the chest...')
    time.sleep(2)
    print('You see another key sticking out under the chest...')
    time.sleep(2)
    print('Try the keys in the locks, and see what you found!')

    goldenChest2 = random.randint (9, 12)
    silverChest2 = random.randint (9, 12)
    emeraldChest2 = random.randint (9, 12)
    rubyChest2 = random.randint (9, 12)

    if chosenChest2 == str(goldenChest2):
        print('A gem! The golden gem!')
    elif chosenChest2 == str(silverChest2):
        print('A silver diamond...so close!')
    elif chosenChest2 == str(emeraldChest2):
        print('Two emeralds...so close!')
    elif chosenChest2 == str(rubyChest2):
        print('Twelve beautiful rubies...so close!')

    
def main():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        chestNumber = chooseChest()
        checkChest = (chestNumber)

        print('Would you like to play again?')
        playAgain = input()
