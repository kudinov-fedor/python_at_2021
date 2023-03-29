# To Do -> Tests can relate to list:
# string representation and formatting ++
# get length ++
# usage of + and * operators  ++
# usage in conditions ++
# usage for loops ++
# objects conversion from list and to list (str, bool, tuple, dict, set)
# usage of list methods (append, extend. etc.)
# interaction with built-in functions (zip, enumerate, map etc.)


def test_get_list_length_1():
    testable_list1 = [4, 67, 98, 'test', 34, 29, 76, 987, 34243, 8678, 64]
    if len(testable_list1) > 10:
        print('List is too large')
    else:
        print('Good result')


def test_get_list_length_2():
    testable_list2 = [4, 67, 98, 'test', 34, 29]
    testable_list2_len = len(testable_list2)
    assert testable_list2_len == 6


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


def test_list_to_string_6():
    input_list = ['Python', ' ', 'programming']
    mapped_string = ''.join(map(str, input_list))
    assert mapped_string == 'Python programming'


def test_list_multiplication_7():
    list1 = [5]
    list2 = list1 * 5
    assert list2 == [5, 5, 5, 5, 5]


def test_list_multiplication_8():
    list1 = [5]
    list2 = list1 + [5]
    assert list2 == [5, 5]
