'''
App build on the console version of the blackjack game in file BlackJack.py.
Images from: https://opengameart.org/content/playing-cards-0
To work properly will need 'assets' folder in file path containing cards images.
'''

import os
import random
import tkinter as tk
from PIL import ImageTk, Image
assets_folder = os.path.abspath(r'C:\Users\PLKANIE3\PycharmProjects\LearningPython\TkinterExample\assets')

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return ''.join((self.suit, self.value))
    def get_file(self):
        # self.cardImage = tk.PhotoImage(file=assets_folder+'\\'+''.join((self.suit,self.value))+'.png')
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

class Deck:
    def __init__(self):
        # self.cards = [Card(s,v) for s in ['Spades','Clubs','Hearts','Diamonds']
        #               for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]
        self.cards = [Card(s,v) for s in ['s','c','h','d']
                      for v in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']]
    def shuffle(self):
        if len(self.cards)>1:
            random.shuffle(self.cards)
    def deal(self):
        if len(self.cards)>1:
            return self.cards.pop(0)

class Hand:
    def __init__(self,dealer = False):
        self.dealer = dealer
        self.cards = []
        self.value = 0
    def add_card(self,card):
        self.cards.append(card)
    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            # if card.value.isnumeric():
            #     self.value += int(card.value)
            # else:
            #     if int(card.value == 1):
            #         has_ace = True
            #         self.value += 11
            #     elif self.value > 10:
            #         self.value += 10
            if int(card.value)==1:
                has_ace = True
                self.value += 11
            elif int(card.value)>10:
                self.value += 10
            else:
                self.value += int(card.value)
        if has_ace and self.value > 21:
            self.value -= 10
    def get_value(self):
        self.calculate_value()
        return self.value

class GameState:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand(dealer=True)
        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

        self.has_winner = ''

    def player_is_over(self):
        return self.player_hand.get_value()>21

    def someone_has_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value()==21:
            player = True
        if self.dealer_hand.get_value()==21:
            dealer = True
        if player and dealer:
            return 'dp'
        elif player:
            return 'p'
        elif dealer:
            return 'd'
        return False

    def hit(self):
        self.player_hand.add_card(self.deck.deal())
        if self.someone_has_blackjack() == 'p':
            self.has_winner = 'p'
        if self.player_is_over():
            self.has_winner = 'd'
        return self.has_winner

    def get_table_state(self):
        blackjack = False
        winner = self.has_winner
        if not winner:
            winner = self.someone_has_blackjack()
            if winner:
                blackjack = True
        table_state = {
            'player_cards': self.player_hand.cards,
            'dealer_cards': self.dealer_hand.cards,
            'has_winner': winner,
            'blackjack': blackjack
        }
        return table_state

    def calculate_final_state(self):
        player_hand_value = self.player_hand.get_value()
        dealer_hand_value = self.dealer_hand.get_value()
        if player_hand_value == dealer_hand_value:
            winner = 'dp'
        elif player_hand_value > dealer_hand_value:
            winner = 'p'
        else:
            winner = 'd'
        table_state = {
            'player_cards': self.player_hand.cards,
            'dealer_cards': self.dealer_hand.cards,
            'has_winner': winner,
        }
        return table_state

    def player_score_as_text(self):
        return 'Score: '+str(self.player_hand.get_value())

class GameScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        #constants
        self.title('Blackjack')
        self.geometry('800x600')
        self.resizable(False, False)
        self.CARD_ORIGINAL_POSITION = 100
        self.CARD_WIDTH_OFFSET = 100
        self.PLAYER_CARD_HEIGHT = 350
        self.DEALER_CARD_HEIGHT = 150
        self.PLAYER_SCORE_TEXT_COORDS= (400,450)
        self.WINNER_TEXT_COORDS = (400,250)
        #set up game screen and frames
        self.game_state = GameState()
        self.game_screen = tk.Canvas(self,bg='white', width=800, height=500)
        self.bottom_frame = tk.Frame(self, width=800, height=100, bg='black')
        self.bottom_frame.pack_propagate(0)
        #set up buttons
        self.hit_button = tk.Button(self.bottom_frame, text='Hit', width=25, command=self.hit)
        self.stick_button = tk.Button(self.bottom_frame, text='Stick', width=25, command=self.stick)
        self.play_again_button= tk.Button(self.bottom_frame, text='Play again', width=25, command=self.play_again)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', width=25, command=self.destroy)
        #putting elements in the game screen
        self.hit_button.pack(side=tk.LEFT, padx=(100,200))
        self.stick_button.pack(side=tk.LEFT)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.game_screen.pack(side=tk.LEFT,anchor=tk.N)
        self.display_table()
    def display_table(self, hide_dealer=True, table_state=None):
        if not table_state:
            table_state = self.game_state.get_table_state()
        player_card_images = [card.get_file() for card in table_state['player_cards']]
        dealer_cards_images = [card.get_file() for card in table_state['dealer_cards']]
        if hide_dealer and not table_state['blackjack']:
            dealer_cards_images[0] = Card.get_back_file()
        self.game_screen.delete('ALL')
        self.tabletop_image = tk.PhotoImage(file=assets_folder+'/tabletop.png')
        self.game_screen.create_image((400,250), image=self.tabletop_image)
        self.game_screen.create_text(100, 250,
                                     text='Your cards',
                                     font=('Arial', 20,'bold'),
                                     fill='white')
        for card_number, card_image in enumerate(player_card_images):
            self.game_screen.create_image((self.CARD_ORIGINAL_POSITION +
                                           self.CARD_WIDTH_OFFSET * card_number,
                                           self.PLAYER_CARD_HEIGHT),
                                          image=card_image)
        self.game_screen.create_text(100, 50,
                                     text='Dealer cards',
                                     font=('Arial', 20,'bold'),
                                     fill='white')
        for card_number, card_image in enumerate(dealer_cards_images):
            self.game_screen.create_image((self.CARD_ORIGINAL_POSITION +
                                           self.CARD_WIDTH_OFFSET * card_number,
                                           self.DEALER_CARD_HEIGHT),
                                          image=card_image)
        self.game_screen.create_text(self.PLAYER_SCORE_TEXT_COORDS,
                                     text=self.game_state.player_score_as_text(),
                                     font=(None,20))
        if table_state['has_winner']:
            if table_state['has_winner'] == 'p':
                self.game_screen.create_text(self.WINNER_TEXT_COORDS,
                                             text='You win!',
                                             font=('Arial',50,'bold'),
                                             fill = 'yellow')
            elif table_state['has_winner'] == 'dp':
                self.game_screen.create_text(self.WINNER_TEXT_COORDS,
                                             text='Tie!',
                                             font=('Arial', 50, 'bold'),
                                             fill='yellow')
            else:
                self.game_screen.create_text(self.WINNER_TEXT_COORDS,
                                             text='Dealer wins!',
                                             font=('Arial', 50, 'bold'),
                                             fill='yellow')
            self.show_play_again_options()

    def show_play_again_options(self):
        #hide Hit/Stick buttons
        self.hit_button.pack_forget()
        self.stick_button.pack_forget()
        #show PlayAigain/Quit buttons
        self.play_again_button.pack(side=tk.LEFT,padx=(100,200))
        self.quit_button.pack(side=tk.LEFT)

    def hit(self):
        self.game_state.hit()
        self.display_table()

    def stick(self):
        table_state = self.game_state.calculate_final_state()
        self.display_table(False,table_state)

    def play_again(self):
        self.show_gameplay_buttons()
        self.game_state = GameState()
        self.display_table()

    def show_gameplay_buttons(self):
        #hide PlayAigain/Quit buttons
        self.play_again_button.pack_forget()
        self.quit_button.pack_forget()
        # show Hit/Stick buttons
        self.hit_button.pack(side=tk.LEFT, padx=(100, 200))
        self.stick_button.pack(side=tk.LEFT)

if __name__ == '__main__':
    gs = GameScreen()
    gs.mainloop()




