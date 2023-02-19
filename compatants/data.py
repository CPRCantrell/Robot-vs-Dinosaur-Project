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
        'power': 5
    },
    4:{
        'name': 'Ray gun',
        'power': 120,
        'accuracy': .9
    }
}

robot_names = ['M3gan', 'Hal', 'Fender', 'Ratchet', 'Goddard', 'Bastion']

robots = {
    1:{
        'model': 'T-800',
        'balance':{
            'description': f"Has 100% accuracy no matter the weapon but can't use the same weapon twice",
            'accuracy': 1.0
        }
    },
    2:{
        'model': 'B1-268',
        'balance':{
            'description': f"Decreased accuracy by 80% but deal 1.5 times more damage",
            'accuracy': .8,
            'power': 1.5
        }
    },
    3:{
        'model': 'E54',
        'balance':{
            'description': f"Able to heal 20% of health but can't attack when healing",
            'healing': .2
        }
    }
}

dino_names = ['Aladar','Neera','Petrie', 'Spike','Blue','Butch']

dino = {
    'T-Rex':{
        'mods':{
            'Bite': 3
        }
    },
    2:{
        'model': 'Stegosurus',
        'balance':{
            'description': f"Swing attack hits multiple enemy's dealing even damage to each",
            'health': 100
        }
    },
    3:{
        'model': 'Pterodactyl',
        'balance':{
            'description': f"High evasiveness, but lower health",
            'evasion': .3,
            'health': -100
        }
    }
}