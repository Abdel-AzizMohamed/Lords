from random import randint


def resetBattle(name, Map, main_json):
    Map.changeMap(name, 1)
    Map.current_entities["player"].hp = main_json["vit"] * 10
    Map.current_entities["player"].damge = main_json["str"]

    mon_max_hp = Map.current_entities['monster'][0].hp
    mon_name = Map.current_entities['monster'][0].name

    return (mon_max_hp, mon_name)

def calc_attack(Map):
    crit_num = randint(1, 25)
    pl_crit_ch = 1
    if randint(1, 25) == crit_num:
        pl_crit_ch = 1.3
    mon_crit_ch = 1
    if randint(1, 25) == crit_num:
        mon_crit_ch = 1.3

    mon_damge_diff = randint(round(Map.current_entities['monster'][0].damge * .7), Map.current_entities['monster'][0].damge)
    pl_damge_diff = randint(round(Map.current_entities['player'].damge * .7), Map.current_entities['player'].damge)

    Map.current_entities['player'].hp -=  round(mon_damge_diff * pl_crit_ch)
    Map.current_entities['monster'][0].hp -= round( pl_damge_diff * mon_crit_ch)

def xpCalc(level):
    return round((level/0.3)**2)
