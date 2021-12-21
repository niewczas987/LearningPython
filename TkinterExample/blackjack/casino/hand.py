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
