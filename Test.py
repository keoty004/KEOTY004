"""
File: Assingment 2 - Implementation.py
Description: This is a test file to test the code
Author: Thomas Keo
StudentID: 110349388
EmailID: KEOTY004 
This is my own work as defined by the University's Academic Misconduct Policy.  
"""

import unittest
from Assignment2 import *


class TestWorkshop(unittest.TestCase):
    
    def setUp(self): 
        self.workshop = Workshop(Forge(), Enchanter())
        self.enchantment = Enchantment(Diamond(), Diamond())
        self.weapon = Weapon(Maple(), Bronze())
        self.workshop.addWeapon(self.weapon)
        self.workshop.addEnchantment(self.enchantment)
        self.workshop.addMaterial('Maple', 1)
        self.material = 'Maple'

    def testAddWeapons(self):
        self.assertIn(self.weapon, self.workshop.weapons)
    
    def testRemoveWeapons(self):
        self.workshop.removeWeapon(self.weapon)
        self.assertNotIn(self.weapon, self.workshop.weapons)

    def testAddEnchantments(self):
        self.assertIn(self.enchantment, self.workshop.enchantments)
    
    def testRemoveEnchantments(self):
        self.workshop.removeEnchantment(self.enchantment)
        self.assertNotIn(self.enchantment, self.workshop.weapons)

    def testAddMaterials(self):
        self.assertIn(self.material, self.workshop.materials)

    def testRemoveMaterials(self):
        self.workshop.removeMaterial(self.material, 1)
        self.assertEqual(self.workshop.materials, {'Maple':0})

    def testDisplayMaterials(self):
        self.assertEqual(self.workshop.displayMaterials(), "Maple: 1 remaining.\n")

    def testDisplayWeapon(self):      
        self.weapon.name = 'Sword'
        self.weapon.damage = 90.0
        self.assertEqual(self.workshop.displayWeapons(), "The Sword is not enchanted. It deals 90.0 damage.\n")

    def testDisplayEnchantments(self):
        self.enchantment.name = 'Holy'
        self.assertEqual(self.workshop.displayEnchantments(), "A Holy enchantment is stored in the workshop.\n")

class TestForge(unittest.TestCase):
        
    def setUp(self): 
        self.forge = Forge()
        self.workshop = Workshop(Forge(), Enchanter())
        self.enchantment = Enchantment(Diamond(), Diamond())
        self.weapon = Weapon(Maple(), Bronze())
        self.workshop.addMaterial('Maple', 1)
        self.workshop.addMaterial('Bronze', 1)
        self.forge.craft(self.weapon, Maple(), Bronze(), self.workshop.materials)


    def testCraft(self):
        self.assertEqual(self.workshop.displayMaterials(), 'Maple: 0 remaining.\nBronze: 0 remaining.\n')
        self.assertIsInstance(self.weapon, Weapon)
        
    def testDisassemble(self):
        self.forge.disassemble(self.weapon, self.workshop.materials)
        self.assertEqual(self.workshop.displayMaterials(), 'Maple: 1 remaining.\nBronze: 1 remaining.\n')

class TestEnchanter(unittest.TestCase):
        
    def setUp(self): 
        self.enchanter = Enchanter()
        self.workshop = Workshop(Forge(), Enchanter())
        self.enchantment = Enchantment(Diamond(), Diamond())
        self.enchantment.name = 'Holy'
        self.weapon = Weapon(Maple(), Bronze())
        self.workshop.addWeapon(self.weapon)
        self.workshop.addEnchantment(self.enchantment)
        self.workshop.addMaterial('Diamond', 2)
        self.enchanter.craft(self.enchantment.name, Diamond(), Diamond(), self.workshop.materials)


    def testCraft(self):
        self.assertEqual(self.workshop.displayMaterials(), 'Diamond: 0 remaining.\n')
        self.assertIsInstance(self.enchantment, Enchantment)
        
    def testDisassemble(self):
        self.enchanter.disassemble(self.enchantment, self.workshop.materials)
        self.assertEqual(self.workshop.displayMaterials(), 'Diamond: 2 remaining.\n')
    
    def testEnchant(self):
        self.enchanter.enchant(self.weapon, 'Holy Greatsword', self.enchantment)

        # self.weapon.enchantment.useEffect = 'pulses a blinding beam of light'
        self.enchantment.effect = 'pulses a blinding beam of light'
        self.weapon.damage = 831.6
        self.assertEqual(self.workshop.displayWeapons(), 'The Holy Greatsword is imbued with a Holy enchantment and pulses a blinding beam of light. It deals 831.6 damage.\n')

class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.foge = Forge()
        self.workshop = Workshop(Forge(), Enchanter())
        self.enchantment = Enchantment(Diamond(), Diamond())
        self.weapon = Weapon(Maple(), Bronze())
        self.workshop.addWeapon(self.weapon)

    def testCalculateDamage(self):
        self.assertEqual(self.weapon.calculateDamage(Maple(), Bronze()), 19.5)
    
    def testAttack(self):
        self.weapon.damage = 19.4324
        self.assertEqual(self.weapon.attack, 19.43)

class TestEnchantment(unittest.TestCase):
    def setUp(self):
        self.foge = Forge()
        self.workshop = Workshop(Forge(), Enchanter())
        self.enchantment = Enchantment(Diamond(), Diamond())
        self.weapon = Weapon(Maple(), Bronze())
        self.workshop.addWeapon(self.weapon)

    def testCalculateDamage(self):
        self.assertEqual(self.enchantment.calculateMagicDamage(Sapphire(), Emerald()), 3.68)
    
    def testUseEffect(self):
        self.enchantment.name = 'Holy'
        self.enchantment.effect = 'pulses a blinding beam of light'
        self.assertEqual(self.enchantment.useEffect, 'Holy enchantment and pulses a blinding beam of light')

unittest.main()

