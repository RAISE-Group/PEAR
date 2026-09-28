def test_concat_odered_dict(self):
    expected = pd.concat([pd.Series(range(3)), pd.Series(range(4))], keys=['First', 'Another'])
    result = pd.concat(OrderedDict([('First', pd.Series(range(3))), ('Another', pd.Series(range(4)))]))
    tm.assert_series_equal(result, expected)