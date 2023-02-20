weapons = {
    'DC-15A Blaster Rifle':{
        'power': 40,
        'accuracy': .6
    },
    'Needle Gun':{
        'power': 15,
        'accuracy': .9
    },
    'Fist':{
        'power': 5,
        'accuracy': 1
    },
    'Ray gun':{
        'power': 120,
        'accuracy': .9
    }
}

robo_base_stats = {
    'health': 250,
    'self repair': .1
}
robot_names = ['M3gan', 'Hal', 'Fender', 'Ratchet', 'Goddard', 'Bastion']
robots_models = {
    '2nd Gen Sparring bot':{
        'mods':{
            'fist': 10,
            'evade': .3
            #NOTES: Can only use fists
        }
    },
    'B1-268':{
        'mods':{
            'accuracy': .8,
            'power': 1.5
        }
    },
    'E54':{
        'mods':{
            'self repair': .3,
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