import numpy as np
from scripts.import_data import get_input
from scripts.clean_data import identify_duplicate_values, remove_duplicates

fpath = r"data/results.csv"

dataset = get_input(fpath) #import dataset

duplicate_index_list = identify_duplicate_values(dataset, "user_id")
clean_array = remove_duplicates(dataset, duplicate_index_list)

print(clean_array)