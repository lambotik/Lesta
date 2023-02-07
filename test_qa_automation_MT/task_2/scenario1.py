from time import sleep

import bot_controller
import pymodule1 as log
from tasks import *


def get_data():
    data = {
        'Movement Points': ['11.11 12.3 123.4',
                            '13.14 12.3 127.4',
                            '13.14 12.3 127.4',
                            '17.14 12.1 127.4',
                            '13.14 12.3 127.4',
                            ],
        'login': 'bot1@qa.qa|q1w2e3r4t5',
        'Puts Shoot': {
            't-26': ['17.14 12.1 127.4', 2, 'HE'],
            'pz4': ('45.02 778.4 127.4', 3, 'AP'),
            'IS2': ['60.02 5.4 127.4', 5, 'APCR'],
        },
        'tanks': ('T-44'),
        'Reload Time': 1.5
    }
    return data


class Data:
    pass


class Bot(object):
    name = None
    p = {}
    gun_point = p
    tank = None
    login = ''
    state = None

    def login_in_hangar(self, login):
        self.state = 'logining'
        name = login.split('|')[0]
        password = login.split('|')[1]
        log.log_info(name, 'Starting logining Bot %s with login: %s, password: %s' % (name, login, password))
        sleep(1)
        self.name = name
        self.state = 'In hangar'
        log.log_info(name, 'Bot state: ' + self.state)

    def get_tank(self, tank):
        self.state = 'Buying tank'
        log.log_info(self.name, 'Buying tank: ' + tank)
        sleep(2)
        self.tank = tank
        log.log_info(self.name, '... OK')
        self.state = 'In hangar'

    def go_to_battle(self):
        self.state = 'Load map'
        log.log_info(self.name, 'LOADING...')
        sleep(5)
        self.p['x'] = self.gun_point['x'] = 0.0
        self.p['y'] = self.gun_point['y'] = 0.0
        self.p['z'] = self.gun_point['z'] = 0.0
        log.log_debug(self.name, '...OK')


scenarioData = Data()
bot = Bot()
log.log_info('', '~~START~~')
log.long_debug(get_data())
bot.login_in_hangar(get_data()['login'])
bot.get_tank(get_data()['tanks'])
bot.go_to_battle()
controller = bot_controller.BotController()
teleport_point = tuple(get_data()['Movement Points'][0].split(' '))
first_mission_point = MovementTask(controller.get_task_uid(), bot, get_data()['Movement Points'][1:3],
                                   'Move to first battle point')
first_mission_point.teleport(*teleport_point)
firs_target = ShootTask(bot=bot, uid=controller.get_task_uid(),
                        ammo=get_data()['Puts Shoot']['t-26'][2],
                        target_position=get_data()['Puts Shoot']['t-26'][0],
                        info='destroy t-26',
                        reload_time=get_data()['Reload Time'],
                        shots_to_kill=get_data()['Puts Shoot']['t-26'][1])

second_mission_point = MovementTask(controller.get_task_uid(), bot, get_data()['Movement Points'][2:4],
                                    'Move to second battle point')
second_target = ShootTask(bot=bot, uid=controller.get_task_uid(),
                          ammo=get_data()['Puts Shoot']['pz4'][2],
                          target_position=get_data()['Puts Shoot']['pz4'][0],
                          info='destroy pz4',
                          reload_time=get_data()['Reload Time'],
                          shots_to_kill=get_data()['Puts Shoot']['pz4'][1])
last_mission_point = MovementTask(controller.get_task_uid(), bot, get_data()['Movement Points'][4:],
                                  'move to last battle point')
last_target = ShootTask(bot=bot, uid=controller.get_task_uid(),
                        ammo=get_data()['Puts Shoot']['IS2'][2],
                        target_position=get_data()['Puts Shoot']['IS2'][0],
                        info='destroy IS2',
                        reload_time=get_data()['Reload Time'],
                        shots_to_kill=get_data()['Puts Shoot']['IS2'][1])

SCENARIO = (
    first_mission_point, firs_target,
    second_mission_point, second_target,
    last_mission_point, last_target)

for tank in SCENARIO:
    controller.add_task(tank)
controller.print_execution_stack()
controller.run()
log.log_info(bot.name, '~~FINISH~~')
