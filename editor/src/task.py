import time
from l10n import L10n
from log import Log
from const import Path


class Task:
    win = None
    queue = []
    queueInfoChangedEvent = []
    pollTime = 100

    @classmethod
    def initialize(cls, win):
        Task.win = win

    @classmethod
    def queueInfoChanged(cls):
        [handler(cls.queue) for handler in cls.queueInfoChangedEvent]

    @classmethod
    def enqueue(cls, task):
        task.resetState()
        cls.queue.append(task)
        cls.queueInfoChanged()
        if len(cls.queue) == 1:
            cls.win.after(cls.pollTime, cls.runQueue)

    @classmethod
    def dequeue(cls):
        task = cls.queue[0]
        cls.queue.remove(task)
        cls.queueInfoChanged()
        return task

    @classmethod
    def runQueue(cls):
        if len(cls.queue) == 0:
            return

        if cls.queue[0].isComleted:
            endTask = cls.dequeue()
            endTask.time = time.perf_counter() - endTask.startTime
            endTask.logEnd()

            if endTask.reRun():
                cls.enqueue(endTask)
            if len(cls.queue) == 0:
                return

        startNow = not cls.queue[0].isRunning
        if startNow:
            cls.queue[0].startTime = time.perf_counter()
            cls.queue[0].timeStr = Path.getYYYYMMDDHHMMSS()
            cls.queue[0].isRunning = True
            cls.queue[0].logStart()

        if cls.queue[0].run() or startNow:
            cls.queueInfoChanged()

        if len(cls.queue) > 0:
            cls.win.after(cls.pollTime, cls.runQueue)

    def __init__(self):
        self.resetState()

    def resetState(self):
        self.startTime = 0.0
        self.time = 0.0
        self.timeStr = ""
        self.isRunning = False
        self.isComleted = False
        self.isFailed = False

    def run(self):
        return False

    def reRun(self):
        return False

    def logStart(self):
        Log.user(L10n.format("log_task_start", self))

    def logEnd(self):
        if self.isFailed:
            Log.user(L10n.format("log_task_failed", self, self.time))
        else:
            Log.user(L10n.format("log_task_success", self, self.time))

    def __str__(self):
        if self.isComleted:
            if self.isFailed:
                return "[F]"
            else:
                return "[S]"
        else:
            if self.isRunning:
                return "[R]"
            else:
                return "[_]"
