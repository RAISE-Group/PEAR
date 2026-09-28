def test_preserve_category(self):
    data = DataFrame({'A': [1, 2], 'B': pd.Categorical(['X', 'Y'])})
    result = pd.melt(data, ['B'], ['A'])
    expected = DataFrame({'B': pd.Categorical(['X', 'Y']), 'variable': ['A', 'A'], 'value': [1, 2]})
    tm.assert_frame_equal(result, expected)