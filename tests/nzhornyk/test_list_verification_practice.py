import pytest


def test_get_list_length_1():
    testable_list1 = [4, 67, 98, 'test', 34, 29, 76, 987, 34243, 8678, 64]
    if testable_list1:
        print('List is not empty')
    else:
        print('list is empty')


@pytest.mark.parametrize(["data", "expected_len"], [
    ([1, 2, 3, 4, 5, 6], 6),
    ([], 0)
])
def test_get_list_length_data_driven_2(data, expected_len):
    testable_list2 = data
    testable_list2_len = len(testable_list2)
    assert testable_list2_len == expected_len

@pytest.mark.xfail
@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 35), (4, 44)])
def test_multiplication_data_driven(num, output):
    assert 11 * num == output


def test_get_list_elements_count_3():
    testable_list3 = [4, 67, 98, 'test', 34, 29, 'Python test']
    print('The list is:' + str(testable_list3))
    counter = 0
    for item in testable_list3:
        counter = counter + 1
    print('The length is:' + str(counter))
    assert counter == 7


def test_get_list_element_4():
    testable_list4 = [4, 67, 98, 'test', 34, 29, 'Python test']
    for item in testable_list4:
        if item == 'Python test':
            print('Found the element')
            break
    else:
        print('Python test was not found((')


def test_list_to_string_5():
    input_list = ['Python', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
    new_string = ""
    for x in input_list:
        new_string += x
    print(new_string)
    assert new_string == 'Python programming'
    print(f'Result:' + new_string)


def test_list_mapimg_string_6():
    input_list = ['Python', ' ', 'programming']
    mapped_string = ''.join(map(str, input_list))
    assert mapped_string == 'Python programming'


def test_list_multiplication_7():
    list1 = [5]
    list2 = list1 * 5
    assert list2 == [5, 5, 5, 5, 5]


def test_list_adding_8():
    list1 = [5]
    list2 = list1 + [5]
    assert list2 == [5, 5]


def test_list_concatenation_9():
    list1 = [5, 6, 7, 8, 9]
    list2 = [1, 2, 3, 4]
    concatenated_list = [y for x in [list1, list2] for y in x]
    assert concatenated_list == [5, 6, 7, 8, 9, 1, 2, 3, 4]


def test_list_extending_10():
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8, 9]
    list1.extend(list2)
    assert list1 == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_list_append_11():
    list1 = [1, 2, 3, 4]
    list2 = ['T', 'E', 'S', 'T']
    for x in list2:
        list1.append(x)
    assert list1 == [1, 2, 3, 4, 'T', 'E', 'S', 'T']


def test_list_zip_to_list_12():
    uppercase = ['T', 'E', 'S', 'T']
    lowercase = ['t', 'e', 's', 't']
    new_list = list(zip(uppercase, lowercase))
    assert new_list == [('T', 't'), ('E', 'e'), ('S', 's'), ('T', 't')]


@pytest.fixture
def zipping():
    input_uppercase = ['T', 'E', 'S', 't']
    input_numbers = [1, 2, 3, 4]
    zipped = dict(zip(input_uppercase, input_numbers))
    return zipped


def test_list_zip_to_dict_13(zipping):
    print(zipping)
    assert zipping == {'T': 1, 'E': 2, 'S': 3, 't': 4}


@pytest.fixture
def input_value():
    input_val = 39
    return input_val


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

@pytest.mark.xfail
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0


# magic methods:
@pytest.mark.skip
def test_len(my_list, mocker):
    mocker.spy(list, "__len__")
    len(my_list)
    assert my_list.__len__.called


from collections import UserList


@pytest.mark.skip
def test_list_len(mocker):
    mocker.spy(UserList, "__len__")
    my_list = UserList()
    len(my_list)
    assert UserList.__len__.called

    @pytest.mark.xfail
    @pytest.mark.great
    def test_greater():
        num = 100
        assert num > 100

    @pytest.mark.xfail
    @pytest.mark.great
    def test_greater_equal():
        num = 100
        assert num >= 100

    @pytest.mark.skip
    @pytest.mark.others
    def test_less():
        num = 100
        assert num < 200
