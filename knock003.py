input ='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
split_str=[]
pi=[]
print input

input=input.replace(',','').replace('.','');
split_str=input.split(' ')
for s in split_str:
     pi.append(len(s))

print pi
