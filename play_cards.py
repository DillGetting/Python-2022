import card

# mydeck = card.Deck()
# c = mydeck.deal()
# while c in not None:
#     print(c.show())
#     c = mydeck.deal()
# for c in mydeck:
#     print(c.show())
# mydeck.shuffle()

mydeck = card.Deck()
mydeck.shuffle()
myhand = []
while sum(myhand) < 15:
    myhand.append(mydeck.deal())
print("my hand {}".format(sum(myhand)))
