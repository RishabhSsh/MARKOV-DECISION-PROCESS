# discount factor

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
		value[i][j]=matrix[i][j]
		j += 1

e, w = raw_input().split()
e = int(e)
w = int(w)

for i in range(e):
	a, b = [int(k) for k in raw_input().split()]
	state[a][b] = 1  # end states

for i in range(w):
	a, b = [int(k) for k in raw_input().split()]
	state[a][b] = 2  # walls

i = 0
for k in raw_input().split():
	start_states[i] = int(k)
	i += 1

state[start_states[0]][start_states[1]] = 3  # start state

unit_steps_reward = float(raw_input())
count = 0
cont=1
def check(i,j):

	if i < 0 or j < 0 or i>=n or j>=m : 
		return 0
	else: 
		if state[i][j] == 2 :
			return 0
		
	return 1

while(cont):
	count += 1
	cont = 0
	for i in range(n):
		for j in range(m):
			delt = 0
			if state[i][j] == 2 or state[i][j] == 1:
				continue
			vv = -100000000
			sum1 = unit_steps_reward 
			if check(i+1, j):
		   		sum1 += 0.8*(df*value[i+1][j])
		   	else:
		   		sum1 += 0.8*(df*value[i][j])
		   	if check(i, j+1):
		   		sum1 += 0.1*(df*value[i][j+1])
		   	else:
		   		sum1 += 0.1*(df*value[i][j])
		   	if check(i, j-1):
		   		sum1 += 0.1*(df*value[i][j-1])
		   	else:
		   		sum1 += 0.1*(df*value[i][j])
		   	vv=max(vv, sum1)
 
			sum1 = unit_steps_reward 
			if check(i-1,j) :
		   		sum1 += 0.8*( df*value[i-1][j])
		   	else:
		   		sum1 += 0.8*( df*value[i][j])
		   	if check(i,j+1) :
		   		sum1 += 0.1*( df*value[i][j+1])
		   	else:
		   		sum1 += 0.1*( df*value[i][j])
		   	if check(i,j-1) :
		   		sum1 += 0.1*( df*value[i][j-1])
		   	else:
		   		sum1 += 0.1*( df*value[i][j])
		   	vv=max(vv,sum1)


			sum1 = unit_steps_reward 
			if check(i,j+1) :
		   		sum1 += 0.8*( df*value[i][j+1])
		   	else:
		   		sum1 += 0.8*( df*value[i][j])
		   	if check(i-1,j) :
		   		sum1 += 0.1*( df*value[i-1][j])
		   	else:
		   		sum1 += 0.1*( df*value[i][j])
		   	if check(i+1,j) :
		   		sum1 += 0.1*( df*value[i+1][j])
		   	else:
		   		sum1 += 0.1*( df*value[i][j])

		   	vv=max(vv,sum1)


			sum1 = unit_steps_reward 
			if check(i,j-1) :
		   		sum1 += 0.8*(df*value[i][j-1])
		   	else:
		   		sum1 += 0.8*(df*value[i][j])
		   	if check(i-1,j) :
		   		sum1 += 0.1*(df*value[i-1][j])
		   	else:
		   		sum1 += 0.1*(df*value[i][j])
		   	if check(i+1,j) :
		   		sum1 += 0.1*(df*value[i+1][j])
		   	else:
		   		sum1 += 0.1*(df*value[i][j])

		   	vv =max(vv,sum1)
		   	delt = max(delt,abs(vv-value[i][j]))

		   	if delt > abs(0.01*value[i][j]):
		   		cont = 1
		   	value[i][j] = vv




	print("----------count: "+str(count)+"\n")
	print('\n'.join(['\t'.join(['{:4}'.format(round(item,3)) for item in row]) for row in value]))

	print("\n")






