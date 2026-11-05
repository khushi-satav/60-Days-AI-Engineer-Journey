class Bird():

     def sound(Self):
          print('birks make sound')

class Crow(Bird):
    def sound(self):
        print('cawcaw') 

class parrot(Bird):
    def sound(self):
        print('sssss')    

Bird1=Crow()
Bird2=parrot()
Bird1.sound()
Bird2.sound()                   