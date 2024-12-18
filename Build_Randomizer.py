import random

# List of Murmurs
murmurs = ['Ardour', 'Rhythm', 'Tacet']

# List of Oaths
oaths = [
    'Oathless', 'Blindseer', 'Visionshaper', 'Starkindred', 
    'Arcwarder', 'Linkstrider', 'Jetstriker', 'Dawnwalker', 
    'Contractor', 'ChainWarden', 'Bladeharper', 'Fadetrimmer', 'Saltchemist'
]

# List of Outfits
outfits = [
    'Black Diver', 'Ignition Deepdelver', 'Prophet\'s Cloak', 
    'Authority Commander', 'Legion Centurion', 'Navaen Warcheif', 
    'Justicar\'s Armor', 'Summer Dragoon', 'Ferryman\'s Coat', 
    'Royal Etrean Guard'
]

# List of Weapon Types
weapon_types = [
    'Heavy Sword', 'Heavy Axe', 'Heavy Hammer', 'Medium Sword', 
    'Medium Club', 'Medium Spear', 'Medium Twinblade', 'Medium Rifle', 
    'Light Dagger', 'Light Fists', 'Light Gun'
]

# List of Enchants
enchants = [
    'Blazing', 'Chilling', 'Curse of the Bloodthirsty', 'Curse of the No Life King', 
    'Curse of the Unbidden', 'Curse of Yun\'Shul', 'Curse of Repulsion', 'Deferred', 
    'Detonation', 'Elastic', 'Gluttony', 'Grim', 'Harrowing', 'Heroism', 
    'Metal', 'Nemesis', 'Obfuscation', 'Providence\'s Thorns', 'Sear', 
    'Solar', 'Stone', 'Storm', 'Stormbreaker', 'Tears of the Edenkite', 
    'Umbral Knight', 'Vamparism', 'Wild'
]

# List of Attunements
attunements = ['Flamecharm', 'Frostdraw', 'Thundercall', 'Galebreathe', 
               'Shadowcast', 'Ironsing', 'Bloodrend']

# List of Flaws
flaws = [
    'Deficient', 'Fugitive', 'Vegetarian', 'Glutton', 'Manic', 'Hemophilia', 
    'Squeamish', 'Obvious', 'Simple', 'Blind'
]

# List of Boons
boons = [
    'Autodidact', 'Gourmet', 'Maverick', 'Packmule', 'Scrapper', 'Steadfast', 
    'Survivalist', 'Sly'
]

# List of Traits
traits = ['Vitality', 'Erudition', 'Proficiency', 'Songchant']

# Function to generate traits with a total sum of 12, and each value between 0 and 6
def generate_traits():
    trait_values = [0] * 4
    total = 12
    
    while total > 0:
        for i in range(len(trait_values)):
            if total == 0:
                break
            max_value = min(6 - trait_values[i], total)  # Ensure we don't exceed 6
            add_value = random.randint(0, max_value)
            trait_values[i] += add_value
            total -= add_value
    
    return dict(zip(traits, trait_values))

# Function to select flaws and boons
def generate_flaws_and_boons():
    num_flaws = random.randint(1, 2)
    selected_flaws = random.sample(flaws, num_flaws)
    selected_boons = random.sample(boons, num_flaws)
    return selected_flaws, selected_boons

# Function to generate selections for Murmur, Oath, Outfit, Weapon Type, Attunement, and Enchant
def generate_selections():
    selected_murmur = random.choice(murmurs)
    selected_oath = random.choice(oaths)
    selected_outfit = random.choice(outfits)
    selected_weapon_type = random.choice(weapon_types)
    selected_enchant = random.choice(enchants)
    selected_attunement = random.choice(attunements)
    
    return selected_murmur, selected_oath, selected_outfit, selected_weapon_type, selected_enchant, selected_attunement

# Function to reroll selections based on user input
def reroll_selection(selected_murmur, selected_oath, selected_outfit, selected_weapon_type, selected_enchant, selected_attunement, selected_traits, selected_flaws, selected_boons):
    while True:
        reroll_choice = input("\nWould you like to reroll any of the traits? (Enter 'end' to stop, or 'yes' to continue): ").strip().lower()
        
        if reroll_choice == "end":
            print("\nThank you for using the generator!")
            break
        elif reroll_choice == "yes":
            print("\nWhich one would you like to reroll? Choose a number:")
            print("1: Murmur\n2: Oath\n3: Outfit\n4: Weapon Type\n5: Enchant\n6: Attunement\n7: Traits\n8: Flaws and Boons")
            choice = input("Enter the number (or 'end' to stop): ").strip()
            
            if choice == "end":
                print("\nThank you for using the generator!")
                break
            
            if choice == "1":
                selected_murmur = random.choice(murmurs)
                print(f"New Murmur: {selected_murmur}")
            elif choice == "2":
                selected_oath = random.choice(oaths)
                print(f"New Oath: {selected_oath}")
            elif choice == "3":
                selected_outfit = random.choice(outfits)
                print(f"New Outfit: {selected_outfit}")
            elif choice == "4":
                selected_weapon_type = random.choice(weapon_types)
                print(f"New Weapon Type: {selected_weapon_type}")
            elif choice == "5":
                selected_enchant = random.choice(enchants)
                print(f"New Enchant: {selected_enchant}")
            elif choice == "6":
                selected_attunement = random.choice(attunements)
                print(f"New Attunement: {selected_attunement}")
            elif choice == "7":
                selected_traits = generate_traits()
                print("\nNew Traits with a total of 12:")
                for trait, value in selected_traits.items():
                    print(f"{trait}: {value}")
            elif choice == "8":
                selected_flaws, selected_boons = generate_flaws_and_boons()
                print(f"New Flaws ({len(selected_flaws)}):", selected_flaws)
                print(f"New Boons ({len(selected_boons)}):", selected_boons)

    return selected_murmur, selected_oath, selected_outfit, selected_weapon_type, selected_enchant, selected_attunement, selected_traits, selected_flaws, selected_boons


# Generate and display the selections
selected_murmur, selected_oath, selected_outfit, selected_weapon_type, selected_enchant, selected_attunement = generate_selections()
selected_traits = generate_traits()
selected_flaws, selected_boons = generate_flaws_and_boons()

# Output the results
print(f"Randomly selected Murmur: {selected_murmur}")
print(f"Randomly selected Oath: {selected_oath}")
print(f"Randomly selected Outfit: {selected_outfit}")
print(f"Randomly selected Weapon Type: {selected_weapon_type}")
print(f"Randomly selected Enchant: {selected_enchant}")
print(f"Randomly selected Attunement: {selected_attunement}")

print("\nRandomly selected Traits with a total of 12:")
for trait, value in selected_traits.items():
    print(f"{trait}: {value}")

print(f"\nRandomly selected Flaws ({len(selected_flaws)}):", selected_flaws)
print(f"Randomly selected Boons ({len(selected_boons)}):", selected_boons)

# Ask if the user wants to reroll any trait
selected_murmur, selected_oath, selected_outfit, selected_weapon_type, selected_enchant, selected_attunement, selected_traits, selected_flaws, selected_boons = reroll_selection(
    selected_murmur, selected_oath, selected_outfit, selected_weapon_type, selected_enchant, selected_attunement, selected_traits, selected_flaws, selected_boons
)

