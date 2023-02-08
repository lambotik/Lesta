from logger import fin_logger


class DB:
    def __init__(self):
        self.tanks = {101: {'credits': 1000, 'gold': 0},  # tankID : {resources}
                      201: {'credits': 8500, 'gold': 30},
                      301: {'credits': 15000, 'gold': 100}}

        self.turrets = {101: {221: {'credits': 200, 'gold': 0},  # tankID : {turretID: {resources}}
                              222: {'credits': 0, 'gold': 30}},
                        201: {555: {'credits': 1050, 'gold': 0},
                              666: {'credits': 1240, 'gold': 0}},
                        301: {395: {'credits': 2200, 'gold': 0},
                              257: {'credits': 1510, 'gold': 0}}}

    def tank(self):
        self.tanks = 'gold'


class Shop:
    def __init__(self):
        self.fin_logger = fin_logger()
        self.db = DB()

    def __buyTurrets(self, *args):
        player, tankID, turretID = args

        if tankID in player.inventoryPlanes and turretID in self.db.turrets[tankID]:
            player.inventoryGuns[tankID].append(turretID)
            player.resources.gold -= self.db.turrets[tankID][turretID]['gold']
            player.resources.credits -= self.db.turrets[tankID][turretID]['credits']
            player.saveResources()

        self.fin_logger.log_state(player)

    def __buyTank(self, player, tankID):
        if tankID in self.db.tanks:
            player.inventoryPlanes.append(tankID)

            if self.db.tanks[tankID]['credits'] >= player.resources.credits and \
                    self.db.tanks[tankID]['gold'] >= player.resources.gold:
                player.resources.credits -= self.db.tanks[tankID]['credits']
                player.resources.gold -= self.db.tanks[tankID]['gold']
            player.saveResources()
            self.fin_logger.log_state(player)


class MyShop(Shop):
    print



id = Shop()
player = id.db.tanks.keys()
tank_201, credits_201, gold_201 = id.db.tanks.keys()[0], id.db.tanks.values()[0].values()[0], \
id.db.tanks.values()[0].values()[1]
tank_101, credits_101, gold_101 = id.db.tanks.keys()[1], id.db.tanks.values()[1].values()[0], \
id.db.tanks.values()[1].values()[1]
tank_301, credits_301, gold_301 = id.db.tanks.keys()[2], id.db.tanks.values()[2].values()[0], \
id.db.tanks.values()[2].values()[1]
tankID = id.db.tanks
print tankID.keys()
print tankID.keys()
# buy_tank = shop._Shop__buyTank(player,tankID)
# print buy_tank
print tank_201, credits_201, gold_201
print tank_101, credits_101, gold_101
print tank_301, credits_301, gold_301
sort_dict = sorted(id.db.tanks)
print sort_dict
print sort_dict[0]
igor = Shop()
print igor._Shop__buyTank(player, sort_dict[0])