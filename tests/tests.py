from src.sortslab.math_functions import factorial_dynamic
from src.sortslab.math_functions import factorial_recursive
from src.sortslab.math_functions import fibo_dynamic
from src.sortslab.math_functions import fibo_recursive
from src.sortslab.sorts import bubble_sort as bubble_sort_func
from src.sortslab.sorts import quick_sort as quick_sort_func
from src.sortslab.sorts import counting_sort as counting_sort_func
from src.sortslab.sorts import bucket_sort as bucket_sort_func
from src.sortslab.sorts import radix_sort as radix_sort_func
from src.sortslab.sorts import heap_sort as heap_sort_func
from src.sortslab.sorts import selection_sort as selection_sort_func
from src.sortslab.sorts import insertion_sort as insertion_sort_func

TEST_ARRAY_1 = [64, 34, 25, 12, 22, 11, 90, 5, 88, 1, 77, 99, 0, 42]
TEST_ARRAY_2 = [9, 7, 0, 15, 2, 22, 1, 33, 18, 4, 10, 6, 8, 3]
TEST_ARRAY_3 = [1.7, 0.3, 2.1, 0.9, 1.2, 0.1, 3.4, 2.8, 0.5, 1.9]

EXPECTED_1 = [0, 1, 5, 11, 12, 22, 25, 34, 42, 64, 77, 88, 90, 99]
EXPECTED_2 = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 15, 18, 22, 33]
EXPECTED_3 = [0.1, 0.3, 0.5, 0.9, 1.2, 1.7, 1.9, 2.1, 2.8, 3.4]

def test_factorial_dynamic():
    assert factorial_dynamic(0) == 1
    assert factorial_dynamic(5) == 120
    assert factorial_dynamic(10) == 3628800

def test_factorial_recursive():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(10) == 3628800

def test_fibo_dynamic():
    assert fibo_dynamic(0) == 0
    assert fibo_dynamic(10) == 55
    assert fibo_dynamic(20) == 6765

def test_fibo_recursive():
    assert fibo_recursive(0) == 0
    assert fibo_recursive(10) == 55
    assert fibo_recursive(20) == 6765

def test_bubble_sort():
    assert bubble_sort_func(TEST_ARRAY_1) == EXPECTED_1
    assert bubble_sort_func(TEST_ARRAY_2) == EXPECTED_2
    assert bubble_sort_func(TEST_ARRAY_3) == EXPECTED_3

def test_quick_sort():
    assert quick_sort_func(TEST_ARRAY_1) == EXPECTED_1
    assert quick_sort_func(TEST_ARRAY_2) == EXPECTED_2
    assert quick_sort_func(TEST_ARRAY_3) == EXPECTED_3

def test_counting_sort():
    assert counting_sort_func(TEST_ARRAY_1) == EXPECTED_1
    assert counting_sort_func(TEST_ARRAY_2) == EXPECTED_2
    assert counting_sort_func([1, 4, 1, 2, 0, 3]) == [0, 1, 1, 2, 3, 4]

def test_bucket_sort():
    assert bucket_sort_func(TEST_ARRAY_3) == EXPECTED_3
    assert bucket_sort_func([0.5, 0.2, 0.8, 0.1]) == [0.1, 0.2, 0.5, 0.8]
    assert bucket_sort_func([1.0]) == [1.0]

def test_radix_sort():
    assert radix_sort_func(TEST_ARRAY_1) == EXPECTED_1
    assert radix_sort_func([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]
    assert radix_sort_func([100, 20, 5]) == [5, 20, 100]

def test_heap_sort():
    assert heap_sort_func(TEST_ARRAY_1) == EXPECTED_1
    assert heap_sort_func(TEST_ARRAY_2) == EXPECTED_2
    assert heap_sort_func([]) == []

def test_selection_sort():
    assert selection_sort_func(TEST_ARRAY_1) == EXPECTED_1
    assert selection_sort_func(TEST_ARRAY_2) == EXPECTED_2
    assert selection_sort_func([1]) == [1]

def test_insertion_sort():
    assert insertion_sort_func(TEST_ARRAY_1) == EXPECTED_1
    assert insertion_sort_func(TEST_ARRAY_2) == EXPECTED_2
    assert insertion_sort_func(TEST_ARRAY_3) == EXPECTED_3

if __name__ == "__main__":
    test_factorial_dynamic()
    test_factorial_recursive()
    test_fibo_dynamic()
    test_fibo_recursive()
    test_bubble_sort()
    test_quick_sort()
    test_counting_sort()
    test_bucket_sort()
    test_radix_sort()
    test_heap_sort()
    test_selection_sort()
    test_insertion_sort()