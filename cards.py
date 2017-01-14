import random
import sys  
import time

class deck:
	def __init__(self):
		self.dictionary = {'s': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 'h': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 
				'd': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 'c': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]}
		self.suites = ['s', 'h', 'd', 'c'] 

face = ['J', 'Q', 'K', 'A']

def deal(hand, cards):
	count = 0 
	for i in cards.suites:
		if len(cards.dictionary[i]) == 0:
			del cards.dictionary[i]
			cards.suites.remove(i)	
	
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
			if i not in hand:
				player.kicker = i
				count += 1  
			if i in hand:
				player.hcard = i
		if count == 2:
			player.hcard = hand[0]
			if l[0] > l[1]:
				player.kicker = l[0]
			else:
				player.kicker = l[1]
	
	if player.rank == 2:
		for i in hand:
			if i > x:
				x = i 
		player.hcard = x
	if player.rank == 5:
		x = 0 
		for i in hand:
			if i > x:
				x = i  	
		player.hcard = x
		
	
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
				player.rank = 6
				high_card(dictionary[i], player)
	
	for i in suites:
		for x in dictionary[i]:
			card_value.append(x)

	if straight(card_value, len(card_value)) != None:
		player.rank = 5
		high_card(straight(card_value, len(card_value)), player)
	
	x = 0 
	count = 0
	match = [] 
	while x < len(card_value):
		for i in card_value:
			if card_value[x] == i:
				count += 1 
		if count >= 2:
			match.append(card_value[x])
		x += 1
		count = 0
	if len(match) == 2:
		player.rank = 1 
		high_card(match, player)
	if len(match) == 3:
		player.rank = 4
		high_card(match, player)
	if len(match) == 4:
		x = 0
		count = 0
		while x < 1:
			for i in match:
				if match[x] == i:
					count += 1 
			x += 1
		if count == 4:
			player.rank = 7
			high_card(match, player)
		else:
			player.rank = 2 
			high_card(match, player)
	
	if len(match) == 5:
		player.rank = 10
		high_card(match, player)

class player:
	def __init__(self):
		self.hand = []
		self.rank = 0 
		self.hcard = 0 
		self.kicker = 0 

