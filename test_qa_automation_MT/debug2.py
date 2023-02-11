global uid
uid = 0


def get_uid():
    global uid
    uid = uid + 1
    return uid


class Vehicle(object):
    uid = uid

    def __new__(cls):
        cls.uid = get_uid()
        return cls


class Tank(Vehicle):
    def __init__(self):
        object_id_collector = self.uid


class Tankman(Vehicle):
    uid = Vehicle.uid

    def __new__(cls):
        cls.uid = get_uid()
        return cls


class TankCommander(Tankman):
    def __init__(self):
        object_id_collector = self.uid


class TankGunner(Tankman):
    def __init__(self):
        object_id_collector = self.uid


def check_object_id_collector():
    expected_ids = (1, 2, 3, 4, 5)
    actual_ids = (TankGunner().uid,
                  TankGunner().uid,
                  Tank().uid,
                  TankCommander().uid,
                  Tank().uid
                  )
    assert actual_ids == expected_ids, 'Expected_ids: {}. Actual_ids: {}.'.format(expected_ids, actual_ids)
    print 'Test passed. Amazing job!'


check_object_id_collector()


