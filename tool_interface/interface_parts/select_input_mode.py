'''
Author: Desmond Goh
Date: 2021-03-13 12:52:32
LastEditTime: 2021-03-15 22:46:32
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/tool_interface/interface_parts/select_input_mode.py
'''
import tkinter as tk
    
class SelectInputMode:    

    def __init__(self, parent_frame):
        '''
        initialize input mode label
        initialize input mode checkbox
        '''
        self.selected_mode = tk.StringVar()
        self.selected_mode.set('case')

        lbl_mode = tk.Label(
            parent_frame, 
            text='Choose input mode:'
        )
        self.chk_btn_case = tk.Checkbutton(
            parent_frame,
            text='Test Case Mode',
            variable=self.selected_mode,
            onvalue='case',
            offvalue='case'
        )
        self.chk_btn_data = tk.Checkbutton(
            parent_frame,
            text='Test Data Mode',
            variable=self.selected_mode,
            onvalue='data',
            offvalue='data'
        )
        lbl_mode.grid(row=0,column=0, padx=[0,10])
        self.chk_btn_case.grid(row=0,column=1)
        self.chk_btn_data.grid(row=0,column=2)
        