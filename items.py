weapons = [
    # Common Weapons
    {"name": "Rusty Sword", "rarity": "common", "type": "sword", "attack": 5, "speed": 1.0, "element": None, "effect": None, "value": 10},
    {"name": "Old Hatchet", "rarity": "common", "type": "axe", "attack": 6, "speed": 0.9, "element": None, "effect": None, "value": 12},
    {"name": "Worn Bow", "rarity": "common", "type": "bow", "attack": 4, "speed": 1.2, "element": None, "effect": None, "value": 11},
    {"name": "Training Staff", "rarity": "common", "type": "staff", "attack": 3, "speed": 1.0, "element": "arcane", "effect": None, "value": 9},
    {"name": "Broken Spear", "rarity": "common", "type": "spear", "attack": 5, "speed": 1.1, "element": None, "effect": None, "value": 10},
    {"name": "Club", "rarity": "common", "type": "blunt", "attack": 6, "speed": 0.8, "element": None, "effect": None, "value": 10},
    {"name": "Stone Dagger", "rarity": "common", "type": "dagger", "attack": 3, "speed": 1.4, "element": None, "effect": None, "value": 8},
    {"name": "Basic Wand", "rarity": "common", "type": "wand", "attack": 4, "speed": 1.0, "element": "arcane", "effect": None, "value": 10},
    {"name": "Crude Mace", "rarity": "common", "type": "blunt", "attack": 7, "speed": 0.9, "element": None, "effect": None, "value": 12},
    {"name": "Wooden Pike", "rarity": "common", "type": "spear", "attack": 5, "speed": 1.0, "element": None, "effect": None, "value": 11},

    # Rare Weapons
    {"name": "Steel Sword", "rarity": "rare", "type": "sword", "attack": 12, "speed": 1.0, "element": None, "effect": "Bleed chance", "value": 40},
    {"name": "Hunter's Longbow", "rarity": "rare", "type": "bow", "attack": 10, "speed": 1.3, "element": None, "effect": "Critical bonus", "value": 45},
    {"name": "Flame Wand", "rarity": "rare", "type": "wand", "attack": 9, "speed": 1.0, "element": "fire", "effect": "Burn chance", "value": 42},
    {"name": "War Axe", "rarity": "rare", "type": "axe", "attack": 14, "speed": 0.9, "element": None, "effect": "Armor break", "value": 48},
    {"name": "Ice Spear", "rarity": "rare", "type": "spear", "attack": 11, "speed": 1.0, "element": "ice", "effect": "Slow enemy", "value": 44},
    {"name": "Thunder Rod", "rarity": "rare", "type": "staff", "attack": 10, "speed": 1.1, "element": "lightning", "effect": "Chain damage", "value": 46},
    {"name": "Shadow Dagger", "rarity": "rare", "type": "dagger", "attack": 9, "speed": 1.5, "element": "dark", "effect": "Stealth bonus", "value": 43},
    {"name": "Iron Halberd", "rarity": "rare", "type": "spear", "attack": 13, "speed": 0.95, "element": None, "effect": "Increased reach", "value": 47},
    {"name": "Moonlight Staff", "rarity": "rare", "type": "staff", "attack": 10, "speed": 1.0, "element": "light", "effect": "Mana regen", "value": 45},
    {"name": "Barbed Flail", "rarity": "rare", "type": "blunt", "attack": 12, "speed": 0.85, "element": None, "effect": "Stun chance", "value": 50},

    # Special Weapons
    {"name": "Inferno Blade", "rarity": "special", "type": "sword", "attack": 20, "speed": 1.0, "element": "fire", "effect": "Burn + AoE", "value": 100},
    {"name": "Toxic Fang", "rarity": "special", "type": "dagger", "attack": 17, "speed": 1.4, "element": "poison", "effect": "Poison stacking", "value": 95},
    {"name": "Gale Bow", "rarity": "special", "type": "bow", "attack": 18, "speed": 1.5, "element": "wind", "effect": "Double shot", "value": 105},
    {"name": "Soul Reaver Staff", "rarity": "special", "type": "staff", "attack": 19, "speed": 1.0, "element": "dark", "effect": "Drain HP", "value": 110},
    {"name": "Crystal Hammer", "rarity": "special", "type": "blunt", "attack": 22, "speed": 0.8, "element": "ice", "effect": "Freeze + Shatter", "value": 115},

    # Legendary Weapons
    {"name": "Blade of Eternity", "rarity": "legendary", "type": "sword", "attack": 30, "speed": 1.1, "element": "light", "effect": "True strike (ignores defense)", "value": 250},
    {"name": "Riftbreaker", "rarity": "legendary", "type": "axe", "attack": 35, "speed": 0.9, "element": "void", "effect": "Rift cleave (AoE tear)", "value": 260},
    {"name": "Phoenix Talon", "rarity": "legendary", "type": "dagger", "attack": 25, "speed": 1.6, "element": "fire", "effect": "Revive once on death", "value": 270},
    {"name": "Celestial Scepter", "rarity": "legendary", "type": "staff", "attack": 28, "speed": 1.0, "element": "cosmic", "effect": "Meteor call", "value": 280},
    {"name": "Bow of the Ancients", "rarity": "legendary", "type": "bow", "attack": 26, "speed": 1.4, "element": "arcane", "effect": "Pierce all", "value": 255},
]

armors = [
    # Common Armors
    {"name": "Cloth Hood", "rarity": "common", "type": "helmet", "defense": 1, "resistance": None, "effect": None, "value": 5},
    {"name": "Worn Leather Armor", "rarity": "common", "type": "chestplate", "defense": 3, "resistance": None, "effect": None, "value": 12},
    {"name": "Tattered Robe", "rarity": "common", "type": "chestplate", "defense": 2, "resistance": "arcane", "effect": None, "value": 10},
    {"name": "Old Iron Helm", "rarity": "common", "type": "helmet", "defense": 2, "resistance": None, "effect": None, "value": 8},
    {"name": "Leather Boots", "rarity": "common", "type": "boots", "defense": 1, "resistance": None, "effect": "Slight speed boost", "value": 7},
    {"name": "Basic Chainmail", "rarity": "common", "type": "chestplate", "defense": 4, "resistance": None, "effect": None, "value": 15},
    {"name": "Ragged Pants", "rarity": "common", "type": "leggings", "defense": 1, "resistance": None, "effect": None, "value": 6},
    {"name": "Hide Vest", "rarity": "common", "type": "chestplate", "defense": 3, "resistance": "nature", "effect": None, "value": 11},
    {"name": "Bronze Greaves", "rarity": "common", "type": "leggings", "defense": 2, "resistance": None, "effect": None, "value": 9},
    {"name": "Wool Cloak", "rarity": "common", "type": "chestplate", "defense": 1, "resistance": "cold", "effect": None, "value": 8},
    
    # Rare Armors
    {"name": "Iron Breastplate", "rarity": "rare", "type": "chestplate", "defense": 7, "resistance": None, "effect": None, "value": 40},
    {"name": "Scaled Mail", "rarity": "rare", "type": "chestplate", "defense": 8, "resistance": "fire", "effect": None, "value": 44},
    {"name": "Knight’s Helm", "rarity": "rare", "type": "helmet", "defense": 5, "resistance": None, "effect": "Increased defense when low HP", "value": 38},
    {"name": "Elven Boots", "rarity": "rare", "type": "boots", "defense": 3, "resistance": "nature", "effect": "Boost evasion", "value": 36},
    {"name": "Enchanted Robes", "rarity": "rare", "type": "chestplate", "defense": 4, "resistance": "arcane", "effect": "Increased mana regen", "value": 42},
    {"name": "Frost Pants", "rarity": "rare", "type": "leggings", "defense": 5, "resistance": "ice", "effect": "Chance to slow attackers", "value": 41},
    {"name": "Darksteel Mask", "rarity": "rare", "type": "helmet", "defense": 6, "resistance": None, "effect": "Reduce crit damage", "value": 43},
    {"name": "Fireguard Greaves", "rarity": "rare", "type": "leggings", "defense": 6, "resistance": "fire", "effect": None, "value": 45},
    {"name": "Mystic Sandals", "rarity": "rare", "type": "boots", "defense": 2, "resistance": "arcane", "effect": "Increased casting speed", "value": 40},
    {"name": "Thunder Wrap", "rarity": "rare", "type": "chestplate", "defense": 5, "resistance": "lightning", "effect": "Shock reflection", "value": 48},
    
    # Special Armors
    {"name": "Dragonhide Armor", "rarity": "special", "type": "chestplate", "defense": 12, "resistance": "fire", "effect": "Immune to burn", "value": 90},
    {"name": "Ghost Shroud", "rarity": "special", "type": "chestplate", "defense": 8, "resistance": "dark", "effect": "Chance to phase attacks", "value": 95},
    {"name": "Golem Skin", "rarity": "special", "type": "leggings", "defense": 10, "resistance": "earth", "effect": "Increased knockback resistance", "value": 92},
    {"name": "Windstep Boots", "rarity": "special", "type": "boots", "defense": 4, "resistance": "wind", "effect": "Dash cooldown reduced", "value": 88},
    {"name": "Crown of Ice", "rarity": "special", "type": "helmet", "defense": 6, "resistance": "ice", "effect": "Freeze attackers on crit", "value": 94},
    
    # Legendary Armors
    {"name": "Celestial Plate", "rarity": "legendary", "type": "chestplate", "defense": 18, "resistance": "light", "effect": "Reflects 15% damage", "value": 200},
    {"name": "Helm of the Hollow King", "rarity": "legendary", "type": "helmet", "defense": 10, "resistance": "dark", "effect": "Fear aura", "value": 190},
    {"name": "Boots of Endless Step", "rarity": "legendary", "type": "boots", "defense": 6, "resistance": None, "effect": "Never slowed by terrain", "value": 185},
    {"name": "Lunar Robes", "rarity": "legendary", "type": "chestplate", "defense": 9, "resistance": "arcane", "effect": "Regain HP when casting", "value": 195},
    {"name": "Titan's Greaves", "rarity": "legendary", "type": "leggings", "defense": 12, "resistance": "earth", "effect": "Crush chance on melee", "value": 198},
]

usable_items = [
    # Common Healing & Basic Items
    {"name": "Minor Health Potion", "rarity": "common", "type": "healing", "effect": "Restore 25 HP", "value": 10, "duration": None, "target": "self"},
    {"name": "Minor Mana Potion", "rarity": "common", "type": "healing", "effect": "Restore 15 MP", "value": 10, "duration": None, "target": "self"},
    {"name": "Antidote", "rarity": "common", "type": "cure", "effect": "Cures poison", "value": 12, "duration": None, "target": "self"},
    {"name": "Bandage", "rarity": "common", "type": "healing", "effect": "Heal 10 HP over time", "value": 8, "duration": 3, "target": "self"},
    {"name": "Smelling Salt", "rarity": "common", "type": "cure", "effect": "Wake unconscious ally", "value": 15, "duration": None, "target": "ally"},
    {"name": "Torch", "rarity": "common", "type": "utility", "effect": "Light up dark areas", "value": 5, "duration": 5, "target": "area"},
    {"name": "Throwing Knife", "rarity": "common", "type": "damage", "effect": "Deal 10 damage", "value": 6, "duration": None, "target": "enemy"},
    {"name": "Basic Bomb", "rarity": "common", "type": "damage", "effect": "Deal 15 fire damage", "value": 10, "duration": None, "target": "area"},
    {"name": "Herbal Tea", "rarity": "common", "type": "healing", "effect": "Restore 10 HP & cure fatigue", "value": 9, "duration": None, "target": "self"},
    {"name": "Focus Powder", "rarity": "common", "type": "buff", "effect": "+10% accuracy", "value": 10, "duration": 3, "target": "self"},
    
    # Rare Usables
    {"name": "Greater Health Potion", "rarity": "rare", "type": "healing", "effect": "Restore 75 HP", "value": 25, "duration": None, "target": "self"},
    {"name": "Greater Mana Potion", "rarity": "rare", "type": "healing", "effect": "Restore 50 MP", "value": 25, "duration": None, "target": "self"},
    {"name": "Elixir of Strength", "rarity": "rare", "type": "buff", "effect": "+25% attack power", "value": 30, "duration": 4, "target": "self"},
    {"name": "Elixir of Defense", "rarity": "rare", "type": "buff", "effect": "+25% defense", "value": 30, "duration": 4, "target": "self"},
    {"name": "Cleanse Scroll", "rarity": "rare", "type": "cure", "effect": "Removes all negative status effects", "value": 35, "duration": None, "target": "self"},
    {"name": "Ice Bomb", "rarity": "rare", "type": "damage", "effect": "Deal 25 ice damage + slow", "value": 28, "duration": 2, "target": "area"},
    {"name": "Revival Herb", "rarity": "rare", "type": "cure", "effect": "Revive an ally with 50% HP", "value": 40, "duration": None, "target": "ally"},
    {"name": "Elven Smokeleaf", "rarity": "rare", "type": "buff", "effect": "+20% evasion", "value": 32, "duration": 3, "target": "self"},
    {"name": "Binding Powder", "rarity": "rare", "type": "utility", "effect": "Prevents enemy escape", "value": 18, "duration": 5, "target": "enemy"},
    {"name": "Spirit Flute", "rarity": "rare", "type": "utility", "effect": "Reveal hidden enemies", "value": 30, "duration": 1, "target": "area"},
    
    # Special Items
    {"name": "Phoenix Feather", "rarity": "special", "type": "cure", "effect": "Auto-revive on death (50% HP)", "value": 80, "duration": None, "target": "self"},
    {"name": "Tome of Clarity", "rarity": "special", "type": "buff", "effect": "+50% mana regen", "value": 75, "duration": 5, "target": "self"},
    {"name": "Chaos Bomb", "rarity": "special", "type": "damage", "effect": "Deal 50 random-element damage", "value": 70, "duration": None, "target": "area"},
    {"name": "Mirror Dust", "rarity": "special", "type": "buff", "effect": "Reflect 30% damage", "value": 85, "duration": 3, "target": "self"},
    {"name": "Frost Tincture", "rarity": "special", "type": "buff", "effect": "Immune to freeze & slow", "value": 60, "duration": 5, "target": "self"},
    
    # Legendary Items
    {"name": "Elixir of the Ancients", "rarity": "legendary", "type": "healing", "effect": "Fully restore HP & MP", "value": 150, "duration": None, "target": "self"},
    {"name": "Starlight Sigil", "rarity": "legendary", "type": "buff", "effect": "Double all stats for 3 turns", "value": 200, "duration": 3, "target": "self"},
    {"name": "Black Hole Flask", "rarity": "legendary", "type": "damage", "effect": "Deal 100 void damage to all", "value": 180, "duration": None, "target": "area"},
    {"name": "Chrono Elixir", "rarity": "legendary", "type": "buff", "effect": "Take two actions per turn", "value": 190, "duration": 2, "target": "self"},
    {"name": "Tear of the Goddess", "rarity": "legendary", "type": "cure", "effect": "Revive all allies with full HP", "value": 220, "duration": None, "target": "party"},
]
