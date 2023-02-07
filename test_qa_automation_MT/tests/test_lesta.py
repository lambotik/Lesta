from generator.generator import generated_person
from test_qa_automation_MT.task_3.Shop import DB, Shop
import pytest


class Methods:
    def person(self):
        person = next(generated_person())
        player_name = person.player
        player_credits = person.credits
        player_gold = person.gold
        print(f'\nPlayer name: {player_name}')
        print(f'Player credits: {player_credits}')
        print(f'Player gold: {player_gold}')
        return player_name, player_credits, player_gold


class TestShop(Methods):
    def test_show_person(self):
        self.person()


