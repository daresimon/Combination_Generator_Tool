'''
Author: Desmond Goh
Date: 2021-01-24 23:48:43
LastEditTime: 2021-03-16 23:52:57
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/src/orthogonal_array_generator.py
'''
import numpy as np
import pandas as pd
import src.resources.orthogonal_array_list as oa
import src.model.combinations_generator as cg
import utils.test_data_generator as tdc
import copy

class OrthogonalArrayGenerator(oa.OrthogonalArrayList, cg.CombinationsGenerator):
    __strength = 2
    __factors_and_levels_list = []
    __sort_key_index = []

    def __init__(self, key_list, value_list, fixed_key_list, fixed_value_list):
        self.parameters_key_list = key_list
        self.parameters_value_list = value_list
        self.fixed_parameters_key_list = fixed_key_list
        self.fixed_parameters_value_list = fixed_value_list

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, stre):
        self.__strength = stre

    def __get_factors_and_levels_list(self):
        '''
        based on input data, form list of factors and levels
        factors: number of parameters with the same level
        levels: number of variable in input 
        '''
        self.__factors_and_levels_list = []
        j=0
        for levels in self.parameters_value_list:
            i = 0
            for each_set in self.__factors_and_levels_list:
                if len(levels) == each_set.get('levels'):
                    each_set['factors'] += 1
                    i+=1
                    each_set.get('index', []).append(j)
            if i == 0: #append if there's no factors with this number of levels
                self.__factors_and_levels_list.append({'factors':1,'levels':len(levels), 'index': [j]})
            j+=1
        #print(f'factors and levels: {self.__factors_and_levels_list}')
    
    def __find_matching_fixed_array(self):
        '''
        returns information of array that can fully map input data
        '''
        levels = self.__factors_and_levels_list[0].get('levels')
        factors = self.__factors_and_levels_list[0].get('factors')
        '''
        find suitable set
        '''
        if levels not in self.OA_fixed_levels_list:
            oa_list = self.OA_mixed_levels_strength_2
        elif levels == 2:
            oa_list = self.OA_2_levels
        elif levels == 3:
            oa_list = self.OA_3_levels
        else:
            oa_list = self.OA_fixed_levels
        '''
        find specific array information
        '''
        return self.__match_one_level(factors, oa_list)

    def __match_one_level(self, factors, oa_list):
        '''
        return information of specific array
        '''
        for oa in oa_list.get('OA'):
            if(oa.get('strength') != self.__strength):
                continue
            if factors == oa.get('factors'):
                return {'id': oa.get('id'), 'runs': oa.get('runs'), 'factors': factors, 'file': oa_list.get('file')}
            if factors < oa.get('factors'):
                return {'id': oa.get('id'), 'runs': oa.get('runs'), 'factors': factors, 'file': oa_list.get('file')}
        return None
    
    def __find_matching_mixed_array(self):
        '''
        returns information of list of array that can fully map input data
        '''
        suitable_array_id_list = []
        input_factors_list = []
        input_levels_list = []
        for each_set in self.__factors_and_levels_list:
            input_factors_list.append(each_set.get('factors'))
            input_levels_list.append(each_set.get('levels'))
        '''
        find suitable array list
        '''
        if max(input_levels_list) == 2:
            suitable_array_id_list.append(self.__match_one_level(sum(input_factors_list), self.OA_2_levels)) #get array from oa_2
        if max(input_levels_list) == 3:
            if input_factors_list == [1,1] and 2 in input_levels_list:
                return {'id': 1, 'file': 'src/resources/OA_mixed.csv'} #special case
            suitable_array_id_list.append(self.__match_one_level(sum(input_factors_list), self.OA_3_levels)) #get array from oa_3
        oa_list = self.OA_mixed_levels_strength_2
        for oa in oa_list.get('OA'):
            if len(suitable_array_id_list) > 0:
                if oa.get('runs') > suitable_array_id_list[len(suitable_array_id_list) -1].get('runs'): #already obtained least run possible
                    break
            oa_factors_list = []
            oa_levels_list = []
            for each_set in oa.get('factors_and_levels'):
                oa_factors_list.append(each_set[0])
                oa_levels_list.append(each_set[1])
                if max(input_levels_list) <= max(oa_levels_list):
                    fitting = self.__match_multiple_levels(copy.copy(input_levels_list), copy.copy(input_factors_list), 
                        copy.copy(oa_levels_list), copy.copy(oa_factors_list))
                    if fitting != False:
                        suitable_array_id_list.append({'id': oa.get('id'), 'runs': oa.get('runs'), 
                            'factors': sum(oa_factors_list), 'file': oa_list.get('file'), 'oversize_count': fitting})
        if len(suitable_array_id_list) < 1:
            return None
        best_fit_array = self.__get_best_fit_array(suitable_array_id_list)
        return best_fit_array
           
    def __match_multiple_levels(self, input_levels, input_factors, oa_levels, oa_factors):
        '''
        check if array matches
        returns number of factors that are oversized (i.e. level 3 used for level 2)
        oversized count used for determination of best fit array
        '''
        oversize_count = 0
        for element in input_levels: #iterate all elements from highest level to lowest
            if max(input_levels) in oa_levels: #if current highest level in OA
                input_index = input_levels.index(max(input_levels)) #get index to get number of factors at the level
                oa_index = oa_levels.index(max(input_levels))
                oa_factors[oa_index] -= input_factors[input_index]  #check if OA has matching number of factors
                if oa_factors[oa_index] < 0:  #if OA has less factors
                    if max(oa_levels) > max(input_levels): #check if OA has higher level to match
                        new_oa_index = oa_levels.index(max(oa_levels))
                        oa_factors[new_oa_index] += oa_factors[oa_index]
                        if oa_factors[new_oa_index] < 0: #if higher level not enough to match, return false
                            return False
                        if oa_factors[new_oa_index] == 0:
                            oa_levels[new_oa_index] = 0 #set level to 0 if all factors has been 'used up'
                        oa_factors[oa_index] = 0 #if higher level can match, set to 0 factors at previous level
                        oa_levels[oa_index] = 0 #set level to 0 as it's been 'used up'
                        oversize_count += 1
                    else:
                        return False #if OA has no higher level, return false
                if oa_factors[oa_index] == 0:
                    oa_levels[oa_index] = 0
                input_levels[input_index] = 0 #set levels to 0 as it's been matched
                input_factors[input_index] = 0 #set factors to 0 as it's been matched
            elif max(oa_levels) > max(input_levels): #if OA has higher level than input
                max_input_index = input_levels.index(max(input_levels))
                max_oa_index = oa_levels.index(max(oa_levels))
                oa_factors[max_oa_index] -= input_factors[max_input_index]
                if oa_factors[max_oa_index] < 0: #if OA has less factors, return false 
                    return False
                if oa_factors[max_oa_index] == 0:
                    oa_levels[max_oa_index] = 0 #set levels to 0 as it's been 'used up'
                input_levels[max_input_index] = 0 #set levels to 0 as it's been matched
                input_factors[max_input_index] = 0 #set factors to 0 as it's been matched
                oversize_count +=1
            else:
                return False
        return oversize_count

    def __get_best_fit_array(self, suitable_array_id_list):
        '''
        return dictionary with information of best fitting array
        '''
        best_array = {'id': 0, 'runs': 999, 'factors': 999, 'file': ''} #placeholder values
        for each_array in suitable_array_id_list:
            if best_array.get('runs') > each_array.get('runs'):
                best_array = each_array
            elif best_array.get('runs') == each_array.get('runs'):
                if best_array.get('oversize_count', 0) > each_array.get('oversize_count', 0):
                    best_array = each_array
                elif best_array.get('oversize_count', 0) == each_array.get('oversize_count', 0):
                    if best_array.get('factors') > each_array.get('factors'):
                        best_array = each_array
        #print(f'best fit array: {best_array}')
        return best_array

    def __get_array_shape(self, request_array):
        '''
        return actual array shape
        '''
        df = pd.read_csv(request_array.get('file'))
        df.loc[:,'id'] = df.loc[:,'id'].ffill() #fill up all id rows for matching
        specific_df = df.loc[df['id'] == request_array.get('id')].drop('id',1) #remove id column
        specific_df = specific_df.dropna(axis=1).astype(int).astype(object) #remove all columns with na and set as int type
        array_shape = specific_df.to_numpy() 
        #print(f'array shape: {array_shape}')
        return array_shape

    def __map_array(self, array_shape):
        '''
        map values from array to actual input
        return mapped array
        '''
        self.__sort_key_index = [] #array is not in input order, sort_key_index helps to show correct parameter
        input_factors_list = []
        input_levels_list = []
        input_index_list = []
        for each_set in self.__factors_and_levels_list:
            for i in range(len(each_set.get('index'))):
                input_factors_list.append(1)
            for i in range(len(each_set.get('index'))):
                input_levels_list.append(each_set.get('levels'))
            for i in each_set.get('index'):
                input_index_list.append(i) #to handle multiple of same levels
        column_list = list(range(0, len(array_shape[0])))
        i = 0
        while len(column_list) > 0:
            iterate_column_list = column_list.copy()
            column_list = []
            del_offset = 0
            for column in iterate_column_list: #iterate and match everything that is a perfect fit
                if len(input_factors_list) == 0: #remove remaining columns if everything has been mapped
                    del_index = column - del_offset
                    array_shape = np.delete(array_shape, del_index, 1)
                    del_offset += 1
                    continue
                current_factor = array_shape[:,column]
                factor_level = (max(current_factor) + 1)    #+1 because index starts from 0 
                factor_level -= i                           #deduct current factor by 1 after each columns iteration
                if factor_level not in input_levels_list: #skip factors that don't have perfect match
                    column_list.append(column)
                    continue
                index_value = input_levels_list.index(factor_level)
                parameter_index = input_index_list[index_value]
                if input_factors_list[index_value] == 0:
                    column_list.append(column)
                    continue
                input_factors_list[index_value] -= 1
                del input_factors_list[index_value]
                del input_levels_list[index_value]
                del input_index_list[index_value]
                self.__sort_key_index.append(parameter_index) 
                j=0 #iterate through variables of a factor
                k=0 #for oversized factors, alternate variable
                for element in current_factor:
                    if element > (len(self.parameters_value_list[parameter_index]) -1):
                        array_shape[j][column] = self.parameters_value_list[parameter_index][k]
                        k+=1
                        j+=1
                        if k > (len(self.parameters_value_list[parameter_index]) -1):
                            k=0
                        continue
                    array_shape[j][column] = self.parameters_value_list[parameter_index][element]
                    j+=1
            i+=1
        #print(f'mapped array: {array_shape}')
        return array_shape

    def generate_combinations(self):
        '''
        generate combinations based on array
        '''
        self.__get_factors_and_levels_list() #get factors and levels from parameters input
        if len(self.__factors_and_levels_list) == 1:
            request_array = self.__find_matching_fixed_array()
        else:
            request_array = self.__find_matching_mixed_array()
        if request_array == None:
            return None
        array_shape = self.__get_array_shape(request_array)
        mapped_array = self.__map_array(array_shape)
        self.parameters_key_list = self.reorder_keys()
        return mapped_array

    def reorder_keys(self):
        '''
        reorder keys according to mapped shape
        '''
        reordered_list = []
        for each_index in self.__sort_key_index:
            key = self.parameters_key_list[each_index]
            reordered_list.append(key)
        return reordered_list
