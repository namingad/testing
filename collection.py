print('hello')

from collections import namedtuple

a = namedtuple('course', 'name, department')
s = a('datascience', 'python')
print(s)

from collections import deque
#
# l = ['a', 1, 2, 3, 4]
# a = deque(l)
# print(a)
# a.append(10)
# print(a)
# a.appendleft('navya')
# print(a)
# a.popleft()
# print(a)
# a.reverse()
# print(a)

from collections import ChainMap
a ={'id': 1, 'name':'Navya'}
b = {'id':2, 'name': 'Pooja'}
c=ChainMap(a,b)
print(c)

from collections import Counter
l=[1,1,1,2,1,22,3,3,4,4,5,4,5]
a=Counter(l)
print(a)
b=a.most_common()
print(b)

from collections import OrderedDict

d= OrderedDict()
d[1]='a'
d['id']=10
d['name']='navya'
d[2]='b'
d[3]='c'
print(d)
print(type(d))
print(d.keys())
print(d.values())
print(d.get('id'))

from collections import defaultdict

d = defaultdict(int)
d[1]='name'
d[2]='Fname'
print(d[3])

def name(x,y):

    print(x+y)

name(10,20)

def default_parm(a,b,c=10):
    print(a)
    print(b)
    print(c)
default_parm(10,20)


