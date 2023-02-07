import pprint


debug = True


def log_debug(msg, bot_name):
    if not debug:
        return False
    print('\n' + msg + ' -- ' + bot_name)


def log_info(bot_name, msg):
    print('\nINFO: ' + bot_name + '  -- ' + msg)


def log_error(error_code, msg=''):
    error_msg = '\n!ERROR: ' + 'error code: %s' % error_code
    if msg != '':
        error_msg = error_msg + 'msg: ' + msg
    print('~' * 80)
    print(error_msg + '!')
    print('~' * 80)


def long_debug(long_message, bot_name=''):
    if not debug:
        return False
    print('\nBattle parameters: ' + bot_name)
    pprint.pprint(long_message)
    print('\n')  # just to add free line delimiter
