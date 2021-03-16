'''
Author: Desmond Goh
Date: 2021-03-13 13:06:01
LastEditTime: 2021-03-15 22:46:49
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/tool_interface/interface_parts/test_case_statement.py
'''
import tkinter as tk

class TestCaseStatement:
    def __init__(self, parent_frame):
        '''
        initialize test case statement label
        initialize test case sttaement entry
        '''
        lbl_statement = tk.Label(
            parent_frame,
            text='Input test case statement:'
        )
        self.ent_statement = tk.Entry(
            parent_frame,
            width=100
        )
        lbl_statement.grid(row=0,column=0)
        self.ent_statement.grid(row=0,column=1)

