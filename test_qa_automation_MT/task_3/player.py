import random

from test_qa_automation_MT.task_3.Shop import Shop

shop = Shop()


class Player(object):
    def __init__(self):
        self.inventoryPlanes = Resources.tanks
        self.inventoryGuns = Resources.turrets
        self.resources = Resources
        self.inventoryTurret = Resources.turret_tank

    def saveResources(self):
        credits_after, gold_after = Player().resources.credits, Player().resources.gold
        tankID = player.inventoryPlanes[0]
        player.inventoryGuns.append(tankID)
        turret_tank = Player().inventoryTurret
        print 'Resource value has been saved!'
        return credits_after, gold_after, tankID, turret_tank

    def get_resources(self):
        self.resources.credits = random.randint(1500, 10000)
        self.resources.gold = random.randint(30, 100)
        print 'Player get credits:', self.resources.credits
        print 'Player get gold:', self.resources.gold
        return self.resources.credits, self.resources.gold

    def check_user_has_insufficient_funds(self):
        player.get_resources()
        player_credits = Player().resources.credits
        player_gold = Player().resources.gold
        tankID = UserInitialization.tankID
        tank_cost_credits = shop.db.tanks[tankID]['credits']
        tank_cost_gold = shop.db.tanks[tankID]['gold']
        shop._Shop__buyTank(player, tankID)
        print 'Player buy tank for the: credits', shop.db.tanks[tankID]['credits'], \
            'gold', shop.db.tanks[tankID]['gold']
        bool = tankID in Resources.tanks
        print "bool", bool
        if ((player_credits < tank_cost_credits) or (player_gold < tank_cost_gold)) and \
                (tankID in Resources.tanks) == True:
            bool = False
            return bool
        return bool

    def check_user_can_buy_random_tank(self):
        player = Player()
        player.get_resources()
        credits_before_buy = player.user_inventory()[0]
        gold_before_buy = player.user_inventory()[1]
        tank_before_buy = player.user_inventory()[2]
        print 'credits_before_buy', credits_before_buy
        print 'gold_before_buy', gold_before_buy
        print 'tank_before_buy', tank_before_buy
        tankID = UserInitialization.tankID
        price_credits_per_tank = shop.db.tanks[tankID]['credits']
        price_gold_per_tank = shop.db.tanks[tankID]['gold']
        print 'Player buy tank for the: credits', shop.db.tanks[tankID]['credits'], \
            'gold', shop.db.tanks[tankID]['gold']
        shop._Shop__buyTank(player, tankID)
        tank_in_hangar = player.resources.tanks
        print 'Tank in hangar:', tank_in_hangar[0]
        credits_after_buy = player.user_inventory()[0]
        gold_after_buy = player.user_inventory()[1]
        tank_after_buy = player.user_inventory()[2]
        print 'Credits after_buy', credits_after_buy
        print 'Gold after buy', gold_after_buy
        print 'Tank after buy', tank_after_buy[0]
        return credits_before_buy, gold_before_buy, tank_before_buy, credits_after_buy, \
            gold_after_buy, tank_after_buy, price_credits_per_tank, price_gold_per_tank, tankID, tank_in_hangar[0]

    def check_user_can_buy_turret(self):
        player = Player()
        buy_tank = player.check_user_can_buy_random_tank()
        tankID = buy_tank[8]
        turretID = player.inventoryGuns[0]
        shop._Shop__buyTurrets(player, tankID, turretID)
        credits_after_buy_tank = player.user_inventory()[0]
        gold_after_buy_tank = player.user_inventory()[1]
        tank_after_buy_tank = player.user_inventory()[2]
        turret_after_buy_tank = player.user_inventory()[3]
        list_turret = shop.db.turrets[tankID].keys()[random.randint(0, 1)]
        print 'The player buys a turret by: credits', shop.db.turrets[tankID][list_turret]['credits'], \
            'gold', shop.db.turrets[tankID][list_turret]['gold']
        player.inventoryTurret.append(list_turret)
        print 'Player turret', player.inventoryTurret
        print list_turret
        credits_after_buy_turret = player.user_inventory()[0]
        gold_after_buy_turret = player.user_inventory()[1]
        tank_after_buy_turret = player.user_inventory()[2]
        turret_after_buy_turret = player.user_inventory()[3]
        price_credits_per_turret = shop.db.turrets[tankID][list_turret]['credits']
        price_gold_per_turret = shop.db.turrets[tankID][list_turret]['gold']
        print 'Player buy turret for the: credits', shop.db.turrets[tankID][list_turret]['credits'], \
            'gold', shop.db.turrets[tankID][list_turret]['gold']
        print 'Credits after_buy turret', credits_after_buy_turret
        print 'Gold after buy turret', gold_after_buy_turret
        print 'Tank after buy turret', tank_after_buy_turret[0]
        print 'Turret after buy turret', turret_after_buy_turret[0]
        return credits_after_buy_tank, gold_after_buy_tank, tank_after_buy_tank, \
            turret_after_buy_tank, credits_after_buy_turret, credits_after_buy_turret,\
            price_credits_per_turret, price_gold_per_turret, list_turret, \
            turret_after_buy_turret[0]

    def user_inventory(self):
        credit = Resources.credits
        gold = Resources.gold
        tank = Resources.tanks
        turret = Resources.turret_tank
        return credit, gold, tank, turret


class Resources(Player):
    shop = Shop()
    credits = None
    gold = None
    tanks = []
    turrets = []
    turret_tank = []


class UserInitialization:
    tankID = shop.db.tanks.items()[random.randint(0, 2)][0]
    tankID_credits = shop.db.tanks[tankID]['credits']
    turretID = shop.db.turrets[tankID].keys()[random.randint(0, 1)]


player = Player()
