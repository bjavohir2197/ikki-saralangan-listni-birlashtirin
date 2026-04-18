import pytest

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

def test_merge_sorted_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    expected_result = [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists(list1, list2) == expected_result

def test_merge_sorted_lists_with_duplicates():
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    expected_result = [1, 2, 2, 3, 3, 4]
    assert merge_sorted_lists(list1, list2) == expected_result

def test_merge_sorted_lists_with_empty_lists():
    list1 = [1, 2, 3]
    list2 = []
    expected_result = [1, 2, 3]
    assert merge_sorted_lists(list1, list2) == expected_result

def test_merge_sorted_lists_with_negative_numbers():
    list1 = [-3, -1, 1]
    list2 = [-2, 0, 2]
    expected_result = [-3, -2, -1, 0, 1, 2]
    assert merge_sorted_lists(list1, list2) == expected_result
