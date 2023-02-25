import pytest
import numpy as np
from scripts.import_data import get_input, add_index
from pathlib import Path

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

def test_array_contains_index_col():
    assert "index" in column_names
    pass