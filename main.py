import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import json
import uuid # For generating unique IDs

class HeroManagerApp:
    """
    A GUI application for creating and managing dungeon crawling heroes.
    Allows users to create new level 1 heroes, load heroes from a JSON file,
    and save the current list of heroes to a JSON file.
    """
    def __init__(self, master):
        """
        Initializes the HeroManagerApp.

        Args:
            master: The root Tkinter window.
        """
        self.master = master
        master.title("Python Hero Management System")
        master.geometry("800x700") # Set initial window size
        master.configure(bg='#282c34') # Dark background for the window

        # Configure styles for better aesthetics
        self.style = ttk.Style()
        self.style.theme_use('clam') # Use 'clam' theme for a more modern look
        self.style.configure('TFrame', background='#282c34')
        self.style.configure('TLabel', background='#282c34', foreground='#e0e0e0', font=('Inter', 10))
        self.style.configure('TEntry', fieldbackground='#3a3f4b', foreground='#e0e0e0', borderwidth=1, relief="flat")
        self.style.configure('TCombobox', fieldbackground='#3a3f4b', foreground='#e0e0e0', borderwidth=1, relief="flat")
        self.style.map('TCombobox', fieldbackground=[('readonly', '#3a3f4b')])
        self.style.configure('TButton', background='#61dafb', foreground='white', font=('Inter', 10, 'bold'), borderwidth=0, relief="flat", padding=5)
        self.style.map('TButton', background=[('active', '#21a1f1')])
        self.style.configure('Accent.TButton', background='#4CAF50', foreground='white') # For save button
        self.style.map('Accent.TButton', background=[('active', '#45a049')])

        self.heroes = [] # List to store hero data

        # State variables for new hero creation form
        self.new_hero_name = tk.StringVar()
        self.new_hero_class = tk.StringVar(value="Warrior")
        self.new_hero_strength = tk.IntVar(value=10)
        self.new_hero_dexterity = tk.IntVar(value=10)
        self.new_hero_intelligence = tk.IntVar(value=10)

        # Predefined hero classes
        self.hero_classes = ['Warrior', 'Mage', 'Rogue', 'Cleric']

        # Message display area
        self.message_label = ttk.Label(master, text="", textvariable=self.message_label, wraplength=700)
        self.message_label.pack(pady=10)

        # Title
        title_label = ttk.Label(master, text="Hero Management System", font=('Inter', 24, 'bold'), foreground='#e0e0e0')
        title_label.pack(pady=20)

        # --- Hero Creation Section ---
        create_frame = ttk.Frame(master, padding="20 20 20 20", relief="groove", borderwidth=2, style='TFrame')
        create_frame.pack(pady=10, padx=20, fill="x", expand=True)

        ttk.Label(create_frame, text="Create New Hero", font=('Inter', 16, 'bold'), foreground='#e0e0e0').grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(create_frame, text="Hero Name:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        ttk.Entry(create_frame, textvariable=self.new_hero_name, width=30).grid(row=1, column=1, sticky="ew", pady=5, padx=5)

        ttk.Label(create_frame, text="Class:").grid(row=2, column=0, sticky="w", pady=5, padx=5)
        class_dropdown = ttk.Combobox(create_frame, textvariable=self.new_hero_class, values=self.hero_classes, state="readonly")
        class_dropdown.grid(row=2, column=1, sticky="ew", pady=5, padx=5)
        class_dropdown.set(self.hero_classes[0]) # Set default value

        ttk.Label(create_frame, text="Strength (1-20):").grid(row=3, column=0, sticky="w", pady=5, padx=5)
        ttk.Entry(create_frame, textvariable=self.new_hero_strength, width=10, validate="key", validatecommand=(master.register(self._validate_stat_input), '%P')).grid(row=3, column=1, sticky="w", pady=5, padx=5)

        ttk.Label(create_frame, text="Dexterity (1-20):").grid(row=4, column=0, sticky="w", pady=5, padx=5)
        ttk.Entry(create_frame, textvariable=self.new_hero_dexterity, width=10, validate="key", validatecommand=(master.register(self._validate_stat_input), '%P')).grid(row=4, column=1, sticky="w", pady=5, padx=5)

        ttk.Label(create_frame, text="Intelligence (1-20):").grid(row=5, column=0, sticky="w", pady=5, padx=5)
        ttk.Entry(create_frame, textvariable=self.new_hero_intelligence, width=10, validate="key", validatecommand=(master.register(self._validate_stat_input), '%P')).grid(row=5, column=1, sticky="w", pady=5, padx=5)

        ttk.Button(create_frame, text="Create Hero", command=self.create_hero, style='TButton').grid(row=6, column=0, columnspan=2, pady=15)

        # Configure grid column weights for responsiveness
        create_frame.grid_columnconfigure(1, weight=1)

        # --- File Operations Section ---
        file_frame = ttk.Frame(master, padding="20 20 20 20", relief="groove", borderwidth=2, style='TFrame')
        file_frame.pack(pady=10, padx=20, fill="x", expand=True)

        ttk.Label(file_frame, text="Load/Save Heroes", font=('Inter', 16, 'bold'), foreground='#e0e0e0').grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Button(file_frame, text="Load Heroes from JSON", command=self.load_heroes, style='TButton').grid(row=1, column=0, pady=10, padx=5, sticky="ew")
        ttk.Button(file_frame, text="Save Heroes to JSON", command=self.save_heroes, style='Accent.TButton').grid(row=1, column=1, pady=10, padx=5, sticky="ew")

        file_frame.grid_columnconfigure(0, weight=1)
        file_frame.grid_columnconfigure(1, weight=1)


        # --- Display Heroes Section ---
        display_frame = ttk.Frame(master, padding="20 20 20 20", relief="groove", borderwidth=2, style='TFrame')
        display_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ttk.Label(display_frame, text="Your Heroes", font=('Inter', 16, 'bold'), foreground='#e0e0e0').pack(pady=10)

        self.hero_display_text = tk.Text(display_frame, height=10, width=80, bg='#3a3f4b', fg='#e0e0e0', font=('Consolas', 10), wrap="word", relief="flat")
        self.hero_display_text.pack(fill="both", expand=True)
        self.hero_display_text.config(state="disabled") # Make text widget read-only

    def _validate_stat_input(self, P):
        """
        Validates that the input for stats is a number between 1 and 20.
        """
        if P == "":
            return True # Allow empty input temporarily for clearing
        try:
            value = int(P)
            if 1 <= value <= 20:
                return True
            else:
                self.set_message("Stats must be between 1 and 20.")
                return False
        except ValueError:
            self.set_message("Stats must be a number.")
            return False

    def set_message(self, msg):
        """
        Sets the message displayed to the user.
        """
        self.message_label.config(text=msg)

    def create_hero(self):
        """
        Handles the creation of a new hero based on form inputs.
        Generates a unique ID and adds the hero to the list.
        """
        name = self.new_hero_name.get().strip()
        if not name:
            self.set_message("Hero name cannot be empty!")
            return

        # Ensure stats are within valid range before creating hero
        try:
            strength = self.new_hero_strength.get()
            dexterity = self.new_hero_dexterity.get()
            intelligence = self.new_hero_intelligence.get()
            if not (1 <= strength <= 20 and 1 <= dexterity <= 20 and 1 <= intelligence <= 20):
                 self.set_message("Strength, Dexterity, and Intelligence must be between 1 and 20.")
                 return
        except tk.TclError: # Catches error if entry is non-numeric
            self.set_message("Invalid stat input. Please enter numbers.")
            return

        new_hero = {
            "id": str(uuid.uuid4()), # Generate a unique UUID
            "name": name,
            "level": 1,
            "class": self.new_hero_class.get(),
            "stats": {
                "strength": strength,
                "dexterity": dexterity,
                "intelligence": intelligence,
                "health": 100,
                "mana": 50,
            },
            "skills": [], # New heroes start with no specific skills
        }

        self.heroes.append(new_hero)
        # Changed to .format() method for broader compatibility
        self.set_message('Hero "{}" created successfully!'.format(new_hero["name"]))
        self.update_hero_display()

        # Reset form fields
        self.new_hero_name.set("")
        self.new_hero_class.set("Warrior")
        self.new_hero_strength.set(10)
        self.new_hero_dexterity.set(10)
        self.new_hero_intelligence.set(10)

    def load_heroes(self):
        """
        Handles loading hero data from a JSON file selected by the user.
        """
        file_path = filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if not file_path:
            self.set_message("No file selected for loading.")
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)

            if isinstance(loaded_data, list) and all(isinstance(item, dict) and 'name' in item and 'level' in item and 'class' in item for item in loaded_data):
                # Ensure unique IDs for loaded heroes, assign if missing
                heroes_with_ids = []
                for hero in loaded_data:
                    if 'id' not in hero or not hero['id']:
                        hero['id'] = str(uuid.uuid4())
                    heroes_with_ids.append(hero)

                self.heroes = heroes_with_ids
                self.set_message(f{"Successfully loaded {len(self.heroes)} heroes from file!"})
                self.update_hero_display()
            else:
                self.set_message("Invalid JSON file format. Please ensure it's an array of hero objects with 'name', 'level', and 'class'.")

        except FileNotFoundError:
            self.set_message("File not found.")
        except json.JSONDecodeError as e:
            self.set_message(f"Error parsing JSON file: {e}")
        except Exception as e:
            self.set_message(f"An unexpected error occurred: {e}")

    def save_heroes(self):
        """
        Handles saving the current list of heroes to a JSON file.
        """
        if not self.heroes:
            self.set_message("No heroes to save!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if not file_path:
            self.set_message("Save cancelled.")
            return

        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.heroes, f, indent=4)
            self.set_message(f"Heroes saved to {file_path}!")
        except Exception as e:
            self.set_message(f"Error saving heroes: {e}")

    def update_hero_display(self):
        """
        Updates the text widget to display the current list of heroes.
        """
        self.hero_display_text.config(state="normal") # Enable editing for update
        self.hero_display_text.delete(1.0, tk.END) # Clear existing text

        if not self.heroes:
            self.hero_display_text.insert(tk.END, "No heroes created yet. Start by creating one above or loading from a file!")
        else:
            for hero in self.heroes:
                display_str = f"Name: {hero.get('name', 'N/A')}\n" \
                              f"Level: {hero.get('level', 'N/A')}\n" \
                              f"Class: {hero.get('class', 'N/A')}\n"
                stats = hero.get('stats', {})
                display_str += f"  Strength: {stats.get('strength', 'N/A')}\n" \
                               f"  Dexterity: {stats.get('dexterity', 'N/A')}\n" \
                               f"  Intelligence: {stats.get('intelligence', 'N/A')}\n" \
                               f"  Health: {stats.get('health', 'N/A')}\n" \
                               f"  Mana: {stats.get('mana', 'N/A')}\n"

                skills = hero.get('skills', [])
                if skills:
                    display_str += "  Skills:\n"
                    for skill in skills:
                        display_str += f"    - {skill.get('name', 'N/A')} (Lvl {skill.get('level', 'N/A')})\n"
                display_str += "--------------------\n\n"
                self.hero_display_text.insert(tk.END, display_str)

        self.hero_display_text.config(state="disabled") # Disable editing after update

# Main execution block
if __name__ == "__main__":
    root = tk.Tk()
    app = HeroManagerApp(root)
    root.mainloop()
