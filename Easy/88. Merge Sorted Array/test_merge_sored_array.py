import main
import pytest

@pytest.fixture
def test_data():
    list_tupls = [
    ([1,2,3,0,0,0], 3, [2,5,6], 3)
    ]
    for item in list_tupls:
        yield item

def test_case_1():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    main.Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]
    
def test_case_2():
    nums1 = [1,0]
    m = 1
    nums2 = [2]
    n = 1
    main.Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1,2]
    
def test_case_3():
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    main.Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1,2]
    
def test_case_4():
    nums1 = [-1,0,0,3,3,3,0,0,0]
    m = 6
    nums2 = [1,2,2]
    n = 3
    main.Solution().merge(nums1, m, nums2, n)
    assert nums1 == [-1,0,0,1,2,2,3,3,3]
    
def test_case_5():  
    nums1 = [-1,0,0,0,3,0,0,0,0,0,0]
    m = 5
    nums2 = [-1,-1,0,0,1,2]
    n = 6
    main.Solution().merge(nums1, m, nums2, n)
    assert nums1 == [-1,-1,-1,0,0,0,0,0,1,2,3]