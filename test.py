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
temp = []
for i in plist:
	if i.rank >= x:
		x = i.rank
		winner = i

temp.append(winner)
for i in plist:
	if i == winner:
		continue
	elif i.rank == winner.rank:
		temp.append(i)
x = 0 
if len(temp) > 1:
	for i in temp:
		if i.hcard > x:
			x = i.hcard
			winner = i 
	for i in temp:
		display(i.hand)
		print(i.hcard)

	display(winner.hand)
	display(board)	
