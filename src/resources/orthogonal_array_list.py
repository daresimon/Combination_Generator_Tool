'''
Author: Desmond Goh
Date: 2021-01-25 21:10:01
LastEditTime: 2021-03-16 10:02:24
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/src/resources/orthogonal_array_list.py
'''
class OrthogonalArrayList:
    
    OA_fixed_levels_list = [2, 3, 4, 5, 7, 8, 9]

    OA_2_levels = {'file': 'src/resources/OA_2.csv', 'OA': [
        {'id': 1, 'runs': 4, 'factors': 3, 'strength': 2},
        {'id': 2, 'runs': 8, 'factors': 5, 'strength': 2},
        {'id': 3, 'runs': 8, 'factors': 7, 'strength': 2},
        {'id': 4, 'runs': 12, 'factors': 11, 'strength': 2},
        {'id': 5, 'runs': 16, 'factors': 15, 'strength': 2},
        {'id': 6, 'runs': 20, 'factors': 19, 'strength': 2},
        {'id': 7, 'runs': 8, 'factors': 4, 'strength': 3},
        {'id': 8, 'runs': 16, 'factors': 8, 'strength': 3},
        {'id': 9, 'runs': 24, 'factors': 12, 'strength': 3},
        {'id': 10, 'runs': 32, 'factors': 16, 'strength': 3},
        {'id': 11, 'runs': 40, 'factors': 20, 'strength': 3},
        {'id': 12, 'runs': 48, 'factors': 24, 'strength': 3},
        {'id': 13, 'runs': 80, 'factors': 6, 'strength': 4},
        {'id': 14, 'runs': 128, 'factors': 9, 'strength': 5},
        {'id': 15, 'runs': 64, 'factors': 7, 'strength': 6}
    ]}

    OA_3_levels = {'file': 'src/resources/OA_3.csv', 'OA': [
        {'id': 1, 'runs': 9, 'factors': 4, 'strength': 2},
        {'id': 2, 'runs': 18, 'factors': 7, 'strength': 2},
        {'id': 3, 'runs': 27, 'factors': 13, 'strength': 2},
        {'id': 4, 'runs': 81, 'factors': 40, 'strength': 2},
        {'id': 5, 'runs': 54, 'factors': 5, 'strength': 3},
    ]}

    OA_fixed_levels = {'file': 'src/resources/OA_fixed.csv', 'OA': [
        {'id':1, 'runs': 16, 'factors': 5, 'levels': 4, 'strength': 2},
        {'id':2, 'runs': 32, 'factors': 9, 'levels': 4, 'strength': 2},
        {'id':3, 'runs': 64, 'factors': 21, 'levels': 4, 'strength': 2},
        {'id':4, 'runs': 64, 'factors': 6, 'levels': 4, 'strength': 3},
        {'id':5, 'runs': 256, 'factors': 17, 'levels': 4, 'strength': 3},
        {'id':7, 'runs': 25, 'factors': 6, 'levels': 5, 'strength': 2},
        {'id':8, 'runs': 50, 'factors': 11, 'levels': 5, 'strength': 2},
        {'id':9, 'runs': 49, 'factors': 8, 'levels': 7, 'strength': 2},
        {'id':10, 'runs': 98, 'factors': 15, 'levels': 7, 'strength': 2},
        {'id':11, 'runs': 64, 'factors': 9, 'levels': 8, 'strength': 2},
        {'id':12, 'runs': 128, 'factors':17 , 'levels': 8, 'strength': 2},
        {'id':13, 'runs': 81, 'factors': 10, 'levels': 9, 'strength': 2},
        ''' future plan
        {'id':14, 'runs': 162, 'factors': 19, 'levels': 9, 'strength': 2},
        {'id':15, 'runs': 100, 'factors': 4, 'levels': 10, 'strength': 2},
        {'id':16, 'runs': 121, 'factors': 12, 'levels': 11, 'strength': 2},
        {'id':17, 'runs': 242, 'factors': 23, 'levels': 11, 'strength': 2},
        {'id':18, 'runs': 144, 'factors': 7, 'levels': 12, 'strength': 2},
        {'id':19, 'runs': 169, 'factors': 14, 'levels': 13, 'strength': 2},
        {'id':20, 'runs': 256, 'factors': 17, 'levels': 16, 'strength': 2},
        {'id':21, 'runs': 512, 'factors': 33, 'levels': 16, 'strength': 2},
        {'id':22, 'runs': 289, 'factors': 18, 'levels': 17, 'strength': 2},
        '''
    ]}

    OA_mixed_levels_strength_2 = {'file': 'src/resources/OA_mixed.csv', 'OA': [
        {'id':1, 'runs': 6, 'factors_and_levels': [[1,2],[1,3]]},
        {'id':2, 'runs': 8, 'factors_and_levels': [[4,2],[1,4]]},
        {'id':3, 'runs': 10, 'factors_and_levels': [[1,2],[1,5]]},
        {'id':4, 'runs': 12, 'factors_and_levels': [[4,2],[1,3]]},
        {'id':5, 'runs': 12, 'factors_and_levels': [[2,2],[1,6]]},
        {'id':6, 'runs': 12, 'factors_and_levels': [[1,3],[1,4]]},
        {'id':7, 'runs': 14, 'factors_and_levels': [[1,2],[1,7]]},
        {'id':8, 'runs': 15, 'factors_and_levels': [[1,3],[1,5]]},
        {'id':9, 'runs': 16, 'factors_and_levels': [[6,2],[4,3]]},
        {'id':10, 'runs': 18, 'factors_and_levels': [[6,3],[1,6]]},
        {'id':11, 'runs': 20, 'factors_and_levels': [[8,2],[1,5]]},
        {'id':12, 'runs': 20, 'factors_and_levels': [[2,2],[1,10]]},
        {'id':13, 'runs': 24, 'factors_and_levels': [[13,2],[1,3],[1,4]]},
        {'id':14, 'runs': 28, 'factors_and_levels': [[12,2],[1,7]]},
        {'id':15, 'runs': 28, 'factors_and_levels': [[2,2],[1,14]]},
        #{'id':16, 'runs': 32, 'factors_and_levels': [[16,2],[1,16]]},
        #{'id':17, 'runs': 32, 'factors_and_levels': [[8,4],[1,8]]},
        {'id':18, 'runs': 36, 'factors_and_levels': [[27,2],[1,3]]},
        {'id':19, 'runs': 36, 'factors_and_levels': [[20,2],[2,3]]},
        {'id':20, 'runs': 36, 'factors_and_levels': [[18,2],[1,3],[1,6]]},
        {'id':21, 'runs': 36, 'factors_and_levels': [[13,2],[2,6]]},
        {'id':22, 'runs': 36, 'factors_and_levels': [[13,2],[1,9]]},
        {'id':23, 'runs': 36, 'factors_and_levels': [[11,2],[12,3]]},
        {'id':24, 'runs': 36, 'factors_and_levels': [[11,2],[2,3],[1,6]]},
        {'id':25, 'runs': 36, 'factors_and_levels': [[10,2],[8,3],[1,6]]},
        {'id':26, 'runs': 36, 'factors_and_levels': [[10,2],[1,3],[2,6]]},
        {'id':27, 'runs': 36, 'factors_and_levels': [[9,2],[4,3],[2,6]]},
        {'id':28, 'runs': 36, 'factors_and_levels': [[9,2],[1,3],[2,6]]},
        {'id':29, 'runs': 36, 'factors_and_levels': [[8,2],[3,6]]},
        {'id':30, 'runs': 36, 'factors_and_levels': [[7,2],[2,3],[2,6]]},
        {'id':31, 'runs': 36, 'factors_and_levels': [[5,2],[3,3],[2,6]]},
        {'id':32, 'runs': 36, 'factors_and_levels': [[4,2],[13,3]]},
        {'id':33, 'runs': 36, 'factors_and_levels': [[4,2],[5,3],[1,6]]},
        {'id':34, 'runs': 36, 'factors_and_levels': [[4,2],[3,3],[1,6]]},
        {'id':35, 'runs': 36, 'factors_and_levels': [[4,2],[1,3],[3,6]]},
        {'id':36, 'runs': 36, 'factors_and_levels': [[3,2],[9,3],[1,6]]},
        {'id':37, 'runs': 36, 'factors_and_levels': [[3,2],[6,3],[1,6]]},
        {'id':38, 'runs': 36, 'factors_and_levels': [[3,2],[2,3],[3,6]]},
        {'id':39, 'runs': 36, 'factors_and_levels': [[2,2],[12,3],[1,6]]},
        {'id':40, 'runs': 36, 'factors_and_levels': [[2,2],[5,3],[2,6]]},
        {'id':41, 'runs': 36, 'factors_and_levels': [[2,2],[2,3],[2,6]]},
        {'id':42, 'runs': 36, 'factors_and_levels': [[1,2],[8,3],[2,6]]},
        {'id':43, 'runs': 36, 'factors_and_levels': [[1,2],[3,3],[3,6]]},
        {'id':44, 'runs': 36, 'factors_and_levels': [[1,2],[1,3],[3,6]]},
        {'id':45, 'runs': 36, 'factors_and_levels': [[1,2],[3,6]]},
        {'id':46, 'runs': 36, 'factors_and_levels': [[12,3],[1,12]]},
        {'id':47, 'runs': 36, 'factors_and_levels': [[7,3],[3,6]]}
    ]}