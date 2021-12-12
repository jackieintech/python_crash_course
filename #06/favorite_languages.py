favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

people_poll = ['jen', 'mary', 'joey', 'phil']

for people in people_poll :
    if people in favorite_languages :
        print(f"{people.title()}, thank you for taking the poll!")
    else:
        print(f"{people.title()}, please take the poll!")
