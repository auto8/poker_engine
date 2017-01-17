import random
import sys  
import time

class deck:
	def __init__(self):
		self.dictionary = {'s': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 'h': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 
				'd': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 'c': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]}
		self.suites = ['s', 'h', 'd', 'c'] 

face = ['J', 'Q', 'K', 'A']

def deal(hand, cards, x):
	count = 0 
	for i in cards.suites:
		if len(cards.dictionary[i]) == 0:
			del cards.dictionary[i]
			cards.suites.remove(i)	
	
	for i in range(x):
		a = random.choice(cards.suites)
		first = cards.dictionary[a]
		x = random.choice(first)
		first.remove(x)	
	
		hand.append(a)
		hand.append(x)

def display(cards):
	x = 1
	y = 0  
	temp = [] 
	while x < len(cards):
		count = 0
		if cards[x] > 10:
			for i in range(11, 15):
				if cards[x] == i:
					suite = str(cards[y])
					rank = str(face[count])
					temp.append(rank + suite)
				count += 1 
		else:
			suite = str(cards[y])
			rank = str(cards[x])
			temp.append(rank + suite)
		y += 2
		x += 2
	print(temp)

def hand_data(hand, *args):
	temp = []
	for i in hand:
		temp.append(i)
	for i in args[0]:
		temp.append(i)
	return temp 

def straight(hand, a):
	y = sorted(hand)
	start = 0
	dups = []
	for i in range(1, len(y)):
		if y[start] == y[i]:
			dups.append((y[start]))
		start += 1 
	for i in dups:
		y.remove(i)
		a = len(y)
	start = 0
	temp = []
	count = 1
	x = []
	for i in range(1, a):
		if y[start] + 1 == y[i]:
			if start == 0:
				temp.append(y[start])
				temp.append(y[i])
				count += 1 
			else:
				temp.append(y[i])
				count += 1 
		else:
			count = 1
			temp = []
		if count == 5:
			x = temp
		start += 1 
	if len(x) >= 5:
		return x 


def high_card(hand, player):
	l = [player.hand[1], player.hand[3]]
	count = 0 
	x = 0
	if player.rank == 1:
		for i in l:
			if i not in hand[0]:
				player.kicker = i
				count += 1  
			if i in hand[0]:
				player.hcard = i
		if count == 2:
			player.hcard = hand[0]
			if l[0] > l[1]:
				player.kicker = l[0]
			else:
				player.kicker = l[1]
		print(player.hcard, player.kicker)	
	
	if player.rank == 2:
		x, y = 0, 0 
		out = []
		if len(hand) == 2:
			if hand[0][0] > hand[1][1]:
				x = hand[0][0]
				y = hand[1][1]
			else:
				x = hand[1][1]
				y = hand[0][0]
		else:
			for i in hand:
				out.append(i[0])
			smallest = min(out)
			for i in hand:
				if i[0] == smallest:
					hand.remove(i)
			if hand[0][0] > hand[1][1]:
				x = hand[0][0]
				y = hand[1][1]
			else:
				x = hand[1][1]
				y = hand[0][0]
		player.hcard, player.kicker = x, y
		print(player.hcard, player.kicker)
	
	if player.rank == 3:
		x = 0
		if len(hand) > 1:
			if hand[0][0] > hand[1][1]:
				x = hand[0][0]
			else:
				x = hand[1][1]
		else:
			x = hand[0][0]
		player.hcard = x
		print(player.hcard)	
	if player.rank == 4:
		player.hcard = max(hand)

	if player.rank == 5:
		player.hcard = max(hand)
		
	if player.rank == 6:
		for i in hand:
			if len(i) == 3:
				player.hcard = i[0]
			if len(i) == 2:
				player.kicker = i[0]


	if player.rank == 7:
		if len(hand) >= 2:
			for i in hand:
				if len(i) == 4:
					player.hcard = i[0]
		else:
			player.hcard = hand[0][0]
		print(player.hcard)

def get_rank(community, player):
	suites = ['h', 's', 'c', 'd']
	royal = [14, 13, 12, 11, 10]
	dictionary = {'h': [], 's': [], 'c': [], 'd': []}
	card_value = []
	x = 0 
	y = 1
	while x < len(community): 
		dictionary[community[x]].append(community[y])
		x += 2 
		y += 2

	for i in suites:
		if len(dictionary[i]) >= 5:
			check = straight(dictionary[i], len(dictionary[i]))
			if check != None:
				if sorted(check, reverse=True) == royal:
					player.rank = 9
				else:
					player.rank = 8
					high_card(check, player)
			else:
				player.rank = 5
				high_card(dictionary[i], player)
	
	for i in suites:
		for x in dictionary[i]:
			card_value.append(x)
	
	if straight(card_value, len(card_value)) != None:
		player.rank = 4
		high_card(straight(card_value, len(card_value)), player)
	

	dictionary2 = {}
	for i in card_value:
		dictionary2[i] = []
	
	for i in card_value:
		dictionary2[i].append(i)

	pcount = 0
	temp = []
	pair = False
	trips = False
	quads = False
	for i in dictionary2:
		if len(dictionary2[i]) == 2:
			pair = True
			pcount += 1
			temp.append(dictionary2[i]) 
		if len(dictionary2[i]) == 3:
			trips = True
			temp.append(dictionary2[i])
		if len(dictionary2[i]) == 4:
			quads = True
			temp.append(dictionary2[i])
	
	if pair == True:
		if quads == True:
			player.rank = 7
			high_card(temp, player)
		elif pcount >= 2:
			player.rank = 2
			high_card(temp, player)
		elif trips == True:
			player.rank = 6
			high_card(temp, player)
		else:
			player.rank = 1
			high_card(temp, player)	

	if trips == True:
		if pair == False:
			player.rank = 3
			high_card(temp, player)

class player:
	def __init__(self):
		self.hand = []
		self.rank = 0 
		self.hcard = 0 
		self.kicker = 0 

new = player()
new.hand = ['s', 13, 'c', 3]
board = ['d', 13, 's', 13, 's', 3, 's', 3, 'd', 9]

x = hand_data(new.hand, board)
y = get_rank(x, new)

print(new.rank)

