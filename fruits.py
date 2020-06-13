""" Here the object oriented programming
    concept is described """

class Fruits: #class maned fruits
    def __init__(self,color,flavor):
        self.color=color
        self.flavor=flavor
    def __str__(self):
        return "This fruit is {} in color and {} in taste".format(self.color,self.flavor)

class Apple(Fruits): #apple take the fruit class values
    pass

f=Apple("red","sweet")
print(f)

class Grape(Fruits): #grape take the fruit class values
    pass

g=Apple("green","sour")
print(g)
