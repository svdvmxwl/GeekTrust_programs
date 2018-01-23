
a = {'o1':-1,'o2':-1,'w':-1,'w1':-1,'w2':-1,'w3':-1,'spU':-1}
i = {'o1':-1,'o2':-1,'w':-1,'w1':-1,'w2':-1,'w3':-1,'spU':-1}

path1 = ''
path2 = ''
sp1 = 0
sp2 = 0
weth = ''


def getinp(DT):
    s2 = input(DT)
    s2 = s2.lower()
    global k
    k = s2.split()
    j = -1

    
    global a
    global i
    
    a = {'o1':-1,'o2':-1,'w':-1,'w1':-1,'w2':-1,'w3':-1,'spU':-1}
    i = {'o1':-1,'o2':-1,'w':-1,'w1':-1,'w2':-1,'w3':-1,'spU':-1}

    global path1
    global path2
    global sp1
    global sp2
    global weth

    for wrd in k:
        j += 1
        a['o1'] = wrd.find('orbit1')
        a['o2'] = wrd.find('orbit2')
        a['w'] = wrd.find('weather')
    
        a['w1'] = wrd.find('sunny')
        a['w2'] = wrd.find('windy')
        a['w3'] = wrd.find('rainy')
    
        a['spU'] =wrd.find('megamiles/hour')
    
    
        if a['o1'] != -1:
            i['o1'] = j
        if a['o2'] != -1:
            i['o2'] = j
        if a['w'] != -1:
            i['w'] = j
        if a['w1'] != -1:
            i['w1'] = j
        if a['w2'] != -1:
            i['w2'] = j
        if a['w3'] != -1:
            i['w3'] = j
        if a['spU'] != -1:
            i['spU'] = j
        
    if i['spU'] != -1:
        if i['o1'] != -1:
            path1 = k[i['o1']]
            sp1 = k[i['spU'] - 1]
        if i['o2'] != -1:
            path2 = k[i['o2']]
            sp2 = k[i['spU'] - 1]
        if i['o1'] == -1 and i['o2'] == -1:
            path1 = path2 = 'no path'
            sp1 = sp2 = 'no limit yet'
        
    if i['w'] != -1:
        if i['w1'] != -1:
            weth = k[i['w1']]
        
        if i['w2'] != -1:
            weth = k[i['w2']]
        
        if i['w3'] != -1:
            weth = k[i['w3']]
while True:
    getinp('input weather')
    if i['w'] == -1 or i['w1'] == i['w2'] == i['w3'] == -1:
        print('Please Give Valid input')
    else:
        break
                
wthrTYP = weth

while True:
    getinp('input orbit1')
    if i['o1'] == -1 or i['spU'] == -1 or k[i['spU'] - 1].isnumeric() == False:
        print("please give valid input")
    else:
        break

Orbt1 = path1
MSP1 = int(sp1)

while True:
    getinp('input orbit2')
    if i['o2'] == -1 or i['spU'] == -1 or k[i['spU'] - 1].isnumeric() == False:
        print("please give valid input")
    else:
        break
        
Orbt2 = path2
MSP2 = int(sp2)

## wthr --> weather, Orbt --> Orbit/path, Veh --> Vehicle, Sup --> support, Prcntg --> Percent change
## Crtr --> creater, MaxSp --> Maximum allowed speed Fnl --> Final
class Wthr(object):
    
    def __init__(self,WthrTyp='',VehSup=0,prcntgCrtr=0.0):
        self.WthrTyp = WthrTyp
        self.VehSup = VehSup
        self.prcntgCrtr = prcntgCrtr
        
vehsup = 0
crttpct = 0.0        
if wthrTYP == 'rainy':
    vehsup = (0,1,1)
    crttpct = 0.200
    
if wthrTYP == 'windy':
    vehsup = (1,0,1)
    crttpct = 0.000
    
if wthrTYP == 'sunny':
    vehsup = (1,1,1)
    crttpct = -0.100
Weather = Wthr(wthrTYP,vehsup,crttpct)

prcntg = Weather.prcntgCrtr


class Orbt(object):
    global prcntg
    def __init__(self,OrbtTyp=0,MaxSp=0,Dist=0,Crtr=0):
        self.OrbtTyp = OrbtTyp
        self.MaxSp = MaxSp
        self.Dist = Dist
        self.Crtr = Crtr
        self.Crtr += prcntg * self.Crtr
        
orbit1 = Orbt(Orbt1,MSP1,18,20)
orbit2 = Orbt(Orbt2,MSP2,20,10)

class Veh(object):
    def __init__(self,VehTyp,Sp=0,TCrtr=0):
        self.VehTyp = VehTyp
        self.Sp = Sp
        self.TCrtr = TCrtr
        
Bike = Veh('bike',10,2)
Tuktuk = Veh('tuktuk',12,1)
SuCar = Veh('car',20,3)

Path = [orbit1, orbit2]
Moti = [Bike,Tuktuk, SuCar]

z1 = 0
ij = [[-1,-1,-1],[-1,-1,-1]]
for orb in [orbit1, orbit2]:
    z2 = 0
    for veh in [Bike,Tuktuk, SuCar]:
        MinMaxSp = min(veh.Sp , orb.MaxSp)
        NormTime = orb.Dist / MinMaxSp
        CrtrTime = orb.Crtr*veh.TCrtr*(1/60.00)
        ij[z1][z2] = (NormTime + CrtrTime)*Weather.VehSup[z2]
        z2 += 1
    z1 += 1
    
mini = max(max(ij[0]),max(ij[1]))
for e in range(0,2):
    for f in range(0,3):
        if ij[e][f] < mini and ij[e][f] != 0:
            mini = ij[e][f]

for e in range(0,2):
    for f in range(0,3):
        ij[e][f] = str(ij[e][f])
StrMini = str(mini)
for e in range(0,2):
    for f in range(0,3):
        l = ij[e][f].find(StrMini)
        if l == 0:
            global v1
            global v2
            v1 = e
            v2 = f
            break

print('Vehicle ' + Moti[v2].VehTyp.title() + ' on ' + Path[v1].OrbtTyp.title())
