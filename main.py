from extract_database import extract_modomics_db
from extract_database import extract_albany_db
from dict_ops import merge_dicts

dict2 = extract_albany_db()
dict1 = extract_modomics_db()
merge_dicts(dict1, dict2)

