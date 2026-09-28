def test_pivot_periods_with_margins(self):
    df = DataFrame({'a': [1, 1, 2, 2], 'b': [pd.Period('2019Q1'), pd.Period('2019Q2'), pd.Period('2019Q1'), pd.Period('2019Q2')], 'x': 1.0})
    expected = DataFrame(data=1.0, index=pd.Index([1, 2, 'All'], name='a'), columns=pd.Index([pd.Period('2019Q1'), pd.Period('2019Q2'), 'All'], name='b'))
    result = df.pivot_table(index='a', columns='b', values='x', margins=True)
    tm.assert_frame_equal(expected, result)