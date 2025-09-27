#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed="Mutt"):
        self.name = name
        self.breed= breed
    
    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self
    
    def adopt(self,owner_name):
        self.owner = owner_name

fido = Dog("Fido","ducky")
# print(fido is fido.showing_self())
print(fido.breed)
# fido.owner = "Sophie"
# print(fido.owner)
fido.adopt("Sophie")
print(fido.owner)
# print(fido.favourite_toy)