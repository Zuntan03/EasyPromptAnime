class Log:
    userLogEvent = []
    systemLogEvent = []

    @classmethod
    def user(cls, msg):
        # msgNl = msg if msg.endswith("\n") else msg + "\n"
        # msgNoNewLine = (msg[:-1] if msg.endswith("\n") else msg)

        [hadler(msg) for hadler in cls.userLogEvent]
        cls.system(msg)

    @classmethod
    def system(cls, msg):
        # msgNl = msg if msg.endswith("\n") else msg + "\n"
        # msgNoNewLine = (msg[:-1] if msg.endswith("\n") else msg)
        [hadler(msg) for hadler in cls.systemLogEvent]
        print(msg)

    # @classmethod
    # def _system_impl(cls, msg):
    #     [hadler(msg) for hadler in cls.systemLogEvent]
    #     print(msg)
