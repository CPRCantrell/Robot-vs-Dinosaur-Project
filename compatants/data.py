weapons = {
    1:{
        'name': 'DC-15A Blaster Rifle',
        'power': 40,
        'accuracy': .6
    },
    2:{
        'name': 'Needle Gun',
        'power': 15,
        'accuracy': .9
    },
    3:{
        'name': 'fist',
        'power': 5,
        'accuracy': 1
    },
    4:{
        'name': 'Ray gun',
        'power': 120,
        'accuracy': .9
    }
}

robo_base_stats = {
    'health': 250,
}
robot_names = ['M3gan', 'Hal', 'Fender', 'Ratchet', 'Goddard', 'Bastion']
robots = {
    'T-800':{
        'mods':{
            'description': f"Has 100% accuracy no matter the weapon but can't use the same weapon twice",
            'accuracy': 1.0
        }
    },
    'B1-268':{
        'mods':{
            'description': f"Decreased accuracy by 80% but deal 1.5 times more damage",
            'accuracy': .8,
            'power': 1.5
        }
    },
    'E54':{
        'mods':{
            'description': f"Able to heal 20% of health but can't attack when healing",
            'healing': .2
        }
    }
}

dino_base_stats = {
    'health': 250,
    'power': 50,
    'accuracy': .9,
    'evassion': 0,
    'evade turns': 2,
    'evade move': .3,
}
dino_names = ['Aladar','Neera','Petrie', 'Spike','Blue','Butch']
dino_species = {
    'T-Rex':{
        'mods':{
            'bite': 3,
            'initiative': 1
        }
    },
    'Stegosurus':{
        'mods':{
            'tail': 1.5,
            'plating': .1,
            'health': 75
        }
    },
    'Pterodactyl':{
        'mods':{
            'evade move': .5,
            'base evasion': .2,
            'evade turns': 1, # + base
            'health': -75
        }
    }
}