'''
Author: Desmond Goh
Date: 2021-01-24 16:27:30
LastEditTime: 2021-03-16 23:31:55
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/src/pairs_generator.py
'''
from allpairspy import AllPairs
import src.model.combinations_generator as cg

class PairsGenerator(cg.CombinationsGenerator):

    def __init__(self, key_list, value_list, fixed_key_list, fixed_value_list):
        self.parameters_key_list = key_list
        self.parameters_value_list = value_list
        self.fixed_parameters_key_list = fixed_key_list
        self.fixed_parameters_value_list = fixed_value_list

    def generate_combinations(self):
        return list(AllPairs(self.parameters_value_list))