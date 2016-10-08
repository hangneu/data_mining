import math
def ent(yes,t):
	if yes == 0 or (t-yes)==0:
		return 0
	else:
		yes = yes * 1.0
		yes_p = (yes/t)*math.log((yes/t),2)
		no_p = ((t-yes)/t)*math.log(((t-yes)/t),2)
		total = -1*(yes_p + no_p)
		return total
def gain(data):
	a = []
	entropy = 0
	yes = 0
	t = 0
	for d in data:
		a.append([ent(d[0],d[1]),d[1]])
		yes = yes + d[0]
		t= t + d[1]
	root = [ent(yes,t),t]
	for item in a:
		entropy = entropy + item[0]*item[1]/root[1]
	information_gain = root[0] - entropy
	print information_gain
b = [[3,6],[4,6],[1,5]]
# gain(b)
a = [[5,8],[3,7],[0,2]]
gain(a)

