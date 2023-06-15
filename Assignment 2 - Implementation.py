"""
File: Assingment 2 - Implementation.py
Description: This is the assignment file: Assignment File 2: Implementation
Author: Thomas Keo
StudentID: 110349388
EmailID: KEOTY004 
This is my own work as defined by the University's Academic Misconduct Policy.  
"""

from abc import ABC

class Material(ABC):
    def __init__(self, strength):
        self.strength = strength

class Wood(Material):
    def __init__(self, strength):
        super().__init__(strength)

class Metal(Material):
    def __init__(self, strength, purity):
        super().__init__(strength)
        self.purity = purity

class Gemstone(Material):
    def __init__(self, strength, magicPower):
        super().__init__(strength)
        self.magicPower = magicPower

class Maple(Wood):
    def __init__(self, strength=5):
        super().__init__(strength)

class Ash(Wood):
    def __init__(self, strength=3):
        super().__init__(strength)

class Oak(Wood):
    def __init__(self, strength=4):
        super().__init__(strength)

class Bronze(Metal):
    def __init__(self, strength=3, purity=1.3):
        super().__init__(strength, purity)

class Iron(Metal):
    def __init__(self, strength=6, purity=1.1):
        super().__init__(strength, purity)

class Steel(Metal):
    def __init__(self, strength=10, purity=1.8):
        super().__init__(strength, purity)

class Ruby(Gemstone):
    def __init__(self, strength=1, magicPower=1.8):
        super().__init__(strength, magicPower)

class Sapphire(Gemstone):
    def __init__(self, strength=1.2, magicPower=1.6):
        super().__init__(strength, magicPower)

class Emerald(Gemstone):
    def __init__(self, strength=1.6, magicPower=1.1):
        super().__init__(strength, magicPower)

class Diamond(Gemstone):
    def __init__(self, strength=2.1, magicPower=2.2):
        super().__init__(strength, magicPower)

class Amethyst(Gemstone):
    def __init__(self, strength=1.8, magicPower=3.2):
        super().__init__(strength, magicPower)

class Onyx(Gemstone):
    def __init__(self, strength=0.1, magicPower=4.6):
        super().__init__(strength, magicPower)


"""

Class for workshop which includes has the forge and enchanter. 
This also stores everything that is required for crafting

"""
class Workshop:
    def __init__(self, forge, enchanter):
        self.enchanter = enchanter
        self.forge = forge
        self.weapons = []
        self.enchantments = []
        self.materials = {}


    """ Displays weapons that are stored in the workshop, their enchants (if they have any) and their attack damage """
    def displayWeapons(self):
        display = ''
        for weapon in self.weapons:
            if weapon.isEnchanted == True:
                display += (f"The {weapon.name} is imbued with a {weapon.enchantment.useEffect}. It deals {weapon.attack} damage.\n")
            else:
                display += (f"The {weapon.name} is not enchanted. It deals {weapon.attack} damage.\n")
        return display


    """ Displays what enchantments are stored in the workshop """
    def displayEnchantments(self):
        displayenchants = ''
        for enchantment in self.enchantments:
            displayenchants += (f"A {enchantment.name} enchantment is stored in the workshop.\n")
        return displayenchants


    """ Displays the materials and their quantities in the workshop """
    def displayMaterials(self):
        displaymats = ''
        for material, quantity in self.materials.items():
            displaymats += (f"{material}: {quantity} remaining.\n")
        return displaymats
    

    """ Appends the weapon list with the added weapon """
    def addWeapon(self, weapon):
        self.weapons.append(weapon)

    """ Removes the weapon from the weapon list """
    def removeWeapon(self, weapon):
        self.weapons.remove(weapon)
        
    
    """ Appends the enchantment list with the added enchantment """
    def addEnchantment(self, enchantments):
        self.enchantments.append(enchantments)
        

    """ Removes the enchantment from the enchantment list """
    def removeEnchantment(self, enchantment):
        self.enchantments.remove(enchantment)
       

    def addMaterial(self, material, quantity):
        if material in self.materials:
            self.materials[material] += quantity
        else:
            self.materials[material] = quantity
    
    def removeMaterial(self, material, quantity):
        if material in self.materials:
            if self.materials[material] >= quantity:
                self.materials[material] -= quantity
            else:
                raise ValueError("Not enough material available.")
        else:
            raise ValueError("Material not found in the workshop")

class Crafter(ABC):

    @classmethod
    def craft(self):
        pass

    def disassemble(self):
        pass

class Forge(Crafter):

    def __init__(self):
        pass

    def craft(self, weaponName, primaryMaterial, catalystMaterial, materials):
        weapon = Weapon(primaryMaterial, catalystMaterial)
        weapon.setName(weaponName)
        weapon.setDamage(
            weapon.calculateDamage(primaryMaterial, catalystMaterial)
        )
        if primaryMaterial.__class__.__name__ not in materials or catalystMaterial.__class__.__name__ not in materials:
            raise ValueError("Required materials not found in the workshop.")
        else:
            materials[primaryMaterial.__class__.__name__] -= 1
            materials[catalystMaterial.__class__.__name__] -= 1

        return weapon


    def disassemble(self, weapon, materials):
        primaryMaterial = weapon.getPrimaryMaterial()
        catalystMaterial = weapon.getCatalystMaterial()
        materials[primaryMaterial.__class__.__name__] += 1
        materials[catalystMaterial.__class__.__name__] += 1

        return weapon

class Enchanter(Crafter):
    def __init__(self):
        self.recipes = {
            "Holy": "pulses a blinding beam of light",
            "Lava": "melts the armour off an enemy",
            "Pyro": "applies a devastating burning effect",
            "Darkness": "binds the enemy in dark vines",
            "Cursed": "causes the enemy to become crazed",
            "Hydro": "envelops the enemy in a suffocating bubble",
            "Venomous": "afflicts a deadly, fast-acting toxin",
            "Earthly": "Earthly things"}

    def craft(self, enchantmentName, primaryMaterial, catalystMaterial, materials):
        enchantment = Enchantment(primaryMaterial, catalystMaterial)
        enchantment.setName(enchantmentName)
        enchantment.setEffect(self.recipes[enchantmentName])
        enchantment.setMagicDamage(
            enchantment.calculateMagicDamage(primaryMaterial, catalystMaterial)
        )
        materials[primaryMaterial.__class__.__name__] -= 1
        materials[catalystMaterial.__class__.__name__] -= 1
        return enchantment

    def disassemble(self, enchantment, materials):
        primaryMaterial = enchantment.getPrimaryMaterial()
        catalystMaterial = enchantment.getCatalystMaterial()
        materials[primaryMaterial.__class__.__name__] += 1
        materials[catalystMaterial.__class__.__name__] += 1
        return enchantment      

    def enchant(self, weapon, weaponName, enchantment):
        weapon.damage *= enchantment.magicDamage
        weapon.setEnchantment(enchantment)
        weapon.setEnchanted()
        weapon.name = weaponName
        return weapon

class Weapon:
    def __init__(self, primaryMaterial, catalystMaterial):
        self.__name = ''
        self.__damage = 0
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial
        self.__enchantment = None
        self.__isEnchanted = False

    def getName(self):
        return self.__name

    def getDamage(self):
        return self.__damage
    
    def getEnchanted(self):
        return self.__isEnchanted

    def getPrimaryMaterial(self):
        return self.__primaryMaterial

    def getCatalystMaterial(self):
        return self.__catalystMaterial

    def getEnchantment(self):
        return self.__enchantment

    def setName(self, name):
        self.__name = name

    def setDamage(self, damage):
        self.__damage = damage

    def setEnchanted(self):
        self.__isEnchanted = True
    
    def setEnchantment(self, enchantment):
        self.__enchantment = enchantment

    def calculateDamage(self, primaryMaterial, catalystMaterial):
        if isinstance(primaryMaterial, Wood) and isinstance(catalystMaterial, Wood):
            damage = primaryMaterial.strength * catalystMaterial.strength
        elif isinstance(primaryMaterial, Metal) and isinstance(catalystMaterial, Metal):
            damage = (primaryMaterial.strength * primaryMaterial.purity) + (catalystMaterial.strength * catalystMaterial.purity)
        elif isinstance(primaryMaterial, Wood) and isinstance(catalystMaterial, Metal):
            damage = (primaryMaterial.strength * (catalystMaterial.strength * catalystMaterial.purity))
        elif isinstance(primaryMaterial, Metal) and isinstance(catalystMaterial, Wood):
            damage = (primaryMaterial.strength * (primaryMaterial.purity * catalystMaterial.strength))
        return damage
    
    def attack(self):
        #rounded to 2 decimal places
        return round(self.__damage, 2)
    
    name = property(getName, setName)
    damage = property(getDamage, setDamage)
    isEnchanted = property(getEnchanted, setEnchanted)
    enchantment = property(getEnchantment, setEnchantment)
    attack = property(attack)

class Enchantment:
    def __init__(self, primaryMaterial, catalystMaterial):
        self.__name = ''
        self.__effect = ''
        self.__magicDamage = 0
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial

    def getName(self):
        return self.__name

    def getMagicDamage(self):
        return self.__magicDamage

    def getEffect(self):
        return self.__effect

    def getPrimaryMaterial(self):
        return self.__primaryMaterial

    def getCatalystMaterial(self):
        return self.__catalystMaterial

    def setName(self, name):
        self.__name = name

    def setMagicDamage(self, magicDamage):
        self.__magicDamage = magicDamage
    
    def setEffect(self, effect):
        self.__effect = effect

    def calculateMagicDamage(self, primaryMaterial, catalystMaterial):
        magicDamage = primaryMaterial.magicPower * primaryMaterial.strength + catalystMaterial.magicPower * catalystMaterial.strength
        return magicDamage
    
    def useEffect(self):
        return (f"{self.name} enchantment and {self.effect}")
    
    name = property(getName, setName)
    effect = property(getEffect, setEffect)
    magicDamage = property(getMagicDamage, setMagicDamage)
    useEffect = property(useEffect)

# Create a workshop, forge, enchanter.
workshop = Workshop(Forge(), Enchanter())

# Create a set of materials and lists for testing.
materials = [Maple(), Oak(), Ash(), Bronze(), Iron(), Steel(),
             Ruby(), Sapphire(), Emerald(), Diamond(), Amethyst(), Onyx()]

weaponBlueprints = {
    "Sword": [Steel(), Maple()],
    "Shield": [Bronze(), Oak()],
    "Axe": [Iron(), Ash()],
    "Scythe": [Steel(), Ash()],
    "Bow": [Oak(), Maple()],
    "Wand": [Ash(), Oak()],
    "Staff": [Bronze(), Maple()],
    "Dagger": [Bronze(), Bronze()]}

enchantmentBlueprints = {
    "Holy": [Diamond(), Diamond()],
    "Lava": [Ruby(), Onyx()],
    "Pyro": [Ruby(), Diamond()],
    "Darkness": [Onyx(), Amethyst()],
    "Cursed": [Onyx(), Onyx()],
    "Hydro": [Sapphire(), Emerald()],
    "Venomous": [Emerald(), Amethyst()],
    "Earthly": [Emerald(), Emerald()]}

enchantedWeapons = ["Holy Greatsword", "Molten Defender", "Berserker Axe", "Soul Eater",
    "Twisted Bow", "Wand of the Deep", "Venemous Battlestaff"]

# Adds a number of materials to use for crafting.
for material in materials:
    if isinstance(material, Wood):
        workshop.addMaterial(material.__class__.__name__, 20)
    elif isinstance(material, Metal):
        workshop.addMaterial(material.__class__.__name__, 10)
    else:
        workshop.addMaterial(material.__class__.__name__, 5)

print("--------------------------------Material Store--------------------------------")
print(workshop.displayMaterials())

# Crafts the following: Sword, Shield, Axe, Scythe, Bow, Wand and Staff weapons.
for weapon, materials in weaponBlueprints.items():
    craftedWeapon = workshop.forge.craft(
        weapon, materials[0], materials[1], workshop.materials)
    workshop.addWeapon(craftedWeapon)

# Disassemble the extra weapon.
workshop.removeWeapon(workshop.forge.disassemble(
    workshop.weapons[7], workshop.materials))

print("------------------------------------Armoury-----------------------------------")
print(workshop.displayWeapons())

# Crafts the following: Holy, Lava, Pyro, Darkness, Cursed, Hydro and Venomousenchantments.
for enchantment, materials in enchantmentBlueprints.items():
    craftedEnchantment = workshop.enchanter.craft(
    enchantment, materials[0], materials[1], workshop.materials)
    workshop.addEnchantment(craftedEnchantment)


# Disassemble the extra enchantment.
workshop.removeEnchantment(workshop.enchanter.disassemble(
    workshop.enchantments[7], workshop.materials))

print("------------------------------------Enchantments------------------------------------")
print(workshop.displayEnchantments())

print("-----------------------------------Material Store-----------------------------------")
print(workshop.displayMaterials())

# Enchant the following weapons: Sword, Shield, Axe, Scythe, Bow, Wand and Staff.
for i in range(len(enchantedWeapons)):
    workshop.enchanter.enchant(
        workshop.weapons[i], enchantedWeapons[i], workshop.enchantments[i])

print("-----------------------------------Enchanted Armoury----------------------------------")
print(workshop.displayWeapons())