import random

from test_qa_automation_MT.task_3.Shop import Shop

shop = Shop()


class Player():
    def __init__(self):
        self.inventoryPlanes = Resources.tanks
        self.inventoryGuns = Resources.turrets
        self.resources = Resources

    def saveResources(self):
        credits_after, gold_after = Player().resources.credits, Player().resources.gold
        tankID = player.inventoryPlanes[0]
        inventory_guns = player.inventoryGuns.append(tankID)
        print 'Resource value has been saved!'
        return credits_after, gold_after, tankID, inventory_guns

    def get_resources(self):
        self.resources.credits = random.randint(1000, 10000)
        self.resources.gold = random.randint(30, 100)
        print 'Player get credits:', self.resources.credits
        print 'Player get gold:', self.resources.gold
        return self.resources.credits, self.resources.gold

    def check_user_has_insufficient_funds(self):
        print '#' * 5, ' test_check_user_has_insufficient_funds ', '#' * 5, '\n'
        player.get_resources()
        player_credits = Player().resources.credits
        player_gold = Player().resources.gold
        tankID = UserInitialization.tankID
        tank_cost_credits = shop.db.tanks[tankID]['credits']
        tank_cost_gold = shop.db.tanks[tankID]['gold']
        buy = shop._Shop__buyTank(player, tankID)
        print 'Player buy tank for the: credits', shop.db.tanks[tankID]['credits'], \
            'gold', shop.db.tanks[tankID]['gold']
        bool = tankID in Resources.tanks
        if (player_credits and player_gold < tank_cost_credits and tank_cost_gold) and \
                (tankID in Resources.tanks) == True:
            bool = False

            print 'Warning!!!'
            return bool
        print '### Test Passed ###\n'
        return bool

    def check_user_can_buy_random_tank(self):
        print '#' * 5, ' test_check_user_can_buy_random_tank ', '#' * 5, '\n'
        player = Player()
        player.get_resources()
        tankID = UserInitialization.tankID
        print 'Player buy tank for the: credits', shop.db.tanks[tankID]['credits'], \
            'gold', shop.db.tanks[tankID]['gold']
        shop._Shop__buyTank(player, tankID)
        tank_in_hangar = player.resources.tanks
        print 'Tank in hangar:', tank_in_hangar[0]
        try:
            assert tankID == tank_in_hangar[0]
            print '### Test Passed ###\n'
        except:
            print '### Tank has been not added ###'
            print '### Test Failed ###\n'

    def check_user_can_buy_turret(self):
        print '#' * 5, 'test_check_user_can_buy_turret ', '#' * 5, '\n'
        player = Player()
        player.get_resources()
        tankID = UserInitialization.tankID
        shop._Shop__buyTank(player, tankID)
        print 'Player buy tank for the: credits', shop.db.tanks[tankID]['credits'], \
            'gold', shop.db.tanks[tankID]['gold']
        turretID = player.inventoryGuns[0]
        buy_turret = shop._Shop__buyTurrets(player, tankID, turretID)
        try:
            assert turretID == buy_turret[0]
            print '### Test Passed ###\n'
        except:
            print '### Turret has been not added ###'
            print '### Test Failed ###\n'


class Resources(Player):
    shop = Shop()
    credits = None
    gold = None
    tanks = []
    turrets = []


class UserInitialization:
    tankID = shop.db.tanks.items()[random.randint(0, 2)][0]
    tankID_credits = shop.db.tanks[tankID]['credits']
    turretID = shop.db.turrets[tankID].items()[0][0]  # keys()[random.randint(0, 1)]


player = Player()
