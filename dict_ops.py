import numpy as np


def merge_dicts(dict1, dict2):

    #copy one element from each dictionary
    el1 = dict1.popitem()
    el2 = dict2[el1[0]]
    el1 = el1[1]

    #identify and delete repeted information
    keys1 = list(el1.keys())
    keys2 = list(el2.keys())
    for key1 in keys1:
        for key2 in keys2:
            if key1 in el1 and key2 in el2:
                if el1[key1] == el2[key2] and el1[key1] is not '':
                    print('Databases repeat information in ' + key1 + ' and ' + key2 + ' columns.')
                    for dict in dict2:
                        if not dict in dict1: dict1[dict] = {key1:dict}
                        else: dict1[dict][key1] = dict2[dict][key2]
                        del dict2[dict][key2]

    #create new dictionary
    unique_elements = list(set(list(dict1.keys()) + list(dict2.keys())))
    merged_dict = {}

    for element in unique_elements:
        element_dict = {}

        if element in dict1:
            element_dict.update(dict1[element])
        if element in dict2:
            element_dict.update(dict2[element])
        merged_dict[element] = element_dict

    return merged_dict

def dict_to_file(dict):

    #get different parameter names
    unique = np.unique([item for sublist in [list(set(list(dict[key].keys()))) for key in dict] for item in sublist])

    array = [dict_list_to_list(dict[key], unique) for key in dict]

    print_array_to_file(array, unique)

    return array, unique

def dict_list_to_list(dict, lst):
    return [dict[key] if key in dict else "-" for key in lst]


def print_array_to_file(array, unique):
    file = open('merged_databases.data', 'w')

    #remove new line from elements
    for row in array:
        for ind in range(len(row)):
            row[ind] = row[ind].replace('\n', '|')

    #join elements and labels
    array = [unique] + array

    #write array to file
    st = ''
    for row in array:
        for el in row:
            if len(el) > 0: st = st + el
            else : st = st + '-'
        file.write(st + '\n')
        st = ''

    file.close()






