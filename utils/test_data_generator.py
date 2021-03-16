'''
Author: Desmond Goh
Date: 2021-01-24 21:20:02
LastEditTime: 2021-03-10 22:35:38
LastEditors: Desmond Goh
FilePath: /Testing_Technique_Sharing/utils/test_data_generator.py
'''
import random
import string

class DataRequirement:
    __start_range = 0
    __end_range = 0
    __length = 0
    __function_name = ''
    __fixed_value = ''
    __request_value = ''

    @property
    def request_value(self):
        return self.__request_value

    @request_value.setter
    def request_value(self, value):
        self.__request_value = value

    @property
    def fixed_value(self):
        return self.__fixed_value

    @fixed_value.setter
    def fixed_value(self, value):
        self.__fixed_value = value

    @property
    def function_name(self):
        return self.__function_name

    @function_name.setter
    def function_name(self, name):
        self.__function_name = name

    @property
    def start_range(self):
        return self.__start_range

    @start_range.setter
    def start_range(self, start):
        self.__start_range = start

    @property
    def end_range(self):
        return self.__end_range

    @end_range.setter
    def end_range(self, end):
        self.__end_range = end

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, l):
        self.__length = l

class TestDataGenerator:
        
    def generate_random_int(self, data_requirement):
        return random.randint(data_requirement.start_range, data_requirement.end_range)

    def generate_random_chars(self, data_requirement):
        chars = string.printable
        return ''.join([random.choice(chars) for i in range(data_requirement.length)])

    def generate_random_alphabets(self, data_requirement):
        chars = string.ascii_letters
        return ''.join([random.choice(chars) for i in range(data_requirement.length)])

    def generate_random_digits(self, data_requirement):
        chars = string.digits
        return ''.join([random.choice(chars) for i in range(data_requirement.length)])

    def generate_random_alphanumerics(self, data_requirement):
        chars = string.ascii_letters + string.digits
        return ''.join([random.choice(chars) for i in range(data_requirement.length)])

    def generate_random_float(self, data_requirement):
        return random.uniform(data_requirement.start_range, data_requirement.end_range)

    def configure_data(self, data_requirement):    
        '''
        get function from input value. 
        If input value does not match any functions, return input value
        '''
        if isinstance(data_requirement.request_value, str):                           
            func = getattr(self, data_requirement.request_value, data_requirement.request_value)
            if(func != data_requirement.request_value):
                configured_data = func(data_requirement)
            else:
                configured_data = func
            return configured_data
        return data_requirement.request_value