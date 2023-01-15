
from app import bubble_sort
import pytest



bubble_sort_testdata = [
    ([1,6,7,9,4,15,-3], [-3,1,4,6,7,9,15]),
    ([2.5,0.023,69,199,-0.03,0,-110], [-110,-0.03,0,0.023,2.5,69,199]),
    ([1,25,'wtorek',92,101], None),
    (1905,None)
]

@pytest.mark.parametrize('input_list, sorted_list', bubble_sort_testdata)
def test_bubble_sort(input_list, sorted_list):
    assert bubble_sort(input_list) == sorted_list