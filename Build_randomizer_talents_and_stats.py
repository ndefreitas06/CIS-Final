import random

# Define the total points limit for the build
TOTAL_POINTS = 330

# Define the possible stats
STATS = {
    'Strength': 0,
    'Fortitude': 0,
    'Agility': 0,
    'Intelligence': 0,
    'Willpower': 0,
    'Charisma': 0,
    'Medium Weapon': 0,
    'Shadowcast': 0,
    'Flamecharm': 0,
    'Frostdraw': 0,
    'Thundercall': 0,
    'Bloodrend': 0,
    'Ironsing': 0,
    'Galebreathe': 0
}

# Define requirements for each Oath and armor
OATH_REQUIREMENTS = {
    'Blindseer': {'Willpower': 40},
    'Visionshaper': {'Willpower': 50},
    'Starkindred': {'Strength': 40},
    'Arcwarder': {'Flamecharm': 20, 'Thundercall': 20, 'Fortitude': 20},
    'Jetstriker': {'Agility': 50},
    'Chainwarden': {'Willpower': 40, 'Fortitude': 40, 'Strength': 40},
    'Saltchemist': {'Intelligence': 75}
}

ARMOR_REQUIREMENTS = {
    'Black Diver': {'Willpower': 10},
    'Legion Centurion': {'Fortitude': 10}
}

# Define advanced talents and their point requirements
ADVANCED_TALENTS = {
    'Neural Overload': {'Intelligence': 85},
    'Conditioned Runner': {'Fortitude': 25, 'Agility': 25},
    'Collapsed Lung': {'Strength': 100},
    'Reinforced Armor': {'Fortitude': 90, 'Willpower': 30},
    'Ghost': {'Agility': 40},
    'Dazing Finisher': {'Charisma': 55},
    'Ether Overdrive': {'Intelligence': 90, 'Attunement': 20},
    'Brick Wall': {'Fortitude': 100, 'Willpower': 100},
    'Will o\' Wisp': {'Shadowcast': 25},
    'Reshape and Remold': {'Ironsing': 70},
    'A World Without Song': {'Galebreathe': 75}
}

# Function to generate a build with random choices
def generate_build():
    build = {
        'Oath': random.choice(list(OATH_REQUIREMENTS.keys())),
        'Armor': random.choice(list(ARMOR_REQUIREMENTS.keys())),
        'Weapon': 'Medium Twinblade',  # Fixed for this example
        'Attunement': 'Shadowcast'  # Fixed for this example
    }

    return build

# Function to calculate points used for Oath, Armor, Weapon, and Attunement
def calculate_used_points(build):
    points_used = 0
    
    # Oath points
    oath = build['Oath']
    for stat, points in OATH_REQUIREMENTS[oath].items():
        STATS[stat] += points
        points_used += points
    
    # Armor points
    armor = build['Armor']
    for stat, points in ARMOR_REQUIREMENTS[armor].items():
        STATS[stat] += points
        points_used += points
    
    # Weapon points (Fixed for Medium Twinblade)
    STATS['Medium Weapon'] += 75
    points_used += 75
    
    # Attunement points (Fixed for Shadowcast)
    STATS['Shadowcast'] += 10  # Attunements start with 10 points
    points_used += 10
    
    return points_used

# Function to select advanced talents and calculate their points
def select_advanced_talents(points_available):
    talents = random.sample(list(ADVANCED_TALENTS.keys()), 3)  # Randomly select 3 advanced talents
    points_used = 0

    for talent in talents:
        for stat, points in ADVANCED_TALENTS[talent].items():
            if stat == 'Attunement':  # Special case for attunements
                attunement = 'Shadowcast'  # Fixed for this example
                STATS[attunement] += points
            else:
                STATS[stat] += points
            points_used += points
    
    return points_used

# Function to distribute remaining points across stats
def distribute_remaining_points(points_available):
    while points_available > 0:
        stat = random.choice(list(STATS.keys()))
        
        if stat in ['Strength', 'Fortitude', 'Willpower', 'Charisma']:
            if points_available >= 20 and STATS[stat] + 20 <= TOTAL_POINTS:
                STATS[stat] += 20
                points_available -= 20
            elif points_available >= 5 and STATS[stat] + 5 <= TOTAL_POINTS:
                STATS[stat] += 5
                points_available -= 5
        elif stat in ['Agility', 'Intelligence']:
            if points_available >= 20 and STATS[stat] + 20 <= TOTAL_POINTS:
                STATS[stat] += 20
                points_available -= 20
            elif points_available >= 5 and STATS[stat] + 5 <= TOTAL_POINTS:
                STATS[stat] += 5
                points_available -= 5

# Final build process
def finalize_build():
    # Generate initial build
    build = generate_build()
    
    # Calculate points used by Oath, Armor, Weapon, and Attunement
    points_used = calculate_used_points(build)
    
    # Calculate remaining points after base build
    points_available = TOTAL_POINTS - points_used
    
    # Select and apply advanced talents
    points_used += select_advanced_talents(points_available)
    points_available = TOTAL_POINTS - points_used
    
    # Distribute remaining points into stats
    distribute_remaining_points(points_available)

    # Return final build
    return STATS

# Generate a build and display the result
final_build = finalize_build()
print("Final Build:", final_build)
