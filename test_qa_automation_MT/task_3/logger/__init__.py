class fin_logger():

    def log_state(self, player):
        credit, gold, tank, turret = player.user_inventory()
        print '\n', '#' * 5, 'Player inventory', '#' * 5
        print 'Player credits:', credit
        print 'Player gold:', gold
        print 'Player tank in hangar:', tank[0]
        print 'Player turret in hanger:', turret
