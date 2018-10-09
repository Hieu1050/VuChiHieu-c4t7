def not_int (a):
    try:
        int (a)
        return False 
    except ValueError:
        return True
from random import randint
character = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf'],
    'Gold': 100,
    'Level': 2
}
character['Gold']+=20
character['Backpack'].append ("Flintstone")
character['Pocket']= ['MonsterDex','Flashlight']
skill = [
    {'Name': 'Tackle',
    'Minimum level': 1,
    'Damage': 5,
    'Hit rate': 0.3},

    
    {'Name': 'Quick attack',
    'Minimum level': 2,
    'Damage': 3,
    'Hit rate': 0.5,},

    
    {'Name': 'Strong Kick',
    'Minimum level': 4,
    'Damage': 7,
    'Hit rate': 0.2,}
]
for i in range (len(skill)) :
    print ("SKILL ",i+1)
    for key in skill[i]:
        print (key,':',skill[i][key])
    print ('==============')
while True:
    x = input ("Choose skill:   ")
    while not_int (x) or (int(x) not in [1,2,3]):
        x = input ("Error, try again:   ")
    x = int (x)
    if x > character['Level']:
        print ("Cannot perform this skill!")
    else :
        hit = randint(0,10)/10
        if hit >= skill[x]['Hit rate']:
            print ('Damage: ',skill[x]['Damage'])
        else:
            print ("Missed!") 
    choice = input ("Continue[1] or end[any other keys]  ")
    if choice != '1':
        break