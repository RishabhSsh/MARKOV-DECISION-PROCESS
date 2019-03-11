# discount factor
def check(i,j):
	if i < 0 or j < 0 or i>=n or j>=m : 
		return 0
	else: 
		return 1


df = 0.99

n, m = raw_input().split()
n = int(n)
m = int(m)
start_states = [0 for i in range(2)]
matrix = [[0 for j in range(m)]for i in range(n)]
state = [[0 for j in range(m)]for i in range(n)]
value = [[0 for j in range(m)]for i in range(n)]
for i in range(n):
	j = 0
	for k in raw_input().split():
		matrix[i][j] = float(k)
		j += 1

e, w = raw_input().split()
e = int(e)
w = int(w)

for i in range(e):
	a, b = [int(k) for k in raw_input().split()]
	a -= 1
	b -= 1
	state[a][b] = 1  # end states

for i in range(w):
	a, b = [int(k) for k in raw_input().split()]
	a -= 1
	b -= 1
	state[a][b] = 2  # walls

i = 0
for k in raw_input().split():
	start_states[i] = int(k)
	i += 1

state[start_states[0]][start_states[1]] = 3  # start state

unit_steps_reward = float(raw_input())
count = 0
while(1):
	count += 1
	delt = -100000000
	for i in range(n):
		for j in range(m):
			if state[i][j] == 2 or state[i][j] == 1:
				continue
			v = value[i][j]
			vv = -100000000
			sum1 = 0
			if check(i+1, j):
		   		sum1 += 0.8*(unit_steps_reward + matrix[i][j] + df*value[i+1][j])
		   	if check(i, j+1):
		   		sum1 += 0.1*(unit_steps_reward + matrix[i][j] + df*value[i][j+1])
		   	if check(i, j-1):
		   		sum1 += 0.1*(unit_steps_reward + matrix[i][j] + df*value[i][j-1])
		   	vv=max(vv, sum1)

			sum1 = 0
			if check(i-1,j) :
		   		sum1 += 0.8*(unit_steps_reward + matrix[i][j] + df*value[i-1][j])
		   	if check(i,j+1) :
		   		sum1 += 0.1*(unit_steps_reward + matrix[i][j] + df*value[i][j+1])
		   	if check(i,j-1) :
		   		sum1 += 0.1*(unit_steps_reward + matrix[i][j] + df*value[i][j-1])
		   	vv=max(vv,sum1)


			sum1 = 0
			if check(i,j+1) :
		   		sum1 += 0.8*(unit_steps_reward + matrix[i][j] + df*value[i][j+1])
		   	if check(i-1,j) :
		   		sum1 += 0.1*(unit_steps_reward + matrix[i][j] + df*value[i-1][j])
		   	if check(i+1,j) :
		   		sum1 += 0.1*(unit_steps_reward + matrix[i][j] + df*value[i+1][j])


			sum1 = 0
			if check(i,j-1) :
		   		sum1 += 0.8*(unit_steps_reward + matrix[i][j] + df*value[i][j-1])
		   	if check(i-1,j) :
		   		sum1 += 0.1*(unit_steps_reward + matrix[i][j] + df*value[i-1][j])
		   	if check(i+1,j) :
		   		sum1 += 0.1*(unit_steps_reward + matrix[i][j] + df*value[i+1][j])

		   	vv =max(vv,sum1)
		   	delt = max(delt,abs(vv-value[i][j]))
		   	value[i][j] = vv


	print("----------count: "+str(count)+"\n")
	for i in range(n):
		for j in range(m):
			print(round(value[i][j],3) )
		print "\n"

	if delt < 1.98:
		break




