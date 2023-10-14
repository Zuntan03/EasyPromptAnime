import os, subprocess, threading
from const import Path
from l10n import L10n
from task import Task


class CommandPromptTask(Task):
    def __init__(self, editor, taskMode):
        super().__init__()
        self.editor = editor
        self.taskMode = taskMode
        self.taskName = L10n.get(taskMode)

    def resetState(self):
        super().resetState()
        self.tempDir = ""
        self.errorPath = ""

        self.command = None
        self.process = None
        self.log = ""
        self.thread = None

    def run(self):
        if self.thread is None:
            self.startThread()
        return self.pollThread()

    def startThread(self):
        self.tempDir = os.path.join(Path.temp, self.timeStr)
        os.path.exists(self.tempDir) or os.makedirs(self.tempDir)

        self.errorPath = os.path.join(self.tempDir, f"{self.timeStr}-Error.txt")

        cmd = self.createCommand()
        if self.editor.taskPauseByError:
            cmd += f" || (echo %errorlevel% > {self.errorPath} & pause)"
        else:
            cmd += f" || (echo %errorlevel% > {self.errorPath})"
        self.command = ["start", "/wait", "cmd", "/c", cmd]

        self.log = ""
        self.process = subprocess.Popen(
            self.command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            encoding="utf-8",
        )
        self.thread = threading.Thread(target=self.threadMain)
        self.thread.start()

    def createCommand(self):
        return ""

    def threadMain(self):
        self.log = self.process.communicate()[0]

    def pollThread(self):
        if self.thread.is_alive():
            return False

        self.isComleted = True
        self.isFailed = (
            (self.process.returncode != 0)
            or (os.path.exists(self.errorPath))
            or (self.log == "^C")
        )

        self.thread = None
        self.process = None
        self.isFailed or self.postProcess()
        # Log.system(self.log) # "^C" or ""
        return True

    def postProcess(self):
        pass

    def reRun(self):
        if self.isFailed:
            return False
        return self.editor.taskForever

    def __str__(self):
        return f"{super().__str__()} {self.taskName} {self.timeStr}"
