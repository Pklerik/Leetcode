import main
import pytest

@pytest.fixture
def get_classes():
    import sys, inspect
    returns = []
    for _, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            returns.append(obj)
    return returns

def test_case_1(get_classes):
    nums = [1,2,3,4,5,6,7]
    k = 3
    for class_obj in get_classes:
        assert class_obj().rotate(nums, k) == [5,6,7,1,2,3,4]
    
def test_case_2(get_classes):
    nums = [1,2]
    k = 5
    for class_obj in get_classes:
        assert class_obj().rotate(nums, k) == [2,1]