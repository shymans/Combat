


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
