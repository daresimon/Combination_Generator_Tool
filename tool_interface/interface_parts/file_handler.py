'''
Author: Desmond Goh
Date: 2021-03-16 20:44:45
LastEditTime: 2021-03-16 23:04:15
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/tool_interface/interface_parts/file_handler.py
'''
import tkinter as tk
import tkinter.filedialog as fd
from tool_interface.common.message_box import MessageBox

class FileHandler:

    def __init__(self, parent_frame, target_widget):
        self.target_widget = target_widget
        frm_file_handler = tk.Frame(parent_frame)
        frm_file_handler.grid(
            row=0,
            column=0,
            sticky='e',
            padx=5,
            pady=5
        )
        btn_save = tk.Button(
            frm_file_handler,
            text='Save as text file',
            command=self.save
        )
        btn_save.pack(side=tk.RIGHT)
        btn_open = tk.Button(
            frm_file_handler,
            text='Open text file',
            command=self.open
        )
        btn_open.pack(side=tk.RIGHT, padx=10)

    def save(self):
        f = fd.asksaveasfile(mode='w', defaultextension='.txt')
        self.solve_mac_dialog_bug()
        if f == None:
            return
        save_text = self.target_widget.get(1.0, 'end')
        f.write(save_text)
        f.close()

    def open(self):
        f = fd.askopenfile(mode='r', filetypes=[('Text Document', '*.txt')])
        self.solve_mac_dialog_bug()
        if f == None:
            return
        confirmation_message = MessageBox('Confirmation', 'Are you sure you want to open a file? Existing results will be overwritten')
        self.solve_mac_dialog_bug()
        if confirmation_message.ask_yes_no_box():
            show_text = f.read()
            self.target_widget.delete(1.0, 'end')
            self.target_widget.insert(1.0, show_text)

    def solve_mac_dialog_bug(self):
        '''
        on mac, dialog box will show again after changing windows
        this function is to resolve the issue
        '''
        tk._default_root.grab_set()
        tk._default_root.grab_release()