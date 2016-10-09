import math
import csv
def data_extract():
	with open('data.csv','r') as d:
		reader = csv.DictReader(d)
		p = []
		table = []
		for row in reader:
			p.append(row['education_level'])
			p.append(row['career'])
			p.append(row['years_of_experience'])
			p.append(row['location'])
			p.append(row['salary'])
			table.append(p)
			p = []
	return table
def detail(table,i):
	label = lab(table,-1)
	feature = lab(table,i)
	re = []
	for fe in feature:
		for judge in label:
			be = [fe,judge,0]
			for item in table:
				if(item[i] == fe) and (item[-1] == judge):
					be[2] = be[2] + 1
			re.append(be)
	return re
def lab(table,i):
	container = []
	for a in table:
		container.append(a[i])
	return list(set(container))
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
# (salary,label) = detail(data_extract(),4)
# total = salary[0][1] + salary[1][1]
# print salary
# print label,total

a = detail(data_extract(),1)
s = [[a[0][2],(a[0][2]+a[1][2])],[a[2][2],a[2][2]+a[3][2]]]
gain(s)



# se = [[3,6],[4,6],[1,5]]
# gen = [[5,8],[3,7],[0,2]]
# qiao = [[6,10],[2,5],[0,2]]
# wen = [[7,9],[1,5],[0,3]]
# qi = [[5,7],[3,6],[0,4]]
# chu = [[6,12],[2,5]]
# second_se = [[3,4],[3,4],[1,1]]
# gain(second_se)