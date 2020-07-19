from random import randint


# Functions
def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print()
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')
    return name


def guess_age():
    print()
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print()
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test0(name):
    print()
    print("I'll make you a question", name + ".")
    print()
    print("What color is my underware?!. *Slap!!*?")
    print()
    print("1. Red.")
    print("2. Blue.")
    print("3. Green.")
    print("4. *Return the Slap*.")
    while True:
        _answer = int(input())
        if _answer != 4:
            print("Please, try again.")
        else:
            break


def test1(name):
    print("I'll make you a questions.")
    patrick = ("2. No, this is {0}".format(name),
               "2. Noo, this is {0}!".format(name),
               "2. NOO!!, THIS IS {0}!!!. I'm not the Krusty Krab...".format(name.upper()))
    for i in range(3):
        print()
        print("""
        *Ring*
        *Ring*
        *Response the telephone*
        Telephone: Is this the Krusty Krab?""")
        print()
        print("1. Yes, it is.")
        print(patrick[i])
        print("3. Of Course.")
        while True:
            _answer = int(input())
            if _answer != 2:
                print("Please, try again.")
            else:
                break


def test2(name):
    responses = ("Maybe.",
                 "Yes.",
                 "Yup.")
    man_ray = ("Excuse me sir, but I do believe you've dropped your wallet",
               "What? I just saw you drop it. Here",
               "It is yours. I am trying to be a good person and return it to you.",
               """(Suppose {0} instead of 'Patrick Star')
               ╔═══════════════════════════════╗
               ║  ~~~ ~~~~~~ ~~ ~~~~ ~~ ~~~~~  ║
               ║  ┌───────┐  ~~~ ~~ ~~~~~ ~~   ║
               ║  │ *pic* │      PATRICK       ║
               ║  │       │       STAR         ║
               ║  └───────┘                    ║
               ╚═══════════════════════════════╝
               Aren't you {0}?
               """.format(name),
               "And this is your ID",
               "I found this ID in this wallet. And if that's the case, this must be your wallet.",
               "Then take it.",
               "You dim-bulb! Take back your wallet or I'll rip your arms off!")
    patrick = ("1. Doesn't look familiar to me.",
               "1. Nope, it's not mine",
               "1. Return what to  who?",
               "1. Yup.",
               "1. Yup.",
               "1. That makes sense to me",
               "1. It's not my wallet.",
               "DaPieBot: No. Wrong. Good people don't rip other people's arm off!")
    for i in range(8):
        if i != 7:
            print()
            print(man_ray[i])
            print()
            print(patrick[i])
            print(responses[randint(0, 2)])
        else:
            print()
            print(man_ray[i])
            print()
            print(patrick[i])
        while True:
            _answer = int(input())
            if _answer != 1:
                print("Please, try again.")
            else:
                break


def end():
    print('Well, is the end!. Then...')
    print('Congratulations, have a nice day!')


# Principal code
functions = {
    0: test0,
    1: test1,
    2: test2
}
random_num = randint(0, 3)
if random_num == 3:
    random_num -= 1
_func = functions[random_num]
greet('DaPieBot', '2020')
names = remind_name()
guess_age()
count()
_func(names)
end()
