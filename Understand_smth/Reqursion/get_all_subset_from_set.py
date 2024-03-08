from typing import List, Generator

def get_all_subset_from_set(some_set:set, subset_len:int) -> Generator[set, None, None]:
    """Yields all subsets in given set 

    Args:
        some_set (set): set of items 
        subset_len (int): length of given subset

    Yields:
        Generator[set, None, None]: Object with sets all subsets for given set  
    """
    if subset_len == 0:
        return
    if len(some_set) == subset_len:
        yield set()
    times = len(some_set) - subset_len + 1
    for index in range(times):
        yield set(list(some_set)[index:subset_len + index])
    yield from get_all_subset_from_set(some_set, subset_len - 1)


some_set = {1,2,3,4}
print(list(get_all_subset_from_set(some_set = some_set, subset_len=len(some_set))))