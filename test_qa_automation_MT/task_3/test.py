import pprint
import unittest

from test_qa_automation_MT.task_3.Shop import Shop
from test_qa_automation_MT.task_3.Player import Player

shop = Shop()


class TestPlayerTestCase(unittest.TestCase):
    player = Player()
    count = 1

    def setUp(self):
        self.player.user_inventory()
        print '\n', '#' * 5, 'Start Test ', pprint.saferepr(TestPlayerTestCase.count), '#' * 5

    def tearDown(self):
        self.player.user_inventory()
        print '\n', '#' * 5, 'Finished Test', pprint.saferepr(TestPlayerTestCase.count), '#' * 5, '\n'
        TestPlayerTestCase.count += 1

    @unittest.expectedFailure
    def test_check_user_can_buy_random_tank(self):
        credits_before_buy, gold_before_buy, tank_before_buy, credits_after_buy, gold_after_buy, \
            tank_after_buy, price_credits_per_tank, price_gold_per_tank, tankID, tank_in_hangar = \
            Player().check_user_can_buy_random_tank()
        self.assertTrue(credits_before_buy > price_credits_per_tank, 'The user does not have enough credits')
        self.assertTrue(gold_before_buy > price_gold_per_tank, 'The user does not have enough gold')
        self.assertTrue(credits_before_buy == price_credits_per_tank + credits_after_buy,
                        'Credits have not been written off')
        self.assertTrue(gold_before_buy == price_gold_per_tank + gold_after_buy,
                        'Gold have not been written off')
        self.assertTrue(tankID == tank_in_hangar, 'The purchased tank is not in the hangar, '
                                                  'or there is another tank in the hangar')

    @unittest.expectedFailure
    def test_check_user_can_buy_turret(self):
        credits_after_buy_tank, gold_after_buy_tank, tank_after_buy_tank, turret_after_buy_tank, \
            credits_after_buy_turret, credits_after_buy_turret, price_credits_per_turret, \
            price_gold_per_turret, list_turret, turret_after_buy_turret = Player().check_user_can_buy_turret()
        self.assertTrue(credits_after_buy_tank > price_credits_per_turret, 'The user does not have enough credits')
        self.assertTrue(gold_after_buy_tank > price_gold_per_turret, 'The user does not have enough gold')
        self.assertTrue(gold_after_buy_tank == price_credits_per_turret + credits_after_buy_turret,
                        'Credits have not been written off')
        self.assertTrue(gold_after_buy_tank == price_credits_per_turret + gold_after_buy_tank,
                        'Gold have not been written off')
        self.assertTrue(list_turret == turret_after_buy_turret, 'The purchased turret is not in the hangar, '
                                                                'or there is another tank in the hangar')

    @unittest.expectedFailure
    def test_check_user_has_insufficient_funds(self):
        bool = Player().check_user_has_insufficient_funds()
        self.assertTrue(bool), 'The player does not have enough funds to buy a tank,but he has been purchased'


if __name__ == '__main__':
    unittest.main()
