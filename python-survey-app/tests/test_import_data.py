import pytest
import csv
import numpy as np
import os
import shutil
from numpy import genfromtxt
from pathlib import Path
from scripts.import_data import get_input, save_output

filename = r"data/results.csv"
output = get_input(filename)
column_names = output[0]
expected_col_len = 6
expected_names = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]

def test_file_exists():
    file_exists = Path(filename).is_file()
    assert file_exists == True

def test_input_is_list():
    expected_output = np.ndarray
    assert type(output) == expected_output
    
def test_input_column_len():
    assert len(output[0]) == expected_col_len + 1 #additional column added for added index col

def test_input_column_names():
    col_range = range(expected_col_len)
    
    for col in col_range:
        assert column_names[col] == expected_names[col]

def test_array_contains_index_col(get_test_csv_data):
    data_without_blanks = get_input(get_test_csv_data)
    assert "index" in data_without_blanks[0]

def test_remove_blank_rows(get_test_csv_data):
    data_with_blanks = genfromtxt(get_test_csv_data, delimiter=',', dtype='<U13')
    data_without_blanks = get_input(get_test_csv_data)
    
    #checks all 13 rows exist in temporary test csv
    assert len(data_with_blanks) == 9
    #checks 2 blank rows have been removed from imported temporary data set
    assert len(data_without_blanks) == 7
    
def test_save_output(gen_save_output_file):
    output_file_exists = Path(gen_save_output_file).is_file()
    assert output_file_exists == True