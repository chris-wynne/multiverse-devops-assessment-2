import pytest
import numpy as np
from scripts.clean_data import identify_duplicate_values, remove_rows, find_column_position, capitalise_column_values, identify_invalid_score

test_array = np.array([["index", "test_id", "test_name", "test_score"], [1, 1, "john", 5], [2, 1, "john", 5], [3, 2, "paul", 6], [4, 2, "paul", 0], [5, 3, "george", 7], [6, 4, "ringo", 11]])

def test_identify_duplicate_values():
    duplicate_indexes = identify_duplicate_values(test_array, "test_id")
    assert len(duplicate_indexes) == 2
    assert duplicate_indexes == ['2', '4']

def test_remove_rows():
    duplicate_indexes = identify_duplicate_values(test_array, "test_id")
    invalid_score_indexes = identify_invalid_score(test_array, "test_score")
    
    clean_test_array_1 = remove_rows(test_array, duplicate_indexes)
    clean_test_array_2 = remove_rows(test_array, invalid_score_indexes)
    
    #expected length of test_array
    assert len(test_array) == 7
    
    #expected length of clean test_array
    assert len(clean_test_array_1) == 5
    assert len(clean_test_array_2) == 5

def test_find_column_position():
    col_position = find_column_position(test_array, "index")
    assert col_position == 0

def test_capitalise_column_values():
    capitalised_test_array = capitalise_column_values(test_array, "test_name")
    assert capitalised_test_array[1,2] == "John"
    assert capitalised_test_array[3,2] == "Paul"
    assert capitalised_test_array[5,2] == "George"
    assert capitalised_test_array[6,2] == "Ringo"

def test_identify_invalid_score():
    index_to_remove = identify_invalid_score(test_array, "test_score")
    assert index_to_remove == ['4','6']