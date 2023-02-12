from Shop import Shop


class Player:
    def __init__(self):
        self.inventoryGuns = {}
        self.inventoryPlanes = []
        self.resources = Resources

    def saveResources(self):
        credits_before, gold_before = Player().resources.credits, Player().resources.gold
        print 'Resource value has been saved'
        return credits_before, gold_before

    def get_resources(self):
        self.resources.credits = 6000
        self.resources.gold = 1000
        print 'Player get credits', self.resources.credits
        print 'Player get gold', self.resources.gold
        return self.resources.credits, self.resources.gold


class Resources(Player):
    credits = None
    gold = None


class Methods(Player, Shop):
    player = Player()
    shop = Shop()

    def user(self):
        self.player = Player()
        self.shop = Shop()
        self.tankID = self.shop.db.tanks[101]
        self.tankID_credits = self.tankID['credits']
        return self.player, self.shop, self.tankID, self.tankID_credits

    def credits_will_be_debited(self):
        current_credits = Player().resources.credits
        tankID_credits = self.user()[3]
        result = current_credits - tankID_credits
        difference = tankID_credits
        return result, current_credits - difference

    # def buy_tank(self):


class Test(Methods, Player, Shop):
    def test_check_credits_will_be_debited(self):
        tank = Methods()
        result, difference = Methods.credits_will_be_debited(tank)
        print 'Result value', result
        print 'Result difference', difference
        assert result == difference
        print 'Test passed'


Player().get_resources()
Test().credits_will_be_debited()
Test().test_check_credits_will_be_debited()
player = Player()
shop = Shop()
tankID = shop.db.tanks

# tankID = shop.db.tanks.items()[0][0]
# tankID_credits = shop.db.tanks[tankID]['credits']
# print tankID
# print tankID_credits
# dcit = player.resources.credits
# print 'credits before', dcit
# tank = Shop()
#
# buy = tank._Shop__buyTank(player, tankID)
# print buy
# print player.inventoryPlanes
# credits_after = player.resources.credits
# print 'credits after', credits_after