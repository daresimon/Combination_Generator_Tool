'''
Author: Desmond Goh
Date: 2021-03-15 16:28:12
LastEditTime: 2021-03-16 21:37:05
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/tool_interface/interface_parts/action_buttons.py
'''
import tkinter as tk

class ActionButtons:

    def __init__(self, parent_frame):

        self.btn_generate = tk.Button(
            parent_frame,
            text='Generate'
        )
        self.btn_reset = tk.Button(
            parent_frame,
            text='Reset All'
        )
        self.btn_generate.pack(side=tk.LEFT,padx=5)
        self.btn_reset.pack(side=tk.LEFT,padx=10)