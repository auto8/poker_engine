from cards import *

plist = []

def get_players():
	players = int(input('how many in hand: '))
	return players 

def check_winners(*kwargs):
	hcards = []
	kickers = []
	for i in kwargs[0]:
		hcards.append(i.hcard)
	
	x = max(hcards)
	same = []
	y = 0 
	for i in kwargs[0]:
		if i.hcard == x:
			same.append(i)
	if len(same) > 1:
		hmm = []
		for i in same:
			if i.kicker > y:
				y = i.kicker
				hmm.append(i)
		if len(hmm) > 1:
			return hmm
		else:
			return hmm[0]
	else:
		for i in kwargs[0]:
			if i.hcard == x:
				return i
	

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

if len(temp) > 1:
	winner = check_winners(temp)
else:
	winner = temp[0]

for i in plist:
	display(i.hand)

print()
display(board)
print()
display(winner.hand)
