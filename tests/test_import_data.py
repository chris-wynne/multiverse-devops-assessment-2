import pytest
import csv
import numpy as np
from numpy import genfromtxt
from scripts.import_data import get_input, add_index
from pathlib import Path

filename = r"data/results.csv"
output = get_input(filename)
column_names = output[0]
expected_col_len = 6
expected_names = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]

#test array data for writing to a temporary csv
test_data = [
        ["A", "B", "C"],
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

@pytest.fixture(scope="module")
def get_csv_data(tmp_path_factory):
    # Create a temporary file in the test directory and writes the sample CSV data (test_data)
    test_file = tmp_path_factory.mktemp("data").joinpath("test.csv")
    with test_file.open("w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in test_data:
            csv_writer.writerow(row)
    return test_file

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

def test_remove_blank_rows(get_csv_data):
    data_with_blanks = genfromtxt(get_csv_data, delimiter=',')
    data_without_blanks = get_input(get_csv_data)
    
    #checks all 13 rows exist in temporary test csv
    assert len(data_with_blanks) == 13
    #checks 2 blank rows have been removed from imported temporary data set
    assert len(data_without_blanks) == 11