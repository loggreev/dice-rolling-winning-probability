# https://rosettacode.org/wiki/Dice_game_probabilities

# Two players have a set of dice each. The first player has nine dice with four faces each, with numbers one to four. The second player has six normal dice with six faces each, each face has the usual numbers from one to six.
# They roll their dice and sum the totals of the faces. The player with the highest total wins (it's a draw if the totals are the same). What's the probability of the first player beating the second player?
# Later the two players use a different set of dice each. Now the first player has five dice with ten faces each, and the second player has six dice with seven faces each. Now what's the probability of the first player beating the second player?

import random
import re

def main():
	print('*** Dice rolling winning probability program ***')
	print('In this program, the chance of winning a game of dice rolls is approximated.')
	print('Each player has a given number of dice each with a given number of faces.')
	print('A given number of trials are performed which roll these dice that many times.')
	print('The higher the number of trials, the more accurate the result will be.')
	print('A player wins a trial if they have the higher sum of their dice rolls.')
	print('For example, if the Player 1 rolls a total of 10 and Player 2 rolls a total of 12, Player 2 wins the trial.')
	print('Once all the trials have been performed, the percentage of a player winning is calculated.')
	print()
	
	# player_count = get_int('How many players? ', min = 2)
	# print()
	player_count = 2
	
	gameloop = True
	while gameloop:
		num_trials = get_int('How many trials should be performed? ', min = 1)
		print()
		
		if player_count == 2:
			#p1, p2, tie
			wins = [0,0,0]
		else:
			wins = None
		
		players = []
		for p in range(player_count):
			die_count = get_int(f'How many dice should Player {p+1} have? ', min = 1)
			face_count = get_int(f'How many faces should Player {p+1}\'s dice have? ', min = 2)
			players.append(Player(die_count, face_count))
			print()

		for a in range(num_trials):

			totals = []
			for i, p in enumerate(players):
				p.roll_dice()
				total = sum(p.last_rolls)
				totals.append(total)

			#the winner is the player with the greatest average total
			winner_index = totals.index(max(totals))
			winner = players[winner_index]
			
			if wins is not None:
				if totals[0] == totals[1]:
					wins[2] += 1
				else:
					wins[winner_index] += 1
					
		win_chance = [win / num_trials for win in wins]
		
		print(f'Player 1 has a win chance of about {win_chance[0]*100}%.')
		print(f'Player 2 has a win chance of about {win_chance[1]*100}%.')
		print(f'The chance of of a tie is about {win_chance[2]*100}%.')
		
		gameloop = play_again_prompt()

class Player:
	def __init__(self, die_count, face_count):
		self.die_count = die_count
		self.face_count = face_count
		self.last_rolls = None
	
	#rolls each dice the player has once
	#updates {last_rolls} to the roll results
	def roll_dice(self):
		self.last_rolls = []
		for i in range(self.die_count):
			roll = random.randint(1, self.face_count)
			self.last_rolls.append(roll)
		
#asks user for a valid integer
def get_int(message, min = None, max = None):
	while True:
		try:
			n = int(input(message))
			if min and n < min:
				raise ValueError
			if max and n > max:
				raise ValueError
			return n
		except ValueError:
			print('Please enter a valid integer.')
			
# asks user if they want to play again
# returns their answer
def play_again_prompt():
	while True:
		keep_playing_input = input('Keep playing? (y/n) ');
		if re.search('^y(es)?$', keep_playing_input, re.IGNORECASE):
			print('Starting new game...')
			print()
			return True
		elif re.search('n(o)?$', keep_playing_input, re.IGNORECASE):
			print('Thanks for playing!')
			print()
			return False
		else:
			print('Invalid input.')
			continue
		
main()