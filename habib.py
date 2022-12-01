def make_shirt(size, text):
    print(f'{size, text}')

make_shirt(7,'You\'re the best')

make_shirt(10,'I love Python')
make_shirt(5, 'I love Python')
make_shirt(20, 'Believe in yourself')

def describe_city(city, country='USA'):
    print(f'{city} is in {country}')

describe_city('Miami')

def favourite_book(title):
    print(f'my favorite book is {title}')

favourite_book('The BFG')

def listofnumbers(*numbers):
    print((numbers))

listofnumbers(4, 16, 24, 34, 63, 92, 81, 2, 104, 174,)

def reversestrings(word):
    print(word[:: -1])
reversestrings('olleH')