'''
Author: Desmond Goh
Date: 2021-03-16 09:48:49
LastEditTime: 2021-03-17 00:23:19
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/src/input_processor.py
'''
import json
from src.pairs_generator import PairsGenerator as pg
from src.orthogonal_array_generator import OrthogonalArrayGenerator as oag
from tool_interface.common.message_box import MessageBox

class InputProcessor:

    def __init__(self, param_list, generator_type):
        self.param_list = param_list
        self.generator_type = generator_type

    def process_test_case(self, test_case_statement):
        '''
        form params and var list and validate input
        '''
        input_validation = self.validate_case_input(self.param_list, test_case_statement)
        if input_validation != '':
            input_error = MessageBox('Error', input_validation)
            input_error.error_message_box()
            return None
        fixed_param_list = []
        fixed_param_var_list = []
        combination_param_list = []
        combination_param_var_list = []
        for param in self.param_list:
            parameter_type = param.param_type.get()
            parameter = param.ent_param.get()
            var_list = []
            for var in param.var_list:
                var_list.append(var.ent_var.get())
            if parameter_type == 'Combination':
                combination_param_list.append(parameter)
                combination_param_var_list.append(var_list)
            elif parameter_type == 'Fixed':
                fixed_param_list.append(parameter)
                fixed_param_var_list.append(var_list[0]) #fixed param only has 1 var       
        '''
        generate cases
        '''
        if self.generator_type == 'orthogonal':
            generator = oag(combination_param_list, combination_param_var_list, fixed_param_list, fixed_param_var_list)
        else:
            generator = pg(combination_param_list, combination_param_var_list, fixed_param_list, fixed_param_var_list)
            
        generate_test_case_list = generator.generate_test_case_list(test_case_statement)
        if generate_test_case_list == None:
            return generate_test_case_list
        result_string = ''
        for test_case in generate_test_case_list:
            result_string += f'{test_case}\n'
        return result_string

    def process_test_data(self):
        '''
        form params and var list and validate input
        '''
        input_validation = self.validate_data_input(self.param_list)
        if input_validation != '':
            input_error = MessageBox('Error', input_validation)
            input_error.error_message_box()
            return None
        fixed_param_list = []
        fixed_param_var_list = []
        combination_param_list = []
        combination_param_var_list = []
        for param in self.param_list:
            parameter_type = param.param_type.get()
            parameter = param.ent_param.get()
            var_list = []
            for var in param.var_list:
                var_dict = self.get_var_dict(
                    var.cmb_var.get(), 
                    var.ent_var.get(),
                    var.spin_start.get(),
                    var.spin_end.get(),
                    var.spin_length.get()
                )
                var_list.append(var_dict)
            if parameter_type == 'Combination':
                combination_param_list.append(parameter)
                combination_param_var_list.append(var_list)
            elif parameter_type == 'Fixed':
                fixed_param_list.append(parameter)
                fixed_param_var_list.append(var_list[0]) #fixed param only has 1 var
        '''
        generate data
        '''
        if self.generator_type == 'orthogonal':
            generator = oag(combination_param_list, combination_param_var_list, fixed_param_list, fixed_param_var_list)
        else:
            generator = pg(combination_param_list, combination_param_var_list, fixed_param_list, fixed_param_var_list)
            
        generate_test_data_list = generator.generate_test_data_list()
        if generate_test_data_list == None:
            return generate_test_data_list
        result_string = ''
        i=1
        for test_data in generate_test_data_list:
            result_string += f'Dataset {i}: {json.dumps(test_data)}\n'
            i+=1
        return result_string

    def get_var_dict(self, var_type, ent_value, start_range, end_range, length_value):
        var_dict = {}
        if var_type == 'Manual Input: String':
            var_dict = {'value': ent_value}
        if var_type == 'Manual Input: Int':
            var_dict = {'value': int(ent_value)}
        if var_type == 'Manual Input: Float':
            var_dict = {'value': float(ent_value)}
        if var_type == 'Generate Int':
            var_dict = {'value': 'generate_random_int', 'start_range': int(start_range) ,'end_range': int(end_range)}
        if var_type == 'Generate Characters':
            var_dict = {'value': 'generate_random_chars', 'length': int(length_value)}
        if var_type == 'Generate Alphabets':
            var_dict = {'value': 'generate_random_alphabets', 'length': int(length_value)}
        if var_type == 'Generate Digits':
            var_dict = {'value': 'generate_random_digits', 'length': int(length_value)}
        if var_type == 'Generate Alphanumerics':
            var_dict = {'value': 'generate_random_alphanumerics', 'length': int(length_value)}
        if var_type == 'Generate Float':
            var_dict = {'value': 'generate_random_float', 'start_range': int(start_range) ,'end_range': int(end_range)}
        return var_dict

    def validate_case_input(self, param_list, statement):
        input_validation = ''
        parameter_error = 'Parameter input cannot be empty\n\n'
        entry_error = 'Variable input cannot be empty\n\n'
        if statement == '':
            input_validation += 'Test Case Statement cannot be empty\n\n'
        for param in param_list:
            if param.ent_param.get() == '' and parameter_error not in input_validation:
                input_validation += parameter_error
            for var in param.var_list:
                ent_value = var.ent_var.get()
                if ent_value == '' and entry_error not in input_validation:
                    input_validation += entry_error
        return input_validation

    def validate_data_input(self, param_list):
        input_validation = ''
        parameter_error = 'Parameter input cannot be empty\n\n'
        entry_error = 'Variable input cannot be empty\n\n'
        length_error = 'Variable length cannot be empty\n\n'
        start_error = 'Variable start range cannot be empty\n\n'
        end_error = 'Variable end range cannot be empty\n\n'
        range_error = 'Start range must be lower than end range\n\n'
        for param in param_list:
            if param.ent_param.get() == '' and parameter_error not in input_validation:
                input_validation += parameter_error
            for var in param.var_list:
                var_type = var.cmb_var.get()
                ent_value = var.ent_var.get()
                start_range = var.spin_start.get()
                end_range = var.spin_end.get()
                length_value = var.spin_length.get()
                if var_type in ['Manual Input: String', 'Manual Input: Int', 'Manual Input: Float']:
                    if ent_value == '' and entry_error not in input_validation:
                        input_validation += entry_error
                if var_type in ['Generate Int', 'Generate Float']:
                    if start_range == '' and start_error not in input_validation:
                        input_validation += start_error
                    if end_range == '' and end_error not in input_validation:
                        input_validation += end_error
                    if start_range > end_range and range_error not in input_validation:
                        input_validation += range_error
                if var_type in ['Generate Characters', 'Generate Alphabets', 'Generate Digits', 'Generate Alphanumerics']:
                    if length_value == '' and length_error not in input_validation:
                        input_validation += length_error
        return input_validation
        