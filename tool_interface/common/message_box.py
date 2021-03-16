'''
Author: Desmond Goh
Date: 2021-03-15 16:31:11
LastEditTime: 2021-03-16 23:02:38
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/tool_interface/common/message_box.py
'''
import tkinter as tk
import tkinter.messagebox as mb

class MessageBox:

    def __init__(self, title, message):
        self.title = title
        self.message = message

    def solve_mac_dialog_bug(self):
        '''
        on mac, dialog box will show again after changing windows
        this function is to resolve the issue
        '''
        tk._default_root.grab_set()
        tk._default_root.grab_release()

    def info_message_box(self):
        dialog = mb.showinfo(self.title, self.message)
        self.solve_mac_dialog_bug()
        return dialog

    def warning_message_box(self):
        dialog = mb.showwarning(self.title, self.message)
        self.solve_mac_dialog_bug()
        return dialog

    def error_message_box(self):
        dialog = mb.showerror(self.title, self.message)
        self.solve_mac_dialog_bug()
        return dialog

    def ask_question_box(self):
        dialog = mb.askquestion(self.title, self.message)
        self.solve_mac_dialog_bug()
        return dialog

    def ask_ok_cancel_box(self):
        dialog = mb.askokcancel(self.title, self.message)
        self.solve_mac_dialog_bug()
        return dialog

    def ask_retry_cancel_box(self):
        dialog = mb.askretrycancel(self.title, self.message)
        self.solve_mac_dialog_bug()
        return dialog

    def ask_yes_no_box(self):
        dialog = mb.askyesno(self.title, self.message)
        self.solve_mac_dialog_bug()
        return dialog

    def ask_yes_no_cancel_box(self):
        dialog = mb.askyesnocancel(self.title, self.message)
        self.solve_mac_dialog_bug()
        return dialog
