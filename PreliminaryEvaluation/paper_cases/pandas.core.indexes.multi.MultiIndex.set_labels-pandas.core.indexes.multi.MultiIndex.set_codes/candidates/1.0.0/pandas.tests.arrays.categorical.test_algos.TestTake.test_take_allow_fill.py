def test_take_allow_fill(self):
    cat = pd.Categorical(['a', 'a', 'b'])
    result = cat.take([0, -1, -1], allow_fill=True)
    expected = pd.Categorical(['a', np.nan, np.nan], categories=['a', 'b'])
    tm.assert_categorical_equal(result, expected)