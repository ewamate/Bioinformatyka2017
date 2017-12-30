

def merge_dicts(dict1, dict2):

    unique_elements = list(set(list(dict1.keys()) + list(dict2.keys())))
    print('elo')

    merged_dict = {}
    for element in unique_elements:
        element_dict = {}

        if element in dict1:
            element_dict.update(dict1[element])
        if element in dict2:
            element_dict.update(dict2[element])
        merged_dict[element] = element_dict

    return merged_dict