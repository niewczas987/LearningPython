from __init__ import assets_folder
from PIL import ImageTk, Image


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return ''.join((self.suit, self.value))
    def get_file(self):
        #open image
        picture = Image.open(assets_folder+'\\'+''.join((self.suit,self.value))+'.png')
        #resize image
        resized = picture.resize((100,150), Image.ANTIALIAS)
        self.cardImage = ImageTk.PhotoImage(resized)
        return self.cardImage
    @classmethod
    def get_back_file(cls):
        # open image
        picture = Image.open(assets_folder+'/back.png')
        # resize image
        resized = picture.resize((100, 150), Image.ANTIALIAS)
        cls.back = ImageTk.PhotoImage(resized)
        return cls.back
