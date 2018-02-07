from extract_database import extract_modomics_db
from extract_database import extract_albany_db
from dict_ops import merge_dicts
from dict_ops import dict_to_file

#extract http://modomics.genesilico.pl
dict1 = extract_modomics_db()

#extract http://mods.rna.albany.edu database
dict2 = extract_albany_db()

#merged dictionaries containing two databases
merged_dict = merge_dicts(dict1, dict2)

#save merged dictionaries to file
dict_to_file(merged_dict)
