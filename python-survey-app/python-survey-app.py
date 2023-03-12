import numpy as np
from scripts.import_data import get_input, save_output
from scripts.clean_data import identify_duplicate_values, remove_rows, capitalise_column_values, identify_invalid_score, drop_index
from scripts.read_output import read_output, print_output

fpath = r"data/results.csv"
opath = r"data/output.csv"

dataset = get_input(fpath) #import dataset

#clean data
duplicate_index_list = identify_duplicate_values(dataset, "user_id")
clean_array = remove_rows(dataset, duplicate_index_list)

invalid_a3_index_list = identify_invalid_score(clean_array, "answer_3")
clean_array = remove_rows(clean_array, duplicate_index_list)

clean_array = remove_rows(clean_array, invalid_a3_index_list)

clean_array = capitalise_column_values(clean_array, "first_name")
clean_array = capitalise_column_values(clean_array, "last_name")

#drop index before saving
clean_array = drop_index(clean_array)

#save output
save_output(clean_array, opath)

#read output
output_array = read_output(opath)

#print array
print_output(output_array)