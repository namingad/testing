



x=['hi','python','hi','nav','we','i','hi','python']
y={}

for i in x:
    if i in y.keys():
        y[i]=y[i]+1
    else:
        y[i]=1
print(y)

#addint these list elements to tuple
print("#############")
x=['a','b','c','d']
y=[10,20,30,40]
z=tuple(zip(x,y))
print(z)


#creating tuple within list and printing values present in the 1 index value in anoother list
print("######################")
x=[('a',10),('b',20),('c',30),('d',40)]
y=[]
for i in range(len(x)):
    y.append(x[i][1])
print(y)

#adding two list elements to dictionary
print("###############")
x=['a','b','c','d']
y=[10,20,30,40]
d=dict(zip(x,y))
print(d)

#adding adjectives in another and printinng positive if it contains more good and printing negative if it contains more negative
print("#################")
x= [('hi','noun'),('good','adj'),('run','verb'),('bad','adj'),('good','adj')]
y=[]
for i,j in x:
    if j=='adj':
        y.append(i)
print(y)
if y.count('good')> y.count('bad'):
    print('Positivity')
elif y.count('good')<y.count('bad'):
    print('Negativity')



a=[10,20,30,40,50,60]
for i in range(0,len(a)):
    print(a[i])





