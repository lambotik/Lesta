import time

from pymodule1 import log_debug, log_info


class MovementTask:
    uid = 0
    status = None
    bot = None
    path = 0
    info = ''

    def __init__(self, *args):
        self.uid = args[0]
        self.status = 'still'
        self.bot = args[1]
        path = []
        for p in args[2]:
            points = p.split(' ')
            path.append(points)
        self.path = path
        try:
            self.info = args[3]
        except:
            self.info = args[0]

    def __process__(self):
        self.move()

    def move(self):
        log_debug(self.bot.name, 'Start Moving...')
        self.status = 'moving'
        for point in self.path:
            log_debug(self.bot.name, 'New bot position: ' + str(point))
            self.bot.p['x'] = self.bot.gun_point['x'] = point[0]
            self.bot.p['y'] = self.bot.gun_point['y'] = point[1]
            self.bot.p['z'] = self.bot.gun_point['z'] = point[2]
        log_debug(self.bot.name, 'Finish moving at position: ' + str(self.path[-1]))

    def teleport(self, x, y, z):
        self.status = 'teleport'
        log_debug(self.bot.name, 'Teleport bot on position: %s %s %s' % (x, y, z))
        self.bot.p['x'] = x
        self.bot.p['y'] = y
        self.bot.p['z'] = z
        self.status = 'still'


class ShootTask:
    uid = None
    status = ''
    bot = None
    target = ''
    info = ''
    ammo_type = None
    shots = 0

    def __init__(self, *args, **kwargs):
        self.uid = kwargs['uid']
        self.bot = kwargs['bot']
        self.target = kwargs['target_position'].split(' ')
        self.ammo_type = kwargs['ammo']
        self.reload = kwargs['reload_time']
        self.shots = kwargs['shots_to_kill']
        self.info = kwargs.get('info', 'shoot task #' + str(self.uid))

    def __process__(self):
        self.shoot_at_target()

    def shoot_at_target(self):
        log_info(self.bot.name, 'Start shooting at %s by %s shells' % (self.target, self.ammo_type))
        if self.bot.gun_point['x'] != self.target[0] \
                or self.bot.gun_point['y'] != self.target[1] \
                or self.bot.gun_point['z'] != self.target[2]:
            self.status = 'aiming'
            self.bot.gun_point['x'] = self.target[0]
            self.bot.gun_point['y'] = self.target[1]
            self.bot.gun_point['z'] = self.target[2]
            # wait for turret move on target
            time.sleep(2)

        for shoot_count in range(1, self.shots + 1):
            self.status = 'shooting'
            log_debug(self.bot.name, self.ammo_type + ' shot #' + str(shoot_count))
            self.shot(ammo_type=self.ammo_type)
            self.status = 'reloading'
            time.sleep(self.reload)
            self.status = 'ready'

    def shot(self, ammo_type):
        if ammo_type == 'AP':
            print('BRRRRAMMM!!!')
        if ammo_type == 'APCR':
            print('BDDDRRRRIMMMM!!!')
        if ammo_type == 'HE':
            print('BGGGGSH!!!')
