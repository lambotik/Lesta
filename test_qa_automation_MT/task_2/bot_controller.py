import time as time

from log import *

uid = 0  # complex hash function


class BotController:
    tasks = []
    working_time = 0
    start_time = int(time.time())

    def add_task(self, task):
        self.tasks.append(task)

    def get_all_tasks(self):
        res = None
        if len(self.tasks) > 0:
            res = self.tasks
        return res

    def print_execution_stack(self):
        i = 1
        for task in self.tasks:
            log_info('Bot Controller', 'Task #' + str(i) + ' task name: ' + str(task.info))
            i += 1

    def run(self):
        for task in self.tasks:
            print 'RUN TASK #' + str(task.uid)
            task.__process__()
        log_info('Bot Controller', 'All tasks finished...')

    def get_task_uid(self):
        global uid
        uid = uid + 1
        return uid
