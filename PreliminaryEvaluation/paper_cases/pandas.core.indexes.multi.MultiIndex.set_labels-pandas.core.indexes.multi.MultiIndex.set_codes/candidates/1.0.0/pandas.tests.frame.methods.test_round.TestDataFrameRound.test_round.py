def test_round(self):
    df = DataFrame()
    tm.assert_frame_equal(df, df.round())
    df = DataFrame({'col1': [1.123, 2.123, 3.123], 'col2': [1.234, 2.234, 3.234]})
    expected_rounded = DataFrame({'col1': [1.0, 2.0, 3.0], 'col2': [1.0, 2.0, 3.0]})
    tm.assert_frame_equal(df.round(), expected_rounded)
    decimals = 2
    expected_rounded = DataFrame({'col1': [1.12, 2.12, 3.12], 'col2': [1.23, 2.23, 3.23]})
    tm.assert_frame_equal(df.round(decimals), expected_rounded)
    tm.assert_frame_equal(np.round(df, decimals), expected_rounded)
    round_list = [1, 2]
    with pytest.raises(TypeError):
        df.round(round_list)
    expected_rounded = DataFrame({'col1': [1.1, 2.1, 3.1], 'col2': [1.23, 2.23, 3.23]})
    round_dict = {'col1': 1, 'col2': 2}
    tm.assert_frame_equal(df.round(round_dict), expected_rounded)
    expected_partially_rounded = DataFrame({'col1': [1.123, 2.123, 3.123], 'col2': [1.2, 2.2, 3.2]})
    partial_round_dict = {'col2': 1}
    tm.assert_frame_equal(df.round(partial_round_dict), expected_partially_rounded)
    wrong_round_dict = {'col3': 2, 'col2': 1}
    tm.assert_frame_equal(df.round(wrong_round_dict), expected_partially_rounded)
    non_int_round_dict = {'col1': 1, 'col2': 0.5}
    with pytest.raises(TypeError):
        df.round(non_int_round_dict)
    non_int_round_dict = {'col1': 1, 'col2': 'foo'}
    with pytest.raises(TypeError):
        df.round(non_int_round_dict)
    non_int_round_Series = Series(non_int_round_dict)
    with pytest.raises(TypeError):
        df.round(non_int_round_Series)
    non_int_round_dict = {'col1': 1, 'col2': [1, 2]}
    with pytest.raises(TypeError):
        df.round(non_int_round_dict)
    non_int_round_Series = Series(non_int_round_dict)
    with pytest.raises(TypeError):
        df.round(non_int_round_Series)
    non_int_round_Series = Series(non_int_round_dict)
    with pytest.raises(TypeError):
        df.round(non_int_round_Series)
    non_int_round_Series = Series(non_int_round_dict)
    with pytest.raises(TypeError):
        df.round(non_int_round_Series)
    negative_round_dict = {'col1': -1, 'col2': -2}
    big_df = df * 100
    expected_neg_rounded = DataFrame({'col1': [110.0, 210, 310], 'col2': [100.0, 200, 300]})
    tm.assert_frame_equal(big_df.round(negative_round_dict), expected_neg_rounded)
    nan_round_Series = Series({'col1': np.nan, 'col2': 1})
    expected_nan_round = DataFrame({'col1': [1.123, 2.123, 3.123], 'col2': [1.2, 2.2, 3.2]})
    with pytest.raises(TypeError):
        df.round(nan_round_Series)
    tm.assert_series_equal(df['col1'].round(1), expected_rounded['col1'])
    decimals = 2
    expected_rounded = DataFrame({'col1': [1.12, 2.12, 3.12], 'col2': [1.23, 2.23, 3.23]})
    df.columns.name = 'cols'
    expected_rounded.columns.name = 'cols'
    tm.assert_frame_equal(df.round(decimals), expected_rounded)
    tm.assert_series_equal(df['col1'].round(decimals), expected_rounded['col1'])
    tm.assert_series_equal(df.round(decimals)['col1'], expected_rounded['col1'])