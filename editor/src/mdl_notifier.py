class Notifier:
    def __init__(self):
        self._subscribers = {}
        pass

    def subsc(self, memberName, func):
        if self._subscribers.get(memberName) is None:
            self._subscribers[memberName] = []
        self._subscribers[memberName].append(func)

    def unsubsc(self, memberName, func):
        if self._subscribers.get(memberName) is None:
            return
        self._subscribers[memberName].remove(func)
        if len(self._subscribers[memberName]) == 0:
            del self._subscribers[memberName]

    def notify(self, memberName, value):
        if self._subscribers.get(memberName) is None:
            return
        for func in self._subscribers[memberName]:
            func(self, memberName, value)

    def notifyAll(self):
        for memberName in self._subscribers.keys():
            self.notify(memberName, getattr(self, memberName))

    def set(self, memberName, value):
        if getattr(self, memberName) == value:
            return
        setattr(self, memberName, value)
        self.notify(memberName, value)

    def trace_add(self, memberName, var):
        return var.trace_add("write", lambda *args: self.set(memberName, var.get()))

    def trace_remove(self, var, tid):
        var.trace_remove("write", tid)

    def bind(self, memberName, var):
        self.subsc(memberName, lambda *args: var.set(getattr(self, memberName)))
        self.trace_add(memberName, var)
