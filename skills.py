# This Python list contains 30 different skills for an auto-run dungeon crawling game,
# each with an assigned level from 1 to 5.
# The skills are scaled based on their level, with higher levels indicating more potent or advanced abilities.
# Each skill now includes parameters like 'description', 'damage' (as a string range), 'healing' (as a string range),
# 'effect_type', and 'target'.

skills_data = [
	{"name": "Basic Attack", "level": 1, "description": "Deals 5-10 physical damage to a single enemy.", "damage": "5-10", "effect_type": "physical", "target": "single_enemy"},
	{"name": "Light Heal", "level": 1, "description": "Restores 10-15 health to self.", "healing": "10-15", "effect_type": "healing", "target": "self"},
	{"name": "Quick Dodge", "level": 1, "description": "Grants a temporary dodge chance increase (15%).", "effect_type": "utility", "target": "self"},
	{"name": "Stone Skin (Minor)", "level": 1, "description": "Reduces incoming damage by 5 for 1 turn.", "effect_type": "buff", "target": "self"},
	{"name": "Mana Bolt", "level": 1, "description": "Deals 6-12 arcane damage to a single enemy.", "damage": "6-12", "effect_type": "arcane", "target": "single_enemy"},
	
	{"name": "Shield Bash", "level": 2, "description": "Deals 10-18 physical damage and has a small chance to stun a single enemy.", "damage": "10-18", "effect_type": "physical", "target": "single_enemy"},
	{"name": "Minor Fireball", "level": 2, "description": "Hurls a small fireball, dealing 12-20 fire damage to a single enemy.", "damage": "12-20", "effect_type": "fire", "target": "single_enemy"},
	{"name": "Poison Dart", "level": 2, "description": "Launches a dart that deals 8-15 poison damage over 3 turns to a single enemy.", "damage": "8-15", "effect_type": "poison", "target": "single_enemy_dot"},
	{"name": "Precision Shot", "level": 2, "description": "A precise shot dealing 15-25 physical damage to a single enemy, with increased critical chance.", "damage": "15-25", "effect_type": "physical", "target": "single_enemy"},
	{"name": "Taunt", "level": 2, "description": "Forces all enemies to attack self for 2 turns.", "effect_type": "utility", "target": "all_enemies"},
	
	{"name": "Reckless Swing", "level": 3, "description": "A wild swing dealing 20-35 physical damage to a single enemy, but reduces self-defense for 1 turn.", "damage": "20-35", "effect_type": "physical", "target": "single_enemy"},
	{"name": "Arcane Missile", "level": 3, "description": "Fires a magical missile that deals 25-40 arcane damage to a single enemy.", "damage": "25-40", "effect_type": "arcane", "target": "single_enemy"},
	{"name": "Battle Cry", "level": 3, "description": "Inspires allies, increasing all party members' attack by 10% for 2 turns.", "effect_type": "buff", "target": "party"},
	{"name": "Healing Word", "level": 3, "description": "Restores 30-45 health to self or a single ally.", "healing": "30-45", "effect_type": "healing", "target": "single_ally"},
	{"name": "Shadow Step", "level": 3, "description": "Teleports behind an enemy, dealing 20-30 physical damage and gaining temporary invisibility.", "damage": "20-30", "effect_type": "physical", "target": "single_enemy"},
	{"name": "Explosive Arrow", "level": 3, "description": "Fires an arrow that explodes on impact, dealing 18-30 physical damage to target and minor splash damage to adjacent enemies.", "damage": "18-30", "effect_type": "physical", "target": "area_of_effect"},
	{"name": "Frost Nova", "level": 3, "description": "Deals 15-25 cold damage to all enemies and slows their movement speed for 1 turn.", "damage": "15-25", "effect_type": "cold", "target": "all_enemies"},
	
	{"name": "Thunderclap", "level": 4, "description": "Unleashes a powerful shockwave, dealing 35-50 lightning damage to all enemies and stunning them briefly.", "damage": "35-50", "effect_type": "lightning", "target": "all_enemies"},
	{"name": "Mass Healing", "level": 4, "description": "Restores 50-70 health to all party members.", "healing": "50-70", "effect_type": "healing", "target": "all_party"},
	{"name": "Elemental Blast", "level": 4, "description": "Calls upon elemental forces to deal 40-60 elemental damage to a single enemy, type varies.", "damage": "40-60", "effect_type": "mixed_elemental", "target": "single_enemy"},
	{"name": "Vampiric Touch", "level": 4, "description": "Deals 30-45 shadow damage to a single enemy and heals self for 50% of damage dealt.", "damage": "30-45", "healing_on_damage": "50%", "effect_type": "shadow_drain", "target": "single_enemy"},
	{"name": "Berserker Rage", "level": 4, "description": "Enters a furious state, greatly increasing self-attack for 3 turns but reducing defense.", "effect_type": "buff", "target": "self"},
	{"name": "Divine Shield", "level": 4, "description": "Grants temporary invulnerability to all damage for 1 turn.", "effect_type": "buff", "target": "self"},
	
	{"name": "Meteor Shower", "level": 5, "description": "Calls down a devastating shower of meteors, dealing 60-90 fire damage to all enemies.", "damage": "60-90", "effect_type": "fire", "target": "all_enemies"},
	{"name": "Chain Lightning", "level": 5, "description": "Hurls a bolt of lightning that bounces between 3-5 enemies, dealing 50-75 lightning damage per hit.", "damage": "50-75", "effect_type": "lightning", "target": "multiple_enemies"},
	{"name": "Phoenix Dive", "level": 5, "description": "Dashes through enemies dealing 70-100 fire damage, and heals self for a portion of damage dealt. Resets cooldown on kill.", "damage": "70-100", "healing_on_damage": "25%", "effect_type": "fire_aoe_drain", "target": "area_of_effect"},
	{"name": "Apocalyptic Strike", "level": 5, "description": "Unleashes a cataclysmic strike dealing 100-150 unholy damage to a single enemy, potentially inflicting a powerful debuff.", "damage": "100-150", "effect_type": "unholy", "target": "single_enemy"},
	{"name": "Time Warp", "level": 5, "description": "Manipulates time to reset all self-skill cooldowns and grant an extra turn.", "effect_type": "utility", "target": "self"},
	{"name": "Grand Summoning", "level": 5, "description": "Summons a powerful minion to fight alongside the party for 5 turns.", "effect_type": "summon", "target": "party"},
	{"name": "Eternal Barrier", "level": 5, "description": "Creates an impenetrable magical barrier that absorbs a large amount of damage for all party members for 2 turns.", "effect_type": "buff", "target": "all_party"}
]

# You can now use 'skills_data' in your Python code for your dungeon crawling game.
# For example, to print all skills with their descriptions:
# for skill in skills_data:
#     print(f"Skill: {skill['name']}: {skill['description']}")

# Or to find damage skills:
# damage_skills = [skill for skill in skills_data if 'damage' in skill]
# print("\nDamage Skills:")
# for skill in damage_skills:
#     print(f"{skill['name']} ({skill.get('damage', 'N/A')} {skill.get('effect_type', '')} damage)")



status_effects = [
	# Debuffs
	{"name": "Poisoned", "type": "debuff", "effect": "Lose HP each turn", "duration": 5, "stackable": False, "curable": True},
	{"name": "Burning", "type": "debuff", "effect": "Take fire damage over time", "duration": 3, "stackable": False, "curable": True},
	{"name": "Frozen", "type": "debuff", "effect": "Cannot act; chance to thaw each turn", "duration": 2, "stackable": False, "curable": True},
	{"name": "Paralyzed", "type": "debuff", "effect": "50% chance to lose turn", "duration": 3, "stackable": False, "curable": True},
	{"name": "Silenced", "type": "debuff", "effect": "Cannot cast spells", "duration": 4, "stackable": False, "curable": True},
	{"name": "Blinded", "type": "debuff", "effect": "Severely reduced accuracy", "duration": 3, "stackable": False, "curable": True},
	{"name": "Weakened", "type": "debuff", "effect": "-25% attack power", "duration": 4, "stackable": False, "curable": True},
	{"name": "Slowed", "type": "debuff", "effect": "-30% speed", "duration": 4, "stackable": False, "curable": True},
	{"name": "Cursed", "type": "debuff", "effect": "Cannot be healed", "duration": 5, "stackable": False, "curable": True},
	{"name": "Bleeding", "type": "debuff", "effect": "Lose HP when moving or acting", "duration": 4, "stackable": True, "curable": True},
	
	# Buffs
	{"name": "Regeneration", "type": "buff", "effect": "Recover HP each turn", "duration": 5, "stackable": False, "curable": False},
	{"name": "Mana Regen", "type": "buff", "effect": "Recover MP each turn", "duration": 5, "stackable": False, "curable": False},
	{"name": "Enraged", "type": "buff", "effect": "+50% attack, -25% defense", "duration": 3, "stackable": False, "curable": False},
	{"name": "Fortified", "type": "buff", "effect": "+25% defense", "duration": 4, "stackable": False, "curable": False},
	{"name": "Haste", "type": "buff", "effect": "+30% speed", "duration": 3, "stackable": False, "curable": False},
	{"name": "Shielded", "type": "buff", "effect": "Absorb fixed damage", "duration": 3, "stackable": False, "curable": False},
	{"name": "Focused", "type": "buff", "effect": "+25% accuracy", "duration": 3, "stackable": False, "curable": False},
	{"name": "Stealth", "type": "buff", "effect": "Cannot be targeted directly", "duration": 2, "stackable": False, "curable": False},
	{"name": "Energized", "type": "buff", "effect": "Double action points", "duration": 2, "stackable": False, "curable": False},
	
	# Neutral & Special
	{"name": "Stunned", "type": "special", "effect": "Skip next turn", "duration": 1, "stackable": False, "curable": True},
	{"name": "Confused", "type": "special", "effect": "May act randomly", "duration": 3, "stackable": False, "curable": True},
	{"name": "Charmed", "type": "special", "effect": "Attack allies", "duration": 2, "stackable": False, "curable": True},
	{"name": "Feared", "type": "special", "effect": "Cannot approach source of fear", "duration": 2, "stackable": False, "curable": True},
	{"name": "Petrified", "type": "special", "effect": "Cannot act or be healed", "duration": 2, "stackable": False, "curable": True},
	{"name": "Rooted", "type": "special", "effect": "Cannot move", "duration": 3, "stackable": False, "curable": True},
	{"name": "Marked", "type": "special", "effect": "Takes increased damage", "duration": 3, "stackable": False, "curable": True},
	{"name": "Reflecting", "type": "special", "effect": "Reflects % of incoming magic", "duration": 2, "stackable": False, "curable": False},
	{"name": "Hexed", "type": "special", "effect": "Random debuff each turn", "duration": 3, "stackable": False, "curable": True},
	{"name": "Time Dilated", "type": "special", "effect": "Acts only every 2 turns", "duration": 3, "stackable": False, "curable": False},
]
