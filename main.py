from extract_database import extract_modomics_db
from extract_database import extract_albany_db
from dict_ops import merge_dicts
from dict_ops import dict_to_file

dict1 = extract_modomics_db()
print('OK')
dict2 = extract_albany_db()
print('OK')
merged_dict = merge_dicts(dict1, dict2)
print('OK')
dict_to_file(merged_dict)
print('OK')
