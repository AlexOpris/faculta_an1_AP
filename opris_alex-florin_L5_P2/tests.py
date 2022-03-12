import functions

def test_add_value():
    """
    Test function add_value
    """

    arr_expected = [4]
    arr_value = []
    functions.add_value(arr_value, 4)
    assert arr_expected ==  arr_value

    arr_expected = [4, 10]
    arr_value = [4]
    functions.add_value(arr_value, 10)
    assert arr_expected == arr_value

    arr_expected = [5, 100]
    arr_value = [5]
    functions.add_value(arr_value, 100)
    assert arr_expected == arr_value

    arr_expected = [50,11,23]
    arr_value = [50,11]
    functions.add_value(arr_value, 23)
    assert arr_expected == arr_value

    arr_expected = [24,43,12,52,76]
    arr_value = [24,43,12,52]
    functions.add_value(arr_value, 76)
    assert arr_expected == arr_value


def test_insert_value():
    """
    Tests function insert_value
    """

    arr_expected = [1,2,3]
    arr_value = [1,3]
    functions.insert_value(arr_value, 2, 1)
    assert arr_expected == arr_value

    arr_expected = [10,11,12]
    arr_value = [11,12]
    functions.insert_value(arr_value, 10, 0)
    assert arr_expected == arr_value

    arr_expected = [12,42,25,16,78]
    arr_value = [12,42,25,78]
    functions.insert_value(arr_value, 16, 3)
    assert arr_expected == arr_value

    arr_expected = [90,63,45,77,10,48,92]
    arr_value = [90,63,45,77,10,92]
    functions.insert_value(arr_value, 48, 5)
    assert arr_expected == arr_value

    arr_expected = [32,47,95,63,55,11,27]
    arr_value = [32,47,95,63,55,11]
    functions.insert_value(arr_value, 27, 6)
    assert arr_expected == arr_value

def test_remove_value():
    """
    Tests the function remove_value
    """

    arr_expected = [10,36,42]
    arr_value = [10,2,36,42]
    functions.remove_value(arr_value,1)
    assert arr_expected == arr_value

    arr_expected = [36,42,50,90]
    arr_value = [10,36,42,50,90]
    functions.remove_value(arr_value,0)
    assert arr_expected == arr_value

    arr_expected = [70,59,23,51]
    arr_value = [70,59,23,51,28]
    functions.remove_value(arr_value,4)
    assert arr_expected == arr_value

    arr_expected = [11,25,62,44,23,95]
    arr_value = [11,25,62,44,23,95,77]
    functions.remove_value(arr_value,6)
    assert arr_expected == arr_value

    arr_expected = []
    arr_value = [10]
    functions.remove_value(arr_value,0)
    assert arr_expected == arr_value

def test_remove_from_a_to_b():
    """
    Tests the function remove_from_a_to_b
    """

    arr_expected = [11, 95]
    arr_value = [11, 25, 62, 44, 23, 95]
    functions.remove_from_a_to_b(arr_value, 1, 4)
    assert arr_expected == arr_value

    arr_expected = [62, 44, 23, 95, 77]
    arr_value = [11, 25, 62, 44, 23, 95, 77]
    functions.remove_from_a_to_b(arr_value,0, 1)
    assert arr_expected == arr_value

    arr_expected = [23, 95]
    arr_value = [11, 25, 62, 44, 23, 95]
    functions.remove_from_a_to_b(arr_value, 0, 3)
    assert arr_expected == arr_value

    arr_expected = [55,15]
    arr_value = [55,73,84,24,15]
    functions.remove_from_a_to_b(arr_value, 1, 3)
    assert arr_expected == arr_value

    arr_expected = []
    arr_value = [55,73,84,24,15]
    functions.remove_from_a_to_b(arr_value, 0, 4)
    assert arr_expected == arr_value

def test_replace_value():
    """
    Tests function replace_value
    """

    arr_expected = [23,42,61,22,62]
    arr_value = [23,42,61,55,62]
    functions.replace_value(arr_value, 22, 3)
    assert arr_expected == arr_value

    arr_expected = [100,53,23,72,33]
    arr_value = [7,53,23,72,33]
    functions.replace_value(arr_value, 100, 0)
    assert arr_expected == arr_value

    arr_expected = [42,26,27,73,99,5]
    arr_value = [42,26,27,73,51,5]
    functions.replace_value(arr_value, 99, 4)
    assert arr_expected == arr_value

    arr_expected = [52,35,84,66,12,100,23]
    arr_value = [52,35,84,66,12,66,23]
    functions.replace_value(arr_value, 100, 5)
    assert arr_expected == arr_value

    arr_expected = [52,20,84,66,12,66,23]
    arr_value = [52,35,84,66,12,66,23]
    functions.replace_value(arr_value, 20, 1)
    assert arr_expected == arr_value

def test_filter_mul_n():
    """
    Tests function filter_mul_10
    """

    arr_expected = [60,30]
    arr_value = [92,52,60,55,30,42]
    functions.filter_mul_n(arr_value,10)
    assert arr_expected == arr_value

    arr_expected = []
    arr_value = [92, 52, 55, 42]
    functions.filter_mul_n(arr_value,10)
    assert arr_expected == arr_value

    arr_expected = [10]
    arr_value = [92, 52, 10, 42]
    functions.filter_mul_n(arr_value,10)
    assert arr_expected == arr_value

    arr_expected = [60,50,90,30]
    arr_value = [60, 50, 90, 30,]
    functions.filter_mul_n(arr_value,10)
    assert arr_expected == arr_value

    arr_expected = [80,40]
    arr_value = [80,42,62,35,40]
    functions.filter_mul_n(arr_value,10)
    assert arr_expected == arr_value

def test_filter_higher_n():
    """
    Tests function filter_higher_70
    """

    arr_expected = [83]
    arr_value = [83, 46, 33, 15]
    functions.filter_higher_n(arr_value,70)
    assert arr_expected == arr_value

    arr_expected = []
    arr_value = [46, 33, 15]
    functions.filter_higher_n(arr_value,70)
    assert arr_expected == arr_value

    arr_expected = [83,92,99]
    arr_value = [83, 46, 33, 92, 99, 15]
    functions.filter_higher_n(arr_value,70)
    assert arr_expected == arr_value

    arr_expected = [92,93,99,85]
    arr_value = [92,93,99,85]
    functions.filter_higher_n(arr_value,70)
    assert arr_expected == arr_value

    arr_expected = [92,78]
    arr_value = [3,58,52,36,92,78]
    functions.filter_higher_n(arr_value,70)
    assert arr_expected == arr_value

def test_all():
    test_add_value()
    test_insert_value()
    test_remove_value()
    test_remove_from_a_to_b()
    test_replace_value()
    test_filter_mul_n()
    test_filter_higher_n()