def test_frame_getitem_not_sorted2(self):
    df = DataFrame({'col1': ['b', 'd', 'b', 'a'], 'col2': [3, 1, 1, 2], 'data': ['one', 'two', 'three', 'four']})
    df2 = df.set_index(['col1', 'col2'])
    df2_original = df2.copy()
    df2.index.set_levels(['b', 'd', 'a'], level='col1', inplace=True)
    df2.index.set_codes([0, 1, 0, 2], level='col1', inplace=True)
    assert not df2.index.is_lexsorted()
    assert not df2.index.is_monotonic
    assert df2_original.index.equals(df2.index)
    expected = df2.sort_index()
    assert expected.index.is_lexsorted()
    assert expected.index.is_monotonic
    result = df2.sort_index(level=0)
    assert result.index.is_lexsorted()
    assert result.index.is_monotonic
    tm.assert_frame_equal(result, expected)