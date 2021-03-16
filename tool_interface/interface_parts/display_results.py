'''
Author: Desmond Goh
Date: 2021-03-14 17:02:42
LastEditTime: 2021-03-16 21:31:43
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/tool_interface/interface_parts/display_results.py
'''
import tkinter as tk

class DisplayResult:

    def __init__(self, parent_frame):
        '''
        initialize results label
        initialize results text box
        '''
        lbl_results = tk.Label(
            parent_frame,
            text='Generated Results',
        )
        self.txt_result = tk.Text(
            parent_frame,
            width=150,
            height=20,
            borderwidth=2,
            relief=tk.SOLID,
            wrap=tk.WORD,
            cursor='arrow',
            highlightthickness=0
        )
        '''
        prevent user input
        '''
        self.txt_result.bind('<Key>', lambda e: 'break')
        lbl_results.grid(
            row=0, 
            column=0,
            sticky='w',
        )
        self.txt_result.grid(
            row=1,
            column=0,
            sticky='w'
        )
        self.txt_result.bind('<<Copy>>', self.copy_text)

    def copy_text(self, event):
        self.txt_result.selection_get()

    def get_all_text(self):
        return self.txt_result.get(1.0, 'end')