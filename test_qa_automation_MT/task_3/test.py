from Shop import Shop
from player import Player

shop = Shop()


class TestPlayer(Player):
    player = Player()

    def test_check_user_can_buy_random_tank(self):
        Player().check_user_can_buy_random_tank()

    def test_check_user_can_buy_turret(self):
        Player().check_user_can_buy_turret()

    def test_check_user_has_insufficient_funds(self):
        bool = Player().check_user_has_insufficient_funds()
        try:
            assert bool != False
        except:
            print 'The player does not have enough funds to buy a tank,but he has been purchased'
            print '\n### Test Failed ###\n'


### User initialization ###


### Tests ###

TestPlayer().test_check_user_can_buy_random_tank()
TestPlayer().test_check_user_can_buy_turret()
TestPlayer().test_check_user_has_insufficient_funds()