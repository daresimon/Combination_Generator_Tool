'''
Author: Desmond Goh
Date: 2021-03-10 22:37:00
LastEditTime: 2021-03-16 23:56:56
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/src/model/combinations_generator.py
'''
import utils.test_data_generator as tdc
import copy

class CombinationsGenerator:
    __test_case_statement = ''
    __parameters_key_list = []
    __parameters_value_list = []
    __fixed_parameters_key_list = []
    __fixed_parameters_value_list = []

    @property
    def fixed_parameters_key_list(self):
        return self.__fixed_parameters_key_list

    @fixed_parameters_key_list.setter
    def fixed_parameters_key_list(self, key_list):
        self.__fixed_parameters_key_list = key_list

    @property
    def fixed_parameters_value_list(self):
        return self.__fixed_parameters_value_list

    @fixed_parameters_value_list.setter
    def fixed_parameters_value_list(self, value_list):
        self.__fixed_parameters_value_list = value_list

    @property
    def parameters_key_list(self):
        return self.__parameters_key_list

    @parameters_key_list.setter
    def parameters_key_list(self, key_list):
        self.__parameters_key_list = key_list

    @property
    def parameters_value_list(self):
        return self.__parameters_value_list

    @parameters_value_list.setter
    def parameters_value_list(self, value_list):
        self.__parameters_value_list = value_list

    @property
    def test_case_statement(self):
        return self.__test_case_statement

    @test_case_statement.setter
    def test_case_statement(self, statement):
        self.__test_case_statement = statement

    def form_test_case(self, combinations_list):
        """form test cases based on input parameters

        Returns:
            list: return list of test cases, 
                or return none if there are errors
        """        
        generate_test_case_list = []
        i=1
        try:
            for combination in combinations_list:
                formatted_case = f'Test case {i} of {self.test_case_statement}: '
                for each_key, each_value in zip(self.parameters_key_list, combination):
                    formatted_case += f'({each_key} = {each_value}) '
                generate_test_case_list.append(formatted_case)
                i+=1
        except (ValueError, TypeError):
            return None
        if len(self.fixed_parameters_key_list) > 0:
            final_list = []
            for each_case in generate_test_case_list:
                for each_key, each_value in zip(self.fixed_parameters_key_list, self.fixed_parameters_value_list):
                    each_case += f'({each_key} = {each_value})'
                final_list.append(each_case)
            return final_list
        return generate_test_case_list

    def form_test_data(self, combinations_list):
        """form test data based on input parameters

        Returns:
            list: return list of test cases, 
                or return none if there are errors
        """        
        generate_test_data_list = []
        try:
            test_data = {}
            for combination in combinations_list:
                for each_key, each_value in zip(self.parameters_key_list, combination):
                    test_data[each_key] = each_value
                generate_test_data_list.append(copy.copy(test_data))
        except (ValueError, TypeError):
            return None
        if len(self.fixed_parameters_key_list) > 0:
            final_list = []
            for each_data in generate_test_data_list:
                for each_key, each_value in zip(self.fixed_parameters_key_list, self.fixed_parameters_value_list):
                    each_data[each_key] = each_value
                final_list.append(copy.copy(each_data))
            return final_list
        return generate_test_data_list

    def generate_combinations(self):
        raise NotImplementedError

    def generate_test_case_list(self, case_statement):
        self.test_case_statement = case_statement
        combinations = self.generate_combinations()
        return self.form_test_case(combinations)

    def generate_test_data_list(self):
        data_requirement = tdc.DataRequirement()
        data_generator = tdc.TestDataGenerator()
        processed_list = []
        for each_param in self.parameters_value_list:
            each_param_processed_list = []
            for each_var in each_param:
                data_requirement.request_value = each_var.get('value')
                data_requirement.start_range = each_var.get('start_range')
                data_requirement.end_range = each_var.get('end_range')
                data_requirement.length = each_var.get('length')
                processed_value = data_generator.configure_data(copy.deepcopy(data_requirement))
                each_param_processed_list.append(processed_value)
            processed_list.append(each_param_processed_list)
        processed_fixed_list = []
        for each_var in self.fixed_parameters_value_list:
            data_requirement.request_value = each_var.get('value')
            data_requirement.start_range = each_var.get('start_range')
            data_requirement.end_range = each_var.get('end_range')
            data_requirement.length = each_var.get('length')
            processed_value = data_generator.configure_data(copy.deepcopy(data_requirement))
            processed_fixed_list.append(processed_value)
        self.fixed_parameters_value_list = processed_fixed_list
        self.parameters_value_list = processed_list
        combinations = self.generate_combinations()
        return self.form_test_data(combinations)