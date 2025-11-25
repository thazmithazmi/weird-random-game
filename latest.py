import requests
import random
import os

latest_release = requests.get('https://pastebin.com/raw/pKL5xQXH').text

#Do not change. Used for auto updating.
version_number = 3
latest_version = 0
for i in latest_release.splitlines():
    if 'version_number' in i:
        split = i.split(' ')
        latest_version = split[len(split)-1]
        break

kidneys = 1
money = 0.00

interaction_state = {
    'angry_doctor': False
}

def int_input(prompt):
    output = input(prompt)
    
    try:
        output = int(output)
    except:
        print('Invalid integer.')
        return int_input(prompt)
    else:
        return output

def choice_input(prompt, highestoption):
    output = int_input(prompt)

    if output > highestoption or output < 1:
        print('that\'s literally not even an option')
        return choice_input(prompt, highestoption)
    
    return output

def buy_coffee():
    global money
    global interaction_state

    if money < 2: print('too broke for coffee'); return

    dice_roll = random.randint(1, 100)
    money -= 2
    match dice_roll:
        case x if x < 5 and interaction_state['angry_doctor']: print('you notice the doctor approaching you\nbefore you can react he eats your coffee and runs away\n\nyou don\'t get a refund')
        case x if x < 10: print('you immediately spill your coffee\n\nyou don\'t get a refund')
        case x if x < 50: print('you eat your coffee')
        case x if x > 50: print('you enjoy your coffee, sipping from the cup every so often')
    

def sell_kidney():
    global money
    global kidneys
    global interaction_state
    
    if interaction_state['angry_doctor']:
        print('the doctor wants you out of his sight')
        return
    if kidneys < 1: print('you can\'t sell another kidney'); return
    kidneys -= 1

    print('the doctor takes your kidney and hands you $5')
    print('1. accept the money\n2. say it\'s not enough\n3. take your kidney back')
    
    dice_roll = random.randint(1, 100)
    choice = choice_input('\ndo something: ', 3)
    match choice:
        case 1: money += 5; print('you take the money and leave')
        case x if x == 2 and dice_roll < 10: money += 50; print('the doctor sighs and gives you $50')
        case x if x == 2 and dice_roll < 50: money += 20; print('the doctor sighs and gives you $20')
        case x if x == 2 and dice_roll > 50: print('the doctor gets angry and eats your kidney\nhe shoos you out')
        case 3: 
            print('you lunge for your kidney')
            if dice_roll <= 25:
                print('after a dramatic and epic anime battle, the doctor eats your kidney\n\nfortunately, you ate his wallet +$15')
            interaction_state['angry_doctor'] = True
            money += 15
def update_game():
    with open(__file__, 'w') as f:
        f.write(latest_release)
    quit()

if int(latest_version.strip()) > version_number:
    update = choice_input('You have an older version of the weird random game. Would you like to update?\n1. Yes\n2. No\n\nAnswer: ', 2)
    if update == 1: update_game()
        

#dialog = requests.get(url).text.split('\n')
options = [
    ['buy a coffee', buy_coffee],
    ['sell_kidney', sell_kidney],
]

while True:
    os.system('cls')
    print(f'you have ${money}\n\n')

    for i in range(len(options)):
        print(str(i+1)+'. '+options[i][0])

    choice = choice_input('\ndo something: ', len(options))
    
    os.system('cls')
    options[choice-1][1]()


    input('\nEnter to continue')
