import main
import pytest

@pytest.fixture
def test_data():
    return [
        [1,0,2]
    ]
def test_main_case_1():
    assert main.Solution().candy([1,2,2]) == 4
    
def test_main_case_2():
    assert main.Solution().candy([1,0,2]) == 5
    
def test_main_case_3():
    assert main.Solution().candy([1,2,4,4,4,3]) == 10
    
def test_main_case_4():
    assert main.Solution().candy([1,3,4,5,2]) == 11
    