import pytest

'''test 1'''


@pytest.mark.parametrize('points, counted_nine', [
    ([1, 4, 2, 9, 7, 8, 9, 3, 1], 2),
    ([6, 7, 8, 1], 0)

])
def test_counting_9(points, counted_nine):
    res = points.count(9)
    assert res == counted_nine


'''test2'''
food = {
    'fruit': 'mango',
    'meat': 'beef',
    'vegetable': 'potato'
}


def test_meat():
    x = food.get('meat')
    assert x == 'beef'
    assert x != 'mango'
    assert x != 'meat'
    assert x != ''


'''test 3'''
dogs = ['weimaraner', 'chihuahua', 'maltese', 'spitz', 'shih-tzu', 'maltese']


def test_breeds():
    maltese = dogs.count('maltese')
    assert maltese == 2
    assert maltese != -2
    assert maltese != 3
    assert maltese > 0
    assert maltese < 3


def test_breed_find():
    maltese = dogs.index('maltese')
    assert maltese == 2
    assert maltese != 3
    assert maltese != 5
    assert maltese != 0


'''test 4'''
poem = 'I love apples, apple are my favorite fruit. apples grow on marvelous green apple trees.'


def test_word_counter():
    counter = poem.count('apples')
    assert counter > 1
    assert counter == 2
    assert counter != -2
    assert counter < 3
