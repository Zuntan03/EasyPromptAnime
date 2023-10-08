from log import Log
import tkinter as tk


class OutputController:
    def __init__(self, form, model):
        self.form = form
        self.model = model
        Log.systemLogEvent.append(self.onSystemLog)
        Log.userLogEvent.append(self.onUserLog)

    def onSystemLog(self, msg):
        op = self.form.output
        op.txtSys.configure(state=tk.NORMAL)
        op.txtSys.insert(tk.END, msg)
        op.txtSys.see(tk.END)
        op.txtSys.insert(tk.END, "\n")
        op.txtSys.configure(state=tk.DISABLED)

    def onUserLog(self, msg):
        op = self.form.output
        op.txtUser.configure(state=tk.NORMAL)
        op.txtUser.insert(tk.END, msg)
        op.txtUser.see(tk.END)
        op.txtUser.insert(tk.END, "\n")
        op.txtUser.configure(state=tk.DISABLED)
