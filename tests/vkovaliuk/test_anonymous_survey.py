import pytest

from tests.vkovaliuk.samples.anonymous_survey import AnonymousSurvey


answers = ['English', 'Ukrainian', "Polish"]


@pytest.fixture(scope="class")
def main_setup():
    """Setup and Tear down for whole project"""
    question = "What language you know? \n"
    my_survey = AnonymousSurvey(question)

    return my_survey


@pytest.fixture(scope="class")
def set_up_empty_survey(main_setup):
    yield main_setup
    print("Clean if set_up_empty_survey")


@pytest.fixture(scope="class")
def set_up_full_survey(main_setup):
    for answer in answers:
        main_setup.append_response(answer)
    yield main_setup
    print("clean if set_up_full_survey")


def test_add_single_response(set_up_empty_survey):
    set_up_empty_survey.append_response(answers[0])

    assert answers[:1], set_up_empty_survey.responses


def test_add_many_responses(set_up_empty_survey):
    set_up_empty_survey.append_response(answers)

    assert answers, set_up_empty_survey.responses
    assert 3, len(set_up_empty_survey.responses)


def test_remove_answer_from_survey(set_up_full_survey):
    set_up_full_survey.remove_response(answers[0])

    assert 2, len(set_up_full_survey.responses)
    assert answers[1:], set_up_full_survey.responses


@pytest.mark.parametrize("reverse",
                         [True,
                          False], ids=['test_sort_reverse_true', 'test_sort_reverse_false'])
def test_sort_responses(set_up_full_survey, reverse):
    responses = set_up_full_survey.get_sorted_responses(reverse)

    assert answers.sort(reverse=reverse), responses
