def test_replace_dict_no_regex(self):
    answer = Series({0: 'Strongly Agree', 1: 'Agree', 2: 'Neutral', 3: 'Disagree', 4: 'Strongly Disagree'})
    weights = {'Agree': 4, 'Disagree': 2, 'Neutral': 3, 'Strongly Agree': 5, 'Strongly Disagree': 1}
    expected = Series({0: 5, 1: 4, 2: 3, 3: 2, 4: 1})
    result = answer.replace(weights)
    tm.assert_series_equal(result, expected)