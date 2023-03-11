import pytest
import numpy as np
from scripts.clean_data import identify_duplicate_values, remove_duplicates, find_column_position, capitalise_column_values

test_array = np.array([["index", "test_id", "test_name"], [1, 1, "john"], [2, 1, "john"], [3, 2, "paul"], [4, 2, "paul"], [5, 3, "george"], [6, 4, "ringo"]])

def test_identify_duplicate_values():
    duplicate_indexes = identify_duplicate_values(test_array, "test_id")
    assert len(duplicate_indexes) == 2

def test_remove_duplicates():
    duplicate_indexes = identify_duplicate_values(test_array, "test_id")
    clean_test_array = remove_duplicates(test_array, duplicate_indexes)
    
    #expected length of test_array
    assert len(test_array) == 7
    
    #expected length of clean test_array
    assert len(clean_test_array) == 5

def test_find_column_position():
    col_position = find_column_position(test_array, "index")
    assert col_position == 0

def test_capitalise_column_values():
    capitalised_test_array = capitalise_column_values(test_array, "test_name")
    assert capitalised_test_array[1,2] == "John"
    assert capitalised_test_array[3,2] == "Paul"
    assert capitalised_test_array[5,2] == "George"
    assert capitalised_test_array[6,2] == "Ringo"