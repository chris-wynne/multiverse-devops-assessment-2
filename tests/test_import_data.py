import pytest
import csv
import numpy as np
from scripts.import_data import get_input, add_index
from pathlib import Path

filename = r"data/results.csv"
output = get_input(filename)
column_names = output[0]
expected_col_len = 6
expected_names = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]

#test values for temp csv
test_columns = ["A", "B", "C"]
test_rows = [
        ["a1", "b1", "c1"],
        ["a2", "b2", "c2"],
        ["a3", "b3", "c3"],
        ["", "", ""],
        ["a4", "b4", "c4"],
        ["a5", "b5", "c5"],
        ["a6", "b6", "c6"],
        ["a7", "b7", "c7"],
        ["", "", ""],
        ["a8", "b8", "c8"],
        ["a9", "b9", "c9"],
        ["a10", "b10", "c10"]
    ]

@pytest.fixture(scope='session')
def file_name(tmpdir_data):
    file = tmpdir_data.mktemp('data'.join('csvtest.csv'))
    with open(file, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(test_columns)
        for row in test_rows:
            csv_writer.writerow(row)
    return file

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