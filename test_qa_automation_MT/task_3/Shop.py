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
