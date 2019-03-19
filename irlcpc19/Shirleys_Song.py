name = input()

def rhyme(nm, letter):
    if nm[0].lower() != letter:
        return letter + nm[1:]
    else:
        return nm[1:]

print("{}, {}, bo-{}".format(name,name, rhyme(name, 'b')))
print("bo-na-na fanna, fo-{}".format(rhyme(name, 'f')))
print("fee fi mo-{}, {}!".format(rhyme(name, 'm'), name))

