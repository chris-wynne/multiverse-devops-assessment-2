import pytest
import numpy as np
from scripts.read_output import read_output, print_output
from tests.conftest import test_data

expected_data = [
        ['test_id', 'test_name', 'test_score'],
        ['1', 'john', '5'],
        ['1', 'john', '5'],
        ['2', 'paul', '6'],
        ['2', 'paul', '6'],
        ['3', 'george', '0'],
        ['4', 'ringo', '11']
    ]

print_array = ['test']
print_result = '                   t                     e                     s                     t \n' #formatted string result

def test_read_output(get_test_csv_data):
    data_array = read_output(get_test_csv_data)
  
    assert len(data_array) == len(expected_data)
    assert "index" not in data_array[0]
    
    row_range = range(0, len(data_array))
    for row in row_range:
        assert all([a == b for a, b in zip(data_array[row], expected_data[row])])
        
def test_read_output(capfd, get_test_csv_data):
    print_output(print_array)
    out, err = capfd.readouterr()
    
    assert out == print_result