import pytest
import row_to_list

def test_for_clean_row():
    data = 'good data'
    result = 'pass'
    assert row_to_list(data) == result
 
def test_for_missing_area():
    data = 'broken'
    assert row_to_list(data) is None
    
def test_for_missing_tab():
    data = 'no tab'
    assert row_to_list(data) is None
