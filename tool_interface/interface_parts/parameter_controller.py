'''
Author: Desmond Goh
Date: 2021-03-15 20:30:51
LastEditTime: 2021-03-16 21:34:29
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/tool_interface/interface_parts/parameter_controller.py
'''
import tkinter as tk
from tool_interface.interface_parts.case_parameters_variables import CaseParameter
from tool_interface.interface_parts.data_parameters_variables import DataParameter
from tool_interface.common.message_box import MessageBox

class ParameterController:
    
    def __init__(self, parent_frame, input_type):
        '''
        initialize add/delete parameter buttons
        initialize new parameter when add param clicked
        '''
        self.frame = parent_frame
        self.num_param = 0
        self.param_list = []
        self.input_type = input_type
        btn_add_param = tk.Button(
            self.frame,
            text='Add Parameter',
            command=self.add_param
        )
        btn_add_param.grid(
            row=0,
            column=0, 
            sticky='w', 
            padx=5,
            pady=5,
        )
        '''
        2 parameter minimally
        '''
        self.add_param()
        self.add_param()

    def add_param(self):
        if self.input_type == 'data':
            new_param = DataParameter(self.frame, self.num_param)
        else:
            new_param = CaseParameter(self.frame, self.num_param)
            
        new_param.param_frame.grid(
            row=1, 
            column=self.num_param, 
            sticky='n',
            padx=5
        )

        '''
        handle delete button at parent level to coordinate all parameters position/number
        '''
        btn_del_param = tk.Button(
            new_param.param_frame,
            text='Delete Parameter',
            command=lambda column=self.num_param, param_object=new_param: self.delete_param(column, param_object)
        )
        btn_del_param.grid(row=0,column=0, sticky='e')

        self.num_param += 1
        self.param_list.append(new_param)

    def delete_param(self, column, param_object):
        '''
        remove parameter object
        '''
        if len(self.param_list) > 2:
            delete_frame = param_object.param_frame
            delete_frame.forget()
            delete_frame.destroy()
            object_index = self.param_list.index(param_object)
            self.num_param -= 1
            self.param_list.remove(param_object)
            
            '''
            adjust other frames and label
            '''
            for param in self.param_list[object_index:]:
                frame = param.param_frame
                frame_column = frame.grid_info()['column']
                frame.grid(
                    row=1,
                    column = frame_column-1,
                    sticky='n'
                )
                lbl_param = param.lbl_param_num
                lbl_param['text'] = f'Parameter {frame_column}'
        else:
            error_message = MessageBox('Error', 'There must be at least 2 parameters')
            error_message.error_message_box()