from math import sqrt, pi, cos, sin

depth = 0
maxDepth = 2
done = False
turns = []

def winCheck(pos):
	if pos == [0,0]:
		print('done')
		print('depth =', depth)
		return True
	# print('Not at origin')
	return False

def move(mPos, turn, angle, step):
	newPos = [mPos[0] + step*cos(angle), mPos[1] + step*sin(angle)]
	newAngle = angle + turn*pi/4
	# print(newPos)
	return [newPos, newAngle]

def recurse(pos, angle):
	global depth, done, turns
	depth += 1
	# oldPos, oldAngle = pos, angle
	if not depth == maxDepth and not done:
		for turn in [-1,1]:
			newState = move(pos, turn, angle, depth)
			turns.append(turn)
			recurse(newState[0], newState[1])
			turns.pop()
	depth -= 1

	# pos, angle = oldPos, oldAngle
	if winCheck(pos) and not depth == 0 :
		done = True
		print(turns)

while not done:
	recurse([0,0], 0)
	print('not at depth', maxDepth)
	maxDepth += 1
print(maxDepth)


def endstate(turnSequence):
	global depth
	pos = [0,0]
	angle = 0
	for turn in turnSequence:
		depth += 1
		print(pos, ',', angle/pi)
		newState = move(pos, turn, angle, depth)
		pos, angle = newState[0], newState[1]

	print(pos, ',', angle/pi)


# mTurnSequence = [-1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1]

# endstate([1,1,1])

# state = [[0,0], 0]
# for i in range(10):
# 	print(state)
# 	state = move(state[0], -1, state[1], i+1)
