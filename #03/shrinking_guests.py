guests = ['dakota', 'leena', 'carley', 'bea']
print(guests)
print(f"Hey, {guests[0].title()}! Let's have some wine and read poetry.")
print(f"Hi, {guests[1].title()}! Can you come over so we can overthink things?")
print(f"{guests[2].title()}, I don't know you very well, but I like your vibe.")
print(f"{guests[3].title()}, you're my favorite. Be my friend!")
print(f"Girls, {guests[2].title()} can't make it.")
guests[2] = 'jordan'
print(guests)
print(f"Hey, {guests[0].title()}! Let's have dinner this Saturday.")
print(f"Hi, {guests[1].title()}! I'll make you vegan food!")
print(f"{guests[2].title()}, help me stay on track during this dinner!")
print(f"{guests[3].title()}, let's help each other out!")
print(f"Hey, {guests[0].title()}, {guests[1].title()}, {guests[2].title()}, and {guests[3].title()}. I found a bigger dinner table!")
guests.insert(0, 'layna')
print(guests)
guests.insert(3, 'john')
print(guests)
guests.append('abbey')
print(guests)
print(f"Hey, {guests[0].title()}, come to dinner!")
print(f"I wonder if {guests[1].title()} is available on Saturday.")
print(f"Maybe {guests[2].title()} and Craig can join us soon.")
print(f"I'd very much like to discuss body positivity with {guests[3].title()}!")
print(f"I simply need to have a convo with {guests[4].title()} asap.")
print(f"If {guests[5].title()} joins us, I will DIE!")
print(f"I'm p. sure {guests[6].title()} would find this silly.")
print(f"Hi {guests[0].title()}, {guests[1].title()}, {guests[2].title()}, {guests[3].title()}, {guests[4].title()}, {guests[5].title()}, {guests[6].title()}. Sadly, I no longer have our table. I only have room for two guests.")
uninvited1 = guests.pop()
print(f"I'm sorry, {uninvited1.title()}. I had to remove you from my guest list!")
uninvited2 = guests.pop(0)
print(f"I'm sorry, {uninvited2.title()}. I had to remove you.")
uninvited3 = guests.pop(1)
print(f"I'm sorry, {uninvited3.title()}. I have to uninvite you.")
uninvited4 = guests.pop(1)
print(f"I'm sorry, {uninvited4.title()}. I had to remove your name.")
uninvited5 = guests.pop()
print(f"I'm sorry, {uninvited5.title()}. I promise I'll make it up to you.")
print(f"Hey, {guests[0].title()}, you're still invited! See you soon!")
print(f"Hey, {guests[1].title()}, I still expect you!")
print(guests)
del guests[0]
print(guests)
del guests[0]
print(guests)