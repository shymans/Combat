import random
import tkinter as tk
import skills

import random

# ----- Placeholder for player party and enemy list -----
# (You should replace with your full data)

party = [
	{"name": "Knight", "hp": 100, "attack": 12, "defense": 8, "speed": 5, "weapon": {"attack": 8, "effect": None}, "armor": {"defense": 5}, "statuses": [], "alive": True},
	{"name": "Mage", "hp": 70, "attack": 8, "defense": 3, "speed": 7, "weapon": {"attack": 10, "effect": "Burn chance"}, "armor": {"defense": 2}, "statuses": [], "alive": True}
]

base_enemies = [
	{"name": "Goblin", "base_hp": 50, "base_attack": 6, "base_defense": 2, "speed": 5},
	{"name": "Skeleton", "base_hp": 60, "base_attack": 7, "base_defense": 3, "speed": 4},
	{"name": "Orc", "base_hp": 80, "base_attack": 10, "base_defense": 4, "speed": 3},
]

# ----- Battle System -----
def battle(party, enemies):
	turn = 1
	while any(member["alive"] for member in party) and any(e["hp"] > 0 for e in enemies):
		print(f"\n--- Turn {turn} ---")
		for member in party:
			if not member["alive"]:
				continue
			# Choose random live enemy
			targets = [e for e in enemies if e["hp"] > 0]
			if not targets:
				break
			target = random.choice(targets)
			damage = max(1, member["attack"] + member["weapon"]["attack"] - target["defense"])
			target["hp"] -= damage
			print(f"{member['name']} hits {target['name']} for {damage} damage!")
			
		for enemy in enemies:
			if enemy["hp"] <= 0:
				continue
			target = random.choice([m for m in party if m["alive"]])
			damage = max(1, enemy["attack"] - (target["defense"] + target["armor"]["defense"]))
			target["hp"] -= damage
			print(f"{enemy['name']} hits {target['name']} for {damage} damage!")
			if target["hp"] <= 0:
				target["alive"] = False
				print(f"{target['name']} has fallen!")
				
		turn += 1
		
	if all(e["hp"] <= 0 for e in enemies):
		print("Party cleared the floor!")
		return True
	else:
		print("The party has been wiped out!")
		return False
	
# ----- Dungeon Generator -----
def generate_enemy_wave(floor, base_enemies):
	num_enemies = random.randint(1, 4)
	wave = []
	for _ in range(num_enemies):
		template = random.choice(base_enemies)
		scale = 1 + floor * 0.3
		enemy = {
			"name": f"{template['name']} (F{floor})",
			"hp": int(template["base_hp"] * scale),
			"attack": int(template["base_attack"] * scale),
			"defense": int(template["base_defense"] * scale),
			"speed": template["speed"],
		}
		wave.append(enemy)
	return wave

# ----- Dungeon Run -----
def run_dungeon(party, base_enemies):
	num_floors = random.randint(3, 6)
	print(f"\nEntering dungeon with {num_floors} floors...\n")
	
	for floor in range(1, num_floors + 1):
		print(f"\n=== Floor {floor} ===")
		enemies = generate_enemy_wave(floor, base_enemies)
		
		win = battle(party, enemies)
		if not win:
			print("\nGame Over.")
			return
		
		# Optional post-floor healing & revive
		for member in party:
			if member["alive"]:
				member["hp"] += 20
				print(f"{member['name']} recovers 20 HP.")
			else:
				print(f"{member['name']} remains unconscious...")
				
	print("\n🎉 Dungeon cleared! Victory!")
	
# ----- Run it -----
run_dungeon(party, base_enemies)

import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os

# ----- Sample Characters to Choose From ----- #
available_characters = [
	{"name": "Knight", "hp": 100, "attack": 12, "defense": 8, "speed": 5, "weapon": {"attack": 8}, "armor": {"defense": 5}},
	{"name": "Mage", "hp": 70, "attack": 8, "defense": 3, "speed": 7, "weapon": {"attack": 10}, "armor": {"defense": 2}},
	{"name": "Rogue", "hp": 80, "attack": 10, "defense": 4, "speed": 9, "weapon": {"attack": 6}, "armor": {"defense": 3}},
	{"name": "Cleric", "hp": 90, "attack": 6, "defense": 5, "speed": 6, "weapon": {"attack": 5}, "armor": {"defense": 4}}
]

# ----- Global Party List ----- #
selected_party = []

# ----- GUI Application ----- #
class PartySelectionApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Select Your Party")
		self.party_frame = tk.Frame(root)
		self.party_frame.pack(pady=10)
		
		self.char_vars = []
		for char in available_characters:
			var = tk.IntVar()
			cb = tk.Checkbutton(self.party_frame, text=char["name"], variable=var)
			cb.pack(anchor='w')
			self.char_vars.append((var, char))
			
		btn_frame = tk.Frame(root)
		btn_frame.pack(pady=10)
		
		tk.Button(btn_frame, text="Start with Selected", command=self.select_party).pack(side=tk.LEFT, padx=5)
		tk.Button(btn_frame, text="Load Party from File", command=self.load_party).pack(side=tk.LEFT, padx=5)
		
	def select_party(self):
		global selected_party
		selected_party = []
		for var, char in self.char_vars:
			if var.get():
				char_copy = char.copy()
				char_copy["statuses"] = []
				char_copy["alive"] = True
				selected_party.append(char_copy)
		if not selected_party:
			messagebox.showerror("Error", "No characters selected.")
			return
		self.save_party()
		self.root.quit()
		
	def save_party(self):
		with open("saved_party.json", "w") as f:
			json.dump(selected_party, f)
		messagebox.showinfo("Saved", "Party saved to saved_party.json")
		
	def load_party(self):
		global selected_party
		file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
		if not file_path:
			return
		try:
			with open(file_path, "r") as f:
				loaded_party = json.load(f)
				for member in loaded_party:
					member["statuses"] = []
					member["alive"] = True
				selected_party = loaded_party
				messagebox.showinfo("Loaded", f"Loaded {len(selected_party)} party members.")
				self.root.quit()
		except Exception as e:
			messagebox.showerror("Error", f"Failed to load party: {e}")
			
# ----- Run GUI ----- #
def select_party_gui():
	root = tk.Tk()
	app = PartySelectionApp(root)
	root.mainloop()
	return selected_party

# Example usage:
if __name__ == "__main__":
	party = select_party_gui()
	if party:
		print("Selected Party:")
		for member in party:
			print(f"- {member['name']} (HP: {member['hp']}, ATK: {member['attack']})")
			
			