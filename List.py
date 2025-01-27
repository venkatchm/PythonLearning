
animals = ['cat', 'dog', 'horse', 'elephant', 'camel']

#index 
print(animals[1])

#negative index 
print(animals[-1])

#slice 
print(animals[2:4])

#slice shortcut
print(animals[3:])

print(animals[:2])

isCatExists = 'cat' in animals
print(isCatExists)

animals[3] = 'pony'
print(animals)

print(list(['cat', 'dog', 'horse', 'elephant', 'camel']))
print(list('camel'))