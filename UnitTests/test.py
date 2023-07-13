import unittest

from king import King
from village import createVillage
import points as pt

class TestKingMove(unittest.TestCase):
    def setUp(self):
        self.V = createVillage(1)
        self.King = King([16,34])
        pt.HERO_POS = [16,34]

    def test_move_dead(self):
        """
        checking if dead king move's
        """
        self.King.alive = False
        temp_position = [self.King.position[0]-1,self.King.position[1]]
        self.King.facing = 'down'
        self.King.move('up',self.V)
        self.assertEqual((self.King.facing=='up') or (self.King.position==temp_position) or (pt.HERO_POS==temp_position),False,"dead king moves")
    
    def test_move_on_normal_blank(self):
        """
        move in all directions
        """
        directions = ['up','down','left','right']
        blank_pos = [[3,4],[11,17]]
        vals = [[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(0,len(directions)):
            for j in range(0,len(directions)):
                if i!=j:
                    for blpos in blank_pos:
                        self.King.position = [blpos[0]-vals[j][0],blpos[0]-vals[j][1]]
                        pt.HERO_POS = [blpos[0]-vals[j][0],blpos[0]-vals[j][1]]
                        self.King.facing = directions[i]
                        temp_position = [self.King.position[0]+vals[j][0],self.King.position[1]+vals[j][1]]

                        self.King.move(directions[j],self.V)
                        self.assertEqual((self.King.facing==directions[j]) and (self.King.position==temp_position) and (pt.HERO_POS==temp_position),True,"direction move error")
        
    def test_move_on_normal_spawn(self):
        """
        move on spawn
        """
        directions = ['up','down','left','right']
        vals = [[-1,0],[1,0],[0,-1],[0,1]]
        spawn_pos = [[17,0],[0,35]]
        for i in range(0,len(directions)):
            for j in range(0,len(directions)):
                if i!=j:
                    if (directions[j]=='up') or (directions[j]=='right'):
                        self.King.position = [spawn_pos[0][0]-vals[j][0],spawn_pos[0][1]-vals[j][1]]
                        pt.HERO_POS = [spawn_pos[0][0]-vals[j][0],spawn_pos[0][1]-vals[j][1]]
                        self.King.facing = directions[i]
                        temp_position = [self.King.position[0]+vals[j][0],self.King.position[1]+vals[j][1]]

                        self.King.move(directions[j],self.V)
                        self.assertEqual((self.King.facing==directions[j]) and (self.King.position==temp_position) and (pt.HERO_POS==temp_position),True,"can't move on spawn and blank")
                    elif (directions[j]=='left') or (directions[j]=='down'):
                        self.King.position = [spawn_pos[1][0]-vals[j][0],spawn_pos[1][1]-vals[j][1]]
                        pt.HERO_POS = [spawn_pos[1][0]-vals[j][0],spawn_pos[1][1]-vals[j][1]]
                        self.King.facing = directions[i]
                        temp_position = [self.King.position[0]+vals[j][0],self.King.position[1]+vals[j][1]]

                        self.King.move(directions[j],self.V)
                        self.assertEqual((self.King.facing==directions[j]) and (self.King.position==temp_position) and (pt.HERO_POS==temp_position),True,"can't move on spawn and blank")

    def test_move_on_buildings(self):
        """
        move on buildings
        """
        directions = ['up','down','left','right']
        vals = [[-1,0],[1,0],[0,-1],[0,1]]
        buildings = [[6,11],[10,22],[3,11],[6,16],[17,27]]
        for i in range(0,len(directions)):
            for j in range(0,len(directions)):
                if i!=j:
                    for b_pos in buildings:
                        self.King.position = [b_pos[0]-vals[j][0],b_pos[1]-vals[j][1]]
                        pt.HERO_POS = [b_pos[0]-vals[j][0],b_pos[1]-vals[j][1]]
                        self.King.facing = directions[i]
                        temp_position = self.King.position.copy()

                        self.King.move(directions[j],self.V)
                        self.assertEqual((self.King.facing==directions[j]) and (self.King.position==temp_position) and (pt.HERO_POS==temp_position),True,"move on buildings")
    
    def test_move_after_boundaries(self):
        """
        move after boundaries
        """
        directions = ['up','down','left','right']
        vals = [[-1,0],[1,0],[0,-1],[0,1]]
        # boundaries = [[0,0],[17,35]]
        for i in range(0,len(directions)):
            for j in range(0,len(directions)):
                if i!=j:
                    if (directions[j]=='down') or (directions[j]=='right'):
                        self.King.position = [17,35]
                        pt.HERO_POS = [17,35]
                        self.King.facing = directions[i]
                        temp_position = self.King.position.copy()

                        self.King.move(directions[j],self.V)
                        self.assertEqual((self.King.facing==directions[j]) and (self.King.position==temp_position) and (pt.HERO_POS==temp_position),True,"move on boundaries down,right")
                    elif (directions[j]=='up') or (directions[j]=='left'):
                        self.King.position = [0,0]
                        pt.HERO_POS = [0,0]
                        self.King.facing = directions[i]
                        temp_position = self.King.position.copy()

                        self.King.move(directions[j],self.V)
                        self.assertEqual((self.King.facing==directions[j]) and (self.King.position==temp_position) and (pt.HERO_POS==temp_position),True,"move on boundaries up,left")
    
    def test_move_inequalities(self):
        """
        move up/left
        """
        directions = ['up','down','left','right']
        vals = [[-1,0],[1,0],[0,-1],[0,1]]
        # boundaries = [[0,0],[17,35]]
        for i in range(0,len(directions)):
            for j in range(0,len(directions)):
                if i!=j:
                    if directions[j]=='up':
                        self.King.position = [1,0]
                        pt.HERO_POS = [1,0]
                        self.King.facing = directions[i]
                        temp_position = self.King.position.copy()
                        temp_position[0] -= 1

                        self.King.move(directions[j],self.V)
                        self.assertEqual((self.King.facing==directions[j]) and (self.King.position==temp_position) and (pt.HERO_POS==temp_position),True,"move up")
                    elif directions[j]=='left':
                        self.King.position = [0,1]
                        pt.HERO_POS = [0,1]
                        self.King.facing = directions[i]
                        temp_position = self.King.position.copy()
                        temp_position[1] -= 1

                        self.King.move(directions[j],self.V)
                        self.assertEqual((self.King.facing==directions[j]) and (self.King.position==temp_position) and (pt.HERO_POS==temp_position),True,"move left")


suite = unittest.TestLoader().loadTestsFromTestCase(TestKingMove)
result = unittest.TestResult()
suite.run(result)
if (len(result.failures) == 0) and (len(result.errors) == 0):
    with open('output.txt', 'w') as file:
        file.write('True')
else:
    with open('output.txt', 'w') as file:
        file.write('False')
