def test_take_fill_value(self):
    cat = pd.Categorical(['a', 'b', 'c'])
    result = cat.take([0, 1, -1], fill_value='a', allow_fill=True)
    expected = pd.Categorical(['a', 'b', 'a'], categories=['a', 'b', 'c'])
    tm.assert_categorical_equal(result, expected)