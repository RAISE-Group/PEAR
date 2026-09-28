def test_frame_repr(self):
    df = pd.DataFrame({'A': [1, 2, 3]}, index=pd.CategoricalIndex(['a', 'b', 'c']))
    result = repr(df)
    expected = '   A\na  1\nb  2\nc  3'
    assert result == expected