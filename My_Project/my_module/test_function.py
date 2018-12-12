from functions import element_count, check_elements
"""Test for my functions."""

def test_element_count():
	assert callable(check_elements)
	assert element_count([0,0],0)
	assert [1]== element_count([0,0],0)

def test_check_elements():
	assert callable(check_elements)
	assert check_elements([0,0],[0,0],0)
	assert [0]== check_elements([0,0],[0,0],0)





