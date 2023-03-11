import pytest
import numpy as np
from scripts.clean_data import identify_duplicate_values, remove_duplicates, find_column_position

test_array = np.array([["index", "test_id"], [1, 1], [2, 1], [3, 2], [4, 2], [5, 3], [6, 4]])
test_dup_indexes = [2,4]

def test_identify_duplicate_values():
    duplicate_indexes = identify_duplicate_values(test_array, 1, 0)
    assert len(duplicate_indexes) == 2

def test_remove_duplicates():
    duplicate_indexes = identify_duplicate_values(test_array, 1, 0)
    clean_test_array = remove_duplicates(test_array, 0, duplicate_indexes)
    assert len(clean_test_array) == 5

def test_find_column_position():
    col_position = find_column_position(test_array, "index")
    assert col_position == 0    