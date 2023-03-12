import pytest
import csv
import os
import shutil
from scripts.import_data import save_output

#test array data for writing to a temporary csv.
test_data = [
        ["test_id", "test_name", "test_score"],
        ["1", "john", "5"],
        ["1", "john", "5"],
        ["2", "paul", "6"],
        ["", "", ""],
        ["2", "paul", "6"],
        ["", "", ""],
        ["3", "george", "0"],
        ["4", "ringo", "11"],
    ]

@pytest.fixture(scope="module")
def get_test_csv_data(tmp_path_factory):
    """
    Summary: 
        Create a temporary file in the test directory and writes the sample CSV data (test_data)
    Args:
        tmp_path_factory : A session-scoped fixture which can be used to create arbitrary temporary directories from any other fixture or test
    Returns:
        test_file: csv file containing values generated in test_data
    """
    test_file = tmp_path_factory.mktemp("data").joinpath("test.csv")
    with test_file.open("w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in test_data:
            csv_writer.writerow(row)
    yield test_file
    os.remove(test_file) #remove temp file after it has been tested

@pytest.fixture(scope="module")
def gen_save_output_file(tmp_path_factory):
    output_test_file = tmp_path_factory.mktemp("data").joinpath("output_test.csv")
    save_output(test_data, output_test_file)
    yield  output_test_file
    os.remove(output_test_file) #remove temp file after it has been tested