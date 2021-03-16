'''
Author: Desmond Goh
Date: 2521-03-13 14:36:29
LastEditTime: 2021-03-16 00:16:42
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/tool_interface/interface_parts/case_parameters_variables.py
'''
import tkinter as tk
from tool_interface.common.message_box import MessageBox

class CaseParameter:

    def __init__(self, parent_frame, param_num):
        '''
        initialise parameter label
        initialize parameter entry
        initialize frame with parameter type (combination/fixed)
        initialize frame with add/delete variable buttons
        '''
        self.param_frame = tk.Frame(parent_frame)
        self.var_row = 4
        self.var_list = []

        self.lbl_param_num = tk.Label(
            self.param_frame,
            text=f'Parameter {param_num+1}'
        )
        self.ent_param = tk.Entry(
            self.param_frame,
            width=25
        )

        frm_button = tk.Frame(self.param_frame)
        btn_add_var = tk.Button(
            frm_button,
            text='Add Variable',
            command=self.add_variable
        )
        btn_del_var = tk.Button(
            frm_button,
            text='Delete Variable',
            command=self.delete_variable
        )
        btn_add_var.pack(side=tk.LEFT)
        btn_del_var.pack(side=tk.LEFT, padx=5)
        
        frm_param_type = tk.Frame(self.param_frame)
        lbl_param_type = tk.Label(
            frm_param_type,
            text='Parameter type:'
        )
        self.param_type = tk.StringVar()
        self.param_type.set('Combination')
        self.chk_btn_type = tk.Checkbutton(
            frm_param_type,
            text=self.param_type.get(),
            variable=self.param_type,
            onvalue='Combination',
            offvalue='Fixed',
            command=self.change_type
        )
        lbl_param_type.pack(side=tk.LEFT)
        self.chk_btn_type.pack(side=tk.LEFT, padx=5)
        
        self.lbl_param_num.grid(
            row=0,
            column=0,
            sticky='w'
        )
        self.ent_param.grid(
            row=1,
            column=0,
            sticky='w', 
            pady=5
        )
        frm_param_type.grid(
            row=2,
            column=0,
            pady=5,
            sticky='w'
        )
        frm_button.grid(
            row=3,
            column=0,
            sticky='w',
            pady=5
        )
        '''
        require 1 variable by default
        '''
        self.add_variable()

    def add_variable(self):
        new_var = CaseVariable(self.param_frame, self.var_row)    
        self.var_row += 1
        self.var_list.append(new_var)
        '''
        can only be combination type when more than 1 variable
        '''
        if len(self.var_list) > 1:
            self.param_type.set('Combination')
            self.chk_btn_type['text'] = self.param_type.get()
            self.chk_btn_type['state'] = 'disabled'

    def delete_variable(self):
        if len(self.var_list) > 1:
            last_variable = self.var_list.pop()
            last_variable.ent_var.forget()
            last_variable.ent_var.destroy()
            if len(self.var_list) == 1:
                self.chk_btn_type['state'] = 'normal'
        else:
            error_message = MessageBox('Error', 'There must be at least 1 variable')
            error_message.error_message_box()
        
    def change_type(self):
        self.chk_btn_type['text'] = self.param_type.get()

class CaseVariable:
    
    def __init__(self, param_frame, var_row):
        self.ent_var = tk.Entry(
            param_frame,
            width=25
        )
        self.ent_var.grid(
            row=var_row, 
            column=0, 
            pady=5)