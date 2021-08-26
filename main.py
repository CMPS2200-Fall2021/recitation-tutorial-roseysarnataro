def sum_of_squares(a):
	return sum([x**2 for x in a])
	pass

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
	assert sum_of_squares([2,3,4]) == 29
