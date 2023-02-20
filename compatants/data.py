weapons = {
    'DC-15A Blaster Rifle':{
        'power': 40,
        'accuracy': .6,
        'multi': 0
    },
    'Needle Gun':{
        'power': 15,
        'accuracy': .9,
        'multi': 2
    },
    'Fist':{
        'power': 5,
        'accuracy': 1,
        'multi': 0
    },
    'Ray gun':{
        'power': 120,
        'accuracy': .9,
        'multi': 0
    }
}

robo_base_stats = {
    'health': 250,
    'self repair': .1
}
robot_names = ['M3gan', 'Hal', 'Fender', 'Ratchet', 'Goddard', 'Bastion']
robots_models = {
    '2nd Gen Sparring Bot':{
        'mods':{
            'fist': 10,
            'multi': 3,
            'evade': .3
            #NOTES: Can only use fists
        }
    },
    'B1-268':{
        'mods':{
            'accuracy': .8,
            'power': 2
        }
    },
    'E54':{
        'mods':{
            'self repair': .3,
            'sentry mode multi': 6,
            'sentry mode cd': 3,
            'sentry mode accuracy penalty': .2
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
            'initiative': 2
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
            'evade move': .6,
            'base evasion': .2,
            'evade turns': 1, # + base
            'health': -75
        }
    }
}