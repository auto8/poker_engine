from cards import *

plist = []

def get_players():
	players = int(input('how many in hand: '))
	return players 


players = get_players()

for i in range(players):
	i = player()
	plist.append(i)

cards = deck()
board = []
for i in plist:
	deal(i.hand, cards, 2)

deal(board, cards, 5)

for i in plist:
	x = hand_data(i.hand, board, i)
	get_rank(x, i)

x = 0
for i in plist:
	if i.rank >= x:
		x = i.rank
		winner = i

for i in plist:
	if i.rank == x:
		if i.hcard > winner.hcard:
			display(i.hand)
			display(winner.hand)
			display(board)
			winner = i
			display(winner.hand)
		else:
			continue
