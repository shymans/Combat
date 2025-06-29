# Import and setup
import random
import logging
import re
from enemies import enemies
from skills import skills_data
from items import usable_items

# This will create a log file of the combat to see the details of the battle.
logging.basicConfig(filename="combat_log.txt", level=logging.INFO, filemode="w",
                    format="%(message)s")

def parse_range(range_str):
    """Parses a string like '10-15' into a random integer in that range."""
    if not range_str:
        return 0
    parts = range_str.split("-")
    if len(parts) == 2:
        return random.randint(int(parts[0]), int(parts[1]))
    return int(parts[0])

class Hero:
    """Represents a hero character in the party."""
    def __init__(self, name, hp=30, attack=5, defense=2, speed=3, level=1):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        
        # Base stats are stored to properly handle buffs/debuffs
        self.base_attack = attack
        self.base_defense = defense
        self.base_speed = speed

        # Active stats that can be modified by effects
        self.attack = attack
        self.defense = defense
        self.speed = speed
        
        self.level = level
        self.alive = True
        self.skills = self.assign_skills()
        self.inventory = self.assign_starting_items()
        self.effects = []  # To store buffs/debuffs like {'stat': 'attack', 'modifier': 1.2, 'duration': 3}

    def assign_skills(self):
        """Assigns a few random skills to the hero based on their level."""
        possible = [s for s in skills_data if s.get("level", 1) <= self.level + 1]
        return random.sample(possible, min(3, len(possible)))
        
    def assign_starting_items(self):
        """Gives the hero 1 to 3 random common usable items to start with."""
        common_items = [item for item in usable_items if item['rarity'] == 'common']
        if not common_items:
            return []
        num_items = random.randint(1, 3)
        return random.sample(common_items, k=min(num_items, len(common_items)))

    def update_effects(self):
        """Updates status effects at the start of a hero's turn. Resets stats and reapplies active effects."""
        # Reset stats to base before reapplying non-expired buffs
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.speed = self.base_speed
        
        active_effects = []
        for effect in self.effects:
            effect['duration'] -= 1
            if effect['duration'] > 0:
                active_effects.append(effect)
                # Re-apply the stat modification
                if effect['stat'] == 'attack':
                    self.attack = int(self.attack * effect['modifier'])
                elif effect['stat'] == 'defense':
                    self.defense = int(self.defense * effect['modifier'])
                # Add more stats as needed
            else:
                logging.info(f"{self.name}'s {effect['name']} has worn off.")

        self.effects = active_effects

    def take_damage(self, dmg):
        """Calculates damage taken after defense and updates HP."""
        dmg_taken = max(0, dmg - self.defense)
        self.hp -= dmg_taken
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        logging.info(f"{self.name} takes {dmg_taken} damage. [HP: {self.hp}/{self.max_hp}]")

    def heal(self, amount):
        """Heals the hero for a given amount, not exceeding max HP."""
        if self.alive:
            self.hp = min(self.max_hp, self.hp + amount)
            logging.info(f"{self.name} heals for {amount}. [HP: {self.hp}/{self.max_hp}]")

    def use_item(self, item, allies, enemies):
        """Logic for using an item from the inventory."""
        if item not in self.inventory:
            logging.info(f"{self.name} tries to use {item['name']} but doesn't have it.")
            return

        self.inventory.remove(item)
        logging.info(f"{self.name} uses {item['name']}.")

        item_type = item["type"]
        effect_str = item["effect"]
        target_type = item["target"]
        
        # Use regex to find all numbers in the effect string
        numbers = [int(n) for n in re.findall(r'\d+', effect_str)]
        
        if item_type == "healing":
            amount = numbers[0] if numbers else 0
            if "HP" in effect_str:
                if target_type == "self":
                    self.heal(amount)
                elif target_type == "ally":
                    targets = [a for a in allies if a.alive and a.hp < a.max_hp]
                    if targets:
                        target = random.choice(targets)
                        logging.info(f"{self.name} uses {item['name']} on {target.name}.")
                        target.heal(amount)

        elif item_type == "damage":
            damage = numbers[0] if numbers else 0
            if target_type == "enemy":
                targets = [e for e in enemies if e.alive]
                if targets:
                    target = random.choice(targets)
                    logging.info(f"{self.name} throws a {item['name']} at {target.name} for {damage} damage.")
                    target.take_damage(damage)
            elif target_type == "area":
                logging.info(f"{self.name} uses {item['name']}, hitting all enemies.")
                for target in enemies:
                    if target.alive:
                        target.take_damage(damage)

        elif item_type == "buff":
            duration = item["duration"]
            if numbers and duration:
                percent_boost = numbers[0]
                modifier = 1 + (percent_boost / 100)
                
                new_effect = {
                    'name': item['name'],
                    'duration': duration + 1,  # +1 because it ticks down at start of the next turn
                    'modifier': modifier
                }

                if "attack" in effect_str:
                    new_effect['stat'] = 'attack'
                    self.effects.append(new_effect)
                    self.attack = int(self.attack * modifier)
                    logging.info(f"{self.name}'s attack is boosted by {percent_boost}%.")

                elif "defense" in effect_str:
                    new_effect['stat'] = 'defense'
                    self.effects.append(new_effect)
                    self.defense = int(self.defense * modifier)
                    logging.info(f"{self.name}'s defense is boosted by {percent_boost}%.")
        
        elif item_type == "cure":
            # Current implementation doesn't have status ailments to cure.
            logging.info(f"{self.name} uses {item['name']} to cure ailments.")
        
        else: # Utility, etc.
            logging.info(f"{self.name} uses {item['name']}, but it has no direct combat effect.")

    def use_skill(self, skill, allies, enemies):
        """Logic for using a skill."""
        target_type = skill.get("target")
        name = skill["name"]
        if target_type == "self":
            if "healing" in skill:
                amount = parse_range(skill["healing"])
                logging.info(f"{self.name} uses {name} on self for {amount} healing.")
                self.heal(amount)
        elif target_type == "single_enemy":
            targets = [e for e in enemies if e.alive]
            if targets:
                target = random.choice(targets)
                amount = parse_range(skill["damage"])
                logging.info(f"{self.name} uses {name} on {target.name} for {amount} damage.")
                target.take_damage(amount)
        elif target_type == "all_enemies":
            for target in enemies:
                if target.alive:
                    amount = parse_range(skill["damage"])
                    logging.info(f"{self.name} uses {name} on {target.name} for {amount} damage.")
                    target.take_damage(amount)
        elif target_type == "single_ally":
            targets = [a for a in allies if a.alive and a.hp < a.max_hp]
            if targets:
                target = random.choice(targets)
                amount = parse_range(skill["healing"])
                logging.info(f"{self.name} uses {name} on {target.name} for {amount} healing.")
                target.heal(amount)
        else:
            self.basic_attack(random.choice([e for e in enemies if e.alive]))

    def basic_attack(self, target):
        """A standard attack against a single target."""
        damage = random.randint(self.attack, self.attack + 4)
        logging.info(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

class Enemy:
    """Represents an enemy character."""
    def __init__(self, data, level_scale=0):
        self.name = data["name"]
        self.max_hp = data["hp"] + level_scale * 3
        self.hp = self.max_hp
        self.attack = data["attack"] + level_scale
        self.defense = data["defense"] + level_scale
        self.speed = data["speed"]
        self.xp = data["xp"] + level_scale * 2
        self.alive = True

    def take_damage(self, dmg):
        """Calculates damage taken after defense and updates HP."""
        dmg_taken = max(0, dmg - self.defense)
        self.hp -= dmg_taken
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        logging.info(f"{self.name} takes {dmg_taken} damage. [HP: {self.hp}/{self.max_hp}]")

    def basic_attack(self, target):
        """A standard attack against a single target."""
        damage = random.randint(self.attack, self.attack + 3)
        logging.info(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

def battle(party, enemies_data):
    """Manages a single battle from start to finish."""
    logging.info("\n--- A Battle Begins! ---")
    
    # Log starting inventories for clarity
    for hero in party:
        if hero.inventory:
            item_names = ", ".join([item['name'] for item in hero.inventory])
            logging.info(f"{hero.name} starts with: {item_names}")

    combatants = party + enemies_data
    turn = 1
    while any(hero.alive for hero in party) and any(enemy.alive for enemy in enemies_data):
        logging.info(f"--- Round {turn} ---")
        turn_order = sorted([c for c in combatants if c.alive], key=lambda x: x.speed, reverse=True)
        
        for entity in turn_order:
            if not entity.alive:
                continue

            if isinstance(entity, Hero):
                entity.update_effects()  # Update buffs/debuffs at the start of the turn
                
                # Decide on an action: attack, use a skill, or use an item
                possible_actions = ['attack', 'skill']
                if entity.inventory:
                    possible_actions.append('item')
                
                action = random.choice(possible_actions)
                
                if action == 'item':
                    # For now, just use a random item. This could be made more intelligent.
                    item_to_use = random.choice(entity.inventory)
                    entity.use_item(item_to_use, party, enemies_data)
                elif action == 'skill':
                    skill = random.choice(entity.skills)
                    entity.use_skill(skill, party, enemies_data)
                else:  # 'attack'
                    if any(e.alive for e in enemies_data):
                        target = random.choice([e for e in enemies_data if e.alive])
                        entity.basic_attack(target)
            else:  # Enemy's turn
                if any(h.alive for h in party):
                    target = random.choice([h for h in party if h.alive])
                    entity.basic_attack(target)
        
        logging.info("--- End of Round ---")
        turn += 1
    
    if all(not enemy.alive for enemy in enemies_data):
        logging.info("Victory! All enemies defeated.")
    else:
        logging.info("Defeat... The party has been wiped out.")

def run_dungeon():
    """Sets up and runs a multi-floor dungeon crawl."""
    # NOTE: This function requires 'enemies.py' and 'skills.py' to exist and be populated.
    try:
        if not enemies or not skills_data:
            print("Error: 'enemies' or 'skills_data' not found. Please ensure enemies.py and skills.py are present and populated.")
            return
    except NameError:
        print("Error: 'enemies' or 'skills_data' not found. Please ensure enemies.py and skills.py are present and populated.")
        return

    num_floors = random.randint(3, 7)
    logging.info(f"== Dungeon Run Starts: {num_floors} Floors ==")
    party = [Hero("Warrior", hp=100, speed=10, defense=25, attack=25, level=3), Hero("Rogue", hp=100, speed=12, defense=15, attack=30, level=3), Hero("Cleric", hp=100, attack=20, defense=30, speed=9, level=3)]

    for floor in range(1, num_floors + 1):
        logging.info(f"\n== Floor {floor} ==")
        num_enemies = random.randint(2, 4)
        enemy_pool = random.sample(enemies, k=num_enemies)
        enemy_objs = [Enemy(data, level_scale=floor - 1) for data in enemy_pool]
        
        battle(party, enemy_objs)

        if all(not hero.alive for hero in party):
            logging.info(f"The party was defeated on Floor {floor}.")
            break
        else:
            logging.info("--- Post-Battle Recovery ---")
            for hero in party:
                if hero.alive:
                    heal_amount = int(hero.max_hp * 0.1) # Recover 10% of max HP
                    hero.heal(heal_amount)
                    logging.info(f"{hero.name} rests and recovers {heal_amount} HP.")

    logging.info("\n== Dungeon Run Complete ==")

if __name__ == "__main__":
    run_dungeon()
    print("Dungeon run finished. Check 'combat_log.txt' for the story of your adventure!")
