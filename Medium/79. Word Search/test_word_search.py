
import pytest
from dataclasses import dataclass
from typing import List
from main import Solution
import timeit

@dataclass
class TestCases():
    board: List[List[str]]
    word: str
    excepted: bool
    

@pytest.fixture(scope="module")
def get_test_case():
    test_cases = [
        TestCases([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
        TestCases([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
        TestCases([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False)
    ]
    return test_cases
        

def test_main(get_test_case):
    for case in get_test_case:
        assert Solution().exist(case.board, case.word) == case.excepted
        
def test_time_main(get_test_case):
    for case in get_test_case:
        assert timeit.timeit('Solution().exist(case.board, case.word)', number=10000, globals={'Solution':Solution, 'case':case}) * 1000 < 70