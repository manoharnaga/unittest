import unittest

from king import King
from buildings import Hut, Cannon, Wall, TownHall, WizardTower
from village import createVillage

class TestKingAttackTarget(unittest.TestCase):
    def setUp(self):
        """
        troops is actually buildings
        """
        self.V_levels = [createVillage(1),createVillage(2),createVillage(3)]
        self.King = King((0,0))
        troops = []
        for V in self.V_levels:
            hut_obj = Hut((6,11),V)
            cannon_obj = Cannon((10,22),V)
            wall_obj = Wall((3,11),V)
            townhall_obj = TownHall((6,16),V)
            wizardttower_obj = WizardTower((17,27),V)
            troops.extend([hut_obj,cannon_obj,wall_obj,townhall_obj,wizardttower_obj])
        self.troops = troops
    # def test_attack_target_params1(self):
    #     """ params are null/None """
    #     self.assertEqual(self.King.attack_target(None,10), -1, "incorrect troop input")
    # def test_attack_target_params2(self):
    #     """ params are null/None """
    #     self.assertEqual(self.King.attack_target(self.hut_obj,None), -1, "incorrect attack input")

    # def test_attack_target_normal_reduce_health(self):
    #     """
    #     Check if King attacks normally when alive and reduces health of troops
    #     """
    #     for troop in self.troops:
    #         before_troop_health = troop.health
    #         self.King.attack_target(troop,-troop.health)
    #         self.assertEqual((troop.health > before_troop_health and (not troop.destroyed)), True, "wrong destroy condition")

    # def attack_target(self, target, attack):
    #     if(self.alive == False):
    #         return
    #     target.health -= attack
    #     if target.health <= 0:
    #         target.health = 0
    #         target.destroy()

    def test_attack_target_health_check1(self):
        """
        target.health - wrong inequality check to destroy
        wrong attack happening
        """
        for troop in self.troops:
            self.King.attack_target(troop,troop.health)
            self.assertEqual(troop.destroyed and (troop.health==0), True, "wrong destroy condition (or) attack code")
    
    def test_attack_target_health_check2(self):
        """
        target.health < 0 -> destroy the troop
        """
        for troop in self.troops:
            self.King.attack_target(troop,troop.health+1)
            self.assertEqual(troop.destroyed and (troop.health==0), True, "target.health < 0 -> destroy the troop")
    
    def test_attack_target_health_check3(self):
        """
        target.health > 0 -> shouldn't destroy the troop
        """
        for troop in self.troops:
            self.King.attack_target(troop,troop.health-1)
            self.assertEqual(troop.health > 0, True,"target.health > 0 -> shouldn't destroy the troop")
            self.assertEqual(troop.destroyed, False, "target.health > 0 -> shouldn't destroy the troop")
    
    def test_attack_target_alive(self):
        """
        King is dead, check if it still destroys the target.
        """
        self.King.alive = False
        for troop in self.troops:
            self.King.attack_target(troop,troop.health)
            self.assertEqual(troop.destroyed, False, "King dead but still target destroyed")

suite = unittest.TestLoader().loadTestsFromTestCase(TestKingAttackTarget)
result = unittest.TestResult()
suite.run(result)
if (len(result.failures) == 0) and (len(result.errors) == 0):
    with open('output_bonus.txt', 'w') as file:
        file.write('True')
else:
    with open('output_bonus.txt', 'w') as file:
        file.write('False')
