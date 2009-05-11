count=0;
def countUp():
    count+=1
    return count

class Npc:
    '''
    NPC NPC NPC OH MAN NPC
    '''
    def __init__(self, type, x, y, hp=1.0):
        '''
        npc.init yo yo yo
        '''
        self.count = countUp;
        self.type = type
        self.x = x
        self.y = y
        self.hp = hp
    def f(self):
        ''' npc.f '''
        print('test')
    


n = Npc('lol', 1, 2)

print(n)

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for c in [B, C, D]:
    try:
        raise c()
    except D:
        print ("D")
    except C:
        print ("C")
    except B:
        print ("B")
