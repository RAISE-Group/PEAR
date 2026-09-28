def test_partial_set_invalid(self):
    orig = tm.makeTimeDataFrame()
    df = orig.copy()
    with pytest.raises(TypeError):
        df.loc[100.0, :] = df.iloc[0]
    with pytest.raises(TypeError):
        df.loc[100, :] = df.iloc[0]
    df = orig.copy()
    df.loc['a', :] = df.iloc[0]
    exp = orig.append(Series(df.iloc[0], name='a'))
    tm.assert_frame_equal(df, exp)
    tm.assert_index_equal(df.index, Index(orig.index.tolist() + ['a']))
    assert df.index.dtype == 'object'