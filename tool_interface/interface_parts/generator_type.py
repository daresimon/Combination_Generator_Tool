'''
Author: Desmond Goh
Date: 2021-03-16 13:57:36
LastEditTime: 2021-03-16 14:10:06
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/tool_interface/interface_parts/generator_type.py
'''
import tkinter as tk

class GeneratorType:

    def __init__(self, parent_frame):
        '''
        initialize generator type label
        initialize generator type checkbox
        '''
        self.selected_generator = tk.StringVar()

        lbl_mode = tk.Label(
            parent_frame, 
            text='Choose generator type:'
        )
        self.chk_btn_pairs = tk.Checkbutton(
            parent_frame,
            text='All Pairs',
            variable=self.selected_generator,
            onvalue='pairs',
            offvalue='pairs'
        )
        self.chk_btn_orthogonal = tk.Checkbutton(
            parent_frame,
            text='Orthogonal Array',
            variable=self.selected_generator,
            onvalue='orthogonal',
            offvalue='orthogonal'
        )
        lbl_mode.grid(row=0,column=0, padx=[0,10])
        self.chk_btn_pairs.grid(row=0,column=1)
        self.chk_btn_orthogonal.grid(row=0,column=2)