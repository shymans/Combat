enemies = [
    # Common Enemies
    {"name": "Slime", "rarity": "common", "hp": 10, "attack": 2, "defense": 1, "speed": 3, "special_skill": None, "drops": ["Goo", "Herb"], "xp": 5},
    {"name": "Rat", "rarity": "common", "hp": 12, "attack": 3, "defense": 2, "speed": 5, "special_skill": None, "drops": ["Cloth Scrap", "Cheese"], "xp": 6},
    {"name": "Cave Bat", "rarity": "common", "hp": 8, "attack": 2, "defense": 1, "speed": 7, "special_skill": None, "drops": ["Bat Wing", "Minor Potion"], "xp": 6},
    {"name": "Goblin Scout", "rarity": "common", "hp": 15, "attack": 4, "defense": 2, "speed": 4, "special_skill": None, "drops": ["Rusty Knife", "Coin"], "xp": 8},
    {"name": "Skeleton", "rarity": "common", "hp": 18, "attack": 5, "defense": 4, "speed": 2, "special_skill": None, "drops": ["Bone Shard", "Rusty Armor"], "xp": 10},
    {"name": "Wild Dog", "rarity": "common", "hp": 20, "attack": 6, "defense": 2, "speed": 6, "special_skill": None, "drops": ["Hide", "Sharp Fang"], "xp": 10},
    {"name": "Bandit Thug", "rarity": "common", "hp": 22, "attack": 7, "defense": 3, "speed": 5, "special_skill": None, "drops": ["Coin", "Iron Dagger"], "xp": 12},
    {"name": "Forest Spider", "rarity": "common", "hp": 14, "attack": 4, "defense": 3, "speed": 4, "special_skill": "Poison Bite", "drops": ["Silk", "Venom Gland"], "xp": 9},
    {"name": "Dust Imp", "rarity": "common", "hp": 16, "attack": 5, "defense": 2, "speed": 5, "special_skill": "Blinding Dust", "drops": ["Imp Dust", "Mana Shard"], "xp": 10},
    {"name": "Swamp Leech", "rarity": "common", "hp": 25, "attack": 3, "defense": 5, "speed": 2, "special_skill": "Health Drain", "drops": ["Slime", "Weak Healing Orb"], "xp": 11},
    {"name": "Ashling", "rarity": "common", "hp": 18, "attack": 6, "defense": 1, "speed": 6, "special_skill": "Ember Touch", "drops": ["Charcoal", "Fire Seed"], "xp": 10},
    {"name": "Scavenger Crow", "rarity": "common", "hp": 13, "attack": 5, "defense": 2, "speed": 8, "special_skill": "Peck Barrage", "drops": ["Feather", "Trinket"], "xp": 9},

    # Rare Enemies
    {"name": "Wraith", "rarity": "rare", "hp": 40, "attack": 10, "defense": 6, "speed": 7, "special_skill": "Phase Through", "drops": ["Wraith Essence", "Shadow Cloak"], "xp": 30},
    {"name": "Orc Warrior", "rarity": "rare", "hp": 45, "attack": 12, "defense": 8, "speed": 4, "special_skill": "Berserk", "drops": ["Orc Axe", "Heavy Hide"], "xp": 35},
    {"name": "Flame Elemental", "rarity": "rare", "hp": 35, "attack": 15, "defense": 5, "speed": 6, "special_skill": "Firestorm", "drops": ["Fire Core", "Heat Crystal"], "xp": 32},
    {"name": "Venom Serpent", "rarity": "rare", "hp": 38, "attack": 11, "defense": 5, "speed": 8, "special_skill": "Venom Spit", "drops": ["Snake Skin", "Toxic Fang"], "xp": 33},
    {"name": "Ghoul", "rarity": "rare", "hp": 42, "attack": 10, "defense": 7, "speed": 4, "special_skill": "Paralyzing Touch", "drops": ["Rotting Flesh", "Bone Dust"], "xp": 34},
    {"name": "Dark Acolyte", "rarity": "rare", "hp": 36, "attack": 9, "defense": 5, "speed": 5, "special_skill": "Shadow Bolt", "drops": ["Dark Robe", "Mana Potion"], "xp": 31},
    {"name": "Thunder Lynx", "rarity": "rare", "hp": 34, "attack": 13, "defense": 4, "speed": 10, "special_skill": "Electric Pulse", "drops": ["Spark Core", "Swift Pelt"], "xp": 36},
    {"name": "Iron Golem", "rarity": "rare", "hp": 50, "attack": 14, "defense": 12, "speed": 2, "special_skill": "Shield Wall", "drops": ["Iron Chunk", "Golem Core"], "xp": 40},
    {"name": "Frost Revenant", "rarity": "rare", "hp": 44, "attack": 11, "defense": 8, "speed": 3, "special_skill": "Freeze Aura", "drops": ["Ice Crystal", "Shattered Soul"], "xp": 38},
    {"name": "Harpy", "rarity": "rare", "hp": 30, "attack": 10, "defense": 4, "speed": 9, "special_skill": "Sonic Screech", "drops": ["Wing Feather", "Gold Trinket"], "xp": 33},

    # Special Enemies
    {"name": "Mirror Shade", "rarity": "special", "hp": 60, "attack": 13, "defense": 10, "speed": 6, "special_skill": "Reflect Damage", "drops": ["Shadow Glass", "Illusion Orb"], "xp": 60},
    {"name": "Chaos Fungus", "rarity": "special", "hp": 55, "attack": 11, "defense": 9, "speed": 4, "special_skill": "Spore Burst", "drops": ["Spore Cap", "Mutant Extract"], "xp": 55},
    {"name": "Time Wraith", "rarity": "special", "hp": 50, "attack": 12, "defense": 8, "speed": 9, "special_skill": "Time Warp", "drops": ["Hourglass Dust", "Eternal Thread"], "xp": 58},
    {"name": "Arcane Sentinel", "rarity": "special", "hp": 70, "attack": 15, "defense": 12, "speed": 3, "special_skill": "Mana Drain", "drops": ["Arcane Core", "Ancient Plate"], "xp": 65},
    {"name": "Infernal Beast", "rarity": "special", "hp": 75, "attack": 16, "defense": 10, "speed": 5, "special_skill": "Flame Howl", "drops": ["Inferno Claw", "Demon Blood"], "xp": 68},

    # Boss Enemies
    {"name": "Dreadlord Varnak", "rarity": "boss", "hp": 120, "attack": 25, "defense": 20, "speed": 6, "special_skill": "Soul Drain, Summon Shadows", "drops": ["Soul Gem", "Varnak’s Sigil", "Legendary Staff"], "xp": 150},
    {"name": "Mother Mycelia", "rarity": "boss", "hp": 100, "attack": 20, "defense": 18, "speed": 4, "special_skill": "Spore Plague, Regeneration", "drops": ["Mycelia Heart", "Spore Wand", "Rare Elixirs"], "xp": 140},
    {"name": "The Hollow King", "rarity": "boss", "hp": 130, "attack": 22, "defense": 22, "speed": 5, "special_skill": "Bone Tempest, Curse of Despair", "drops": ["Hollow Crown", "King’s Plate", "Ancient Tome"], "xp": 160},
]

# Monster Special Skills

special_skills = {
    "Poison Bite": {
        "damage": "Normal + Poison DOT",
        "status_effect": "Poison",
        "duration": 3,
        "description": "Bites the target, dealing base damage and inflicting poison for a few turns."
    },
    "Blinding Dust": {
        "damage": "None",
        "status_effect": "Blind",
        "duration": 2,
        "description": "Blinds the enemy, reducing accuracy for a short time."
    },
    "Health Drain": {
        "damage": "Leech (5–10 HP)",
        "status_effect": "None",
        "duration": 0,
        "description": "Drains health from the target and heals the user."
    },
    "Ember Touch": {
        "damage": "Minor Fire (5–8)",
        "status_effect": "Burn (20% chance)",
        "duration": 2,
        "description": "Scorches the enemy with a fiery touch that may ignite them."
    },
    "Peck Barrage": {
        "damage": "3 hits x 2–4 damage",
        "status_effect": "None",
        "duration": 0,
        "description": "Rapid pecking that hits multiple times with less accuracy."
    },
    "Phase Through": {
        "damage": "None",
        "status_effect": "Evasion Boost",
        "duration": 2,
        "description": "Temporarily becomes intangible, avoiding physical damage."
    },
    "Berserk": {
        "damage": "Boosted Attack",
        "status_effect": "Attack ↑ / Defense ↓",
        "duration": 3,
        "description": "Enters a frenzied state, gaining attack but lowering defense."
    },
    "Firestorm": {
        "damage": "Fire AoE (10–15 each target)",
        "status_effect": "Burn (25% chance)",
        "duration": 3,
        "description": "Engulfs all enemies in a fiery storm, may ignite."
    },
    "Venom Spit": {
        "damage": "Moderate (8–12)",
        "status_effect": "Poison",
        "duration": 3,
        "description": "Spits venom that damages and poisons the enemy."
    },
    "Paralyzing Touch": {
        "damage": "Low (5–7)",
        "status_effect": "Paralysis",
        "duration": 1,
        "description": "Chance to immobilize the enemy on contact."
    },
    "Shadow Bolt": {
        "damage": "Dark (10–14)",
        "status_effect": "None",
        "duration": 0,
        "description": "A blast of dark energy dealing magic damage."
    },
    "Electric Pulse": {
        "damage": "Lightning (12–15)",
        "status_effect": "Stun (30% chance)",
        "duration": 1,
        "description": "Zaps the enemy with electricity; may stun."
    },
    "Shield Wall": {
        "damage": "None",
        "status_effect": "Defense ↑↑",
        "duration": 3,
        "description": "Forms a defensive barrier that greatly increases defense."
    },
    "Freeze Aura": {
        "damage": "Ice AoE (6–10)",
        "status_effect": "Slow / Freeze (chance)",
        "duration": 2,
        "description": "Radiates chilling air that slows or freezes nearby enemies."
    },
    "Sonic Screech": {
        "damage": "Sonic AoE (8–12)",
        "status_effect": "Confuse",
        "duration": 2,
        "description": "A disorienting scream that damages and may confuse foes."
    },
    "Reflect Damage": {
        "damage": "Reflects 30% taken",
        "status_effect": "Thorns",
        "duration": 3,
        "description": "Reflects a portion of incoming damage back to the attacker."
    },
    "Spore Burst": {
        "damage": "Minor AoE (5–7)",
        "status_effect": "Confuse / Poison",
        "duration": 2,
        "description": "Explodes in spores that afflict multiple enemies with ailments."
    },
    "Time Warp": {
        "damage": "None",
        "status_effect": "Skip Turn",
        "duration": 1,
        "description": "Disrupts time, making one enemy miss their next action."
    },
    "Mana Drain": {
        "damage": "Mana Leech (5–10 MP)",
        "status_effect": "Mana Loss",
        "duration": 0,
        "description": "Steals mana from the opponent and restores the user’s."
    },
    "Flame Howl": {
        "damage": "Fire AoE (8–14)",
        "status_effect": "Fear / Attack ↓",
        "duration": 2,
        "description": "A terrifying roar infused with flame that weakens enemies."
    },
    "Soul Drain": {
        "damage": "Life & Mana Leech (15–20)",
        "status_effect": "None",
        "duration": 0,
        "description": "Steals health and mana from all enemies."
    },
    "Summon Shadows": {
        "damage": "None",
        "status_effect": "Summons",
        "duration": "Until defeated",
        "description": "Summons shadow minions to aid in battle."
    },
    "Spore Plague": {
        "damage": "None",
        "status_effect": "Stat Reduction (All)",
        "duration": 4,
        "description": "Infects all enemies with spores that sap their stats."
    },
    "Regeneration": {
        "damage": "None",
        "status_effect": "HP Regen",
        "duration": 3,
        "description": "Restores health gradually over time."
    },
    "Bone Tempest": {
        "damage": "Physical AoE (14–18)",
        "status_effect": "Bleed (20% chance)",
        "duration": 2,
        "description": "Summons swirling bone shards to damage all enemies."
    },
    "Curse of Despair": {
        "damage": "None",
        "status_effect": "Attack ↓ / Defense ↓",
        "duration": 3,
        "description": "Dark curse that weakens an enemy’s offensive and defensive abilities."
    }
}
