'''
Author: Desmond Goh
Date: 2521-03-13 14:36:29
LastEditTime: 2021-03-17 00:19:22
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/tool_interface/interface_parts/data_parameters_variables.py
'''
import tkinter as tk
import tkinter.ttk as ttk
from tool_interface.common.message_box import MessageBox

class DataParameter:

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
        new_var = DataVariable(self.param_frame, self.var_row)
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
            last_variable.variable_frame.forget()
            last_variable.variable_frame.destroy()
            if len(self.var_list) == 1:
                self.chk_btn_type['state'] = 'normal'
        else:
            error_message = MessageBox('Error', 'There must be at least 1 variable')
            error_message.error_message_box()
        
    def change_type(self):
        self.chk_btn_type['text'] = self.param_type.get()

class DataVariable:
    
    __variable_choice = [
        'Manual Input: String',
        'Manual Input: Int',
        'Manual Input: Float',
        'Generate Int',
        'Generate Float',
        'Generate Characters',
        'Generate Alphabets',
        'Generate Digits',
        'Generate Alphanumerics'
    ]

    def __init__(self, param_frame, var_row):
        self.variable_frame = tk.Frame(
            param_frame, 
            borderwidth=1, 
            relief=tk.SOLID
        )
        self.variable_frame.grid(
            row=var_row, 
            column=0, 
            pady=5,
            sticky='w'
        )

        self.cmb_var = ttk.Combobox(
            self.variable_frame,
            values=self.__variable_choice,
            state='readonly'
        )
        self.cmb_var.grid(
            row=0, 
            column=0, 
            sticky='w',
            padx=5,
            pady=5
        )
        self.cmb_var.bind(
            '<<ComboboxSelected>>',
            self.select_var_type
        )
        self.cmb_var.current(0)
        
        self.input_frame = tk.Frame(self.variable_frame)
        self.input_frame.grid(
            row=1,
            column=0,
            sticky='w',
            padx=5,
            pady=5
        )
        self.ent_var = tk.Entry(
            self.input_frame,
            width=20
        )
        
        self.spin_frame = tk.Frame(self.input_frame)
        lbl_start = tk.Label(
            self.spin_frame,
            text='Start Range'
        )
        lbl_stop = tk.Label(
            self.spin_frame,
            text='End Range'
        )
        self.spin_start = ttk.Spinbox(
            self.spin_frame,
            from_=0,
            to=100000000,
            width=10
        )
        self.spin_end = ttk.Spinbox(
            self.spin_frame,
            from_=0,
            to=100000000,
            width=10
        )
        lbl_start.grid(
            row=0,
            column=0
        )
        self.spin_start.grid(
            row=0,
            column=1
        )
        lbl_stop.grid(
            row=1,
            column=0
        )
        self.spin_end.grid(
            row=1,
            column=1
        )
        
        self.spin_length_frame = tk.Frame(self.input_frame)
        lbl_length = tk.Label(
            self.spin_length_frame,
            text='Length'
        )
        self.spin_length = ttk.Spinbox(
            self.spin_length_frame,
            from_=0,
            to=100000000,
            width=10
        )
        lbl_length.pack(side=tk.LEFT)
        self.spin_length.pack(side=tk.LEFT)

        '''
        prevent changes by scrolling
        '''
        self.cmb_var.unbind_class('TCombobox', '<MouseWheel>')
        # Linux and other *nix systems:
        self.cmb_var.unbind_class("TCombobox", "<ButtonPress-4>")
        self.cmb_var.unbind_class("TCombobox", "<ButtonPress-5>")
        self.spin_start.bind('<MouseWheel>', self.disable_spinbox_scroll)
        self.spin_end.bind('<MouseWheel>', self.disable_spinbox_scroll)
        self.spin_length.bind('<MouseWheel>', self.disable_spinbox_scroll)

        '''
        default manual input for string
        '''
        self.ent_var.grid(
            row=0,
            column=0,
        )

    def select_var_type(self,event):
        self.reset_var()
        var_type = event.widget.get()
        if var_type == 'Manual Input: String':
            vcmd = self.input_frame.register(self.no_validation)
            self.ent_var.configure(
                validate='all',
                validatecommand=(vcmd, '%P')
            )
            self.ent_var.grid(
                row=0,
                column=0,
            )
        elif var_type == 'Manual Input: Int':
            vcmd = self.input_frame.register(self.validate_int)
            self.ent_var.configure(
                validate='all',
                validatecommand=(vcmd, '%P')
            )
            self.ent_var.grid(
                row=0,
                column=0,
            )
        elif var_type == 'Manual Input: Float':
            vcmd = self.input_frame.register(self.validate_float)
            self.ent_var.configure(
                validate='all',
                validatecommand=(vcmd, '%P')
            )
            self.ent_var.grid(
                row=0,
                column=0,
            )
        elif var_type in ['Generate Int', 'Generate Float']:
            vcmd = self.input_frame.register(self.validate_range)
            self.spin_start.configure(
                validate='all',
                validatecommand=(vcmd, '%P')
            )
            self.spin_end.configure(
                validate='all',
                validatecommand=(vcmd, '%P')
            )
            self.spin_frame.grid(
                row=0,
                column=0,
            )
        elif var_type in ['Generate Characters', 'Generate Alphabets', 'Generate Digits', 'Generate Alphanumerics']:
            vcmd = self.input_frame.register(self.validate_range)
            self.spin_length.configure(
                validate='all',
                validatecommand=(vcmd, '%P')
            )
            self.spin_length_frame.grid(
                row=0,
                column=0,
            )

    def reset_var(self):
        self.ent_var.grid_forget()
        self.ent_var.delete(0, 'end')
        self.spin_frame.grid_forget()
        self.spin_start.set('')
        self.spin_end.set('')
        self.spin_length_frame.grid_forget()
        self.spin_length.set('')

    def no_validation(self, user_input):
        return True

    def validate_int(self, user_input):
        if str.isdigit(user_input) or user_input == '':
            return True
        else:
            return False
    
    def validate_float(self, user_input):
        if user_input == '':
            return True
        else:
            try:
                float(user_input)
                return True
            except ValueError:
                return False

    def validate_range(self, user_input):
        if user_input.isdigit():
            minval = 0
            maxval = 100000001
            if int(user_input) not in range(minval, maxval):
                return False
            return True
        elif user_input == '':
            return True
        else:
            return False

    def disable_spinbox_scroll(self, event):
        '''
        prevent changing option by scrolling
        '''
        return 'break'