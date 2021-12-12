favorite_beverage = 'diet coke'
print("Is favorite_beverage == 'diet coke'? I predict True.")
print(favorite_beverage == 'diet coke')

print("\nIs favorite_beverage == 'tea'? I predict False.")
print(favorite_beverage == 'tea')

print("\nIs favorite != 'tea'? I predict True.")
print(favorite_beverage != 'tea')

singer = 'kevin devine'
print("Is singer == 'kevin devine'? I predict True.")
print(singer == 'kevin devine')

print("\nIs singer == 'conor oberst'? I predict False.")
print(singer == 'conor oberst')

laptop = 'apple'
print("Is the laptop 'dell'? I predict False.")
print(laptop == 'dell')

print("\nIs the laptop 'apple'? I predict True.")
print(laptop == 'apple')

apartment = 'big'
print("Is the apartment 'big'? I predict True.")
print(apartment == 'big')

print("\nIs the apartment 'small'? I predict False.")
print(apartment == 'small')

hair = 'blonde'
print("Is her hair 'blonde'? I predict True.")
print(hair == 'blonde')

print("\nIs her hair 'red'? I predict False.")
print(hair == 'red')

hometown = 'CG'
print("Is my hometown 'SP'? I predict False.")
print(hometown == 'SP')

print("\nIs my hometown 'CG'? I predict True.")
print(hometown == 'CG')

color = 'black'
print("Is my color 'black'? I predict True.")
print(color == 'black')

print("\nIs my color 'purple'? I predict False.")
print(color == 'purple')

birthday = 'july'
print("Is my birthday in 'july'? I predict True.")
print(birthday == 'july')

print("\nIs my birthday in 'december'? I predict False.")
print(birthday == 'december')

love = 'dogs'
print("Are 'dogs' my love? I predict True.")
print(love == 'dogs')

print("\nAre 'cats' my love? I predict False.")
print(love == 'cats')

weight = '55'
print("Is my weight '65'? I predict False.")
print(weight == '65')

print("\nIs my weight '55'? I predict True.")
print(weight == '55')

name = 'Jaqueline'
print("Is my name 'jaqueline'? I predict False.")
print(name == 'jaqueline')

print("Is my name 'jaqueline'? I predict True.")
print(name.lower() == 'jaqueline')

pants = '34'
print("Do I wear '34'? I predict True.")
print(pants == '34')
print("Do I wear '38'? I predict False.")
print(pants == '38')
print("Is '34' bigger than '38'? I predict False.")
print(pants > '38')
print("Is '34' less than '38'? I predict True.")
print(pants < '38')

old = '57'
print("Is the man old? I predict True.")
print(old >= '50')

young = '29'
print("Is the girl young? I predict True.")
print(young <= '29')

print("Are they both young? I predict False.")
print(old <= '29' and young <= "29")

print("Is either of them old? I predict True.")
print(old >= '50' or young <="50")


family = ['sonia', 'edson', 'evelyn', 'fernande', 'tuka']
print("Is 'sonia' in my family? I predict True.")
print('sonia' in family)

print("Is 'becca' in my family? I predict False.")
print('becca' in family)

sister = 'evelyn'
print("Is 'evelyn' not in my family? I predict False.")
if sister not in family:
    print(f"{sister.title()}, where did you go?")

bestie = 'becca'
if bestie not in family:
    print(f"{bestie.title()}, you're like family nonetheless.")