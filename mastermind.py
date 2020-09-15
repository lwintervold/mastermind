import argparse
import random

from typing import Tuple

COLORS = 'RGBYPOACDEFHIJKLMNQSTUVWXZ'

def compareStates(
	statei : str,
	statej : str
	) -> Tuple[int, int]:

	# Mismatches
	mismatchi = {}
	mismatchj = {}

	# Match count
	matches = 0
	for (ci, cj) in zip(statei, statej):
		if ci == cj:
			matches += 1
		else:
			if ci not in mismatchi:
				mismatchi[ci] = 1
			else:
				mismatchi[ci] += 1
			if cj not in mismatchj:
				mismatchj[cj] = 1
			else:
				mismatchj[cj] += 1

	# Find number of rearrangeable matches
	rearrangeable = 0
	for ci in mismatchi:
		if ci in mismatchj:
			rearrangeable += min(mismatchi[ci], mismatchj[ci])
	return (matches, rearrangeable)

def play(
	symbolcount : int,
	colorcount : int
	):
	
	# Generate goal
	goal = ''.join([COLORS[:colorcount][random.randint(0, colorcount - 1)] for x in range(symbolcount)])

	colorset = COLORS[:colorcount]
	solved = False
	while not solved:

		valid = False
		while not valid:
			raw = input('Enter your guess:')
			if len(raw) != symbolcount or any([c not in colorset for c in raw]):
				print('Bad input.')
			else:
				valid = True
		compare = compareStates(raw, goal)
		if compare == (symbolcount, 0):
			solved = True
		else:
			print('Result:', compare)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Mastermind solver')
	subparsers = parser.add_subparsers(dest='command')

	playparser = subparsers.add_parser('play')
	playparser.add_argument('symbolcount', type=int, help='Number of symbols')
	playparser.add_argument('colorcount', type=int, help='Number of colors')

	playparser = subparsers.add_parser('solve')
	playparser.add_argument('symbols', help='Input symbols')
	playparser.add_argument('colorcount', type=int, help='Number of colors')

	args = parser.parse_args()
	dictargs = vars(args)

	if dictargs['command'] == 'play':
		play(dictargs['symbolcount'], dictargs['colorcount'])
	elif dictargs['command'] == 'solve':
		solve()