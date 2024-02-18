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
    prices = [7,1,5,3,6,4]
    for class_obj in get_classes:
        assert class_obj().maxProfit(prices) == 7
    
def test_case_2(get_classes):
    prices = [1,2]
    for class_obj in get_classes:
        assert class_obj().maxProfit(prices) == 1
        
def test_case_3(get_classes):
    prices = [7,6,4,3,1]
    for class_obj in get_classes:
        assert class_obj().maxProfit(prices) == 0
        