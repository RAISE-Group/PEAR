def test_indicator(self):
    df1 = DataFrame({'col1': [0, 1], 'col_conflict': [1, 2], 'col_left': ['a', 'b']})
    df1_copy = df1.copy()
    df2 = DataFrame({'col1': [1, 2, 3, 4, 5], 'col_conflict': [1, 2, 3, 4, 5], 'col_right': [2, 2, 2, 2, 2]})
    df2_copy = df2.copy()
    df_result = DataFrame({'col1': [0, 1, 2, 3, 4, 5], 'col_conflict_x': [1, 2, np.nan, np.nan, np.nan, np.nan], 'col_left': ['a', 'b', np.nan, np.nan, np.nan, np.nan], 'col_conflict_y': [np.nan, 1, 2, 3, 4, 5], 'col_right': [np.nan, 2, 2, 2, 2, 2]})
    df_result['_merge'] = Categorical(['left_only', 'both', 'right_only', 'right_only', 'right_only', 'right_only'], categories=['left_only', 'right_only', 'both'])
    df_result = df_result[['col1', 'col_conflict_x', 'col_left', 'col_conflict_y', 'col_right', '_merge']]
    test = merge(df1, df2, on='col1', how='outer', indicator=True)
    tm.assert_frame_equal(test, df_result)
    test = df1.merge(df2, on='col1', how='outer', indicator=True)
    tm.assert_frame_equal(test, df_result)
    tm.assert_frame_equal(df1, df1_copy)
    tm.assert_frame_equal(df2, df2_copy)
    df_result_custom_name = df_result
    df_result_custom_name = df_result_custom_name.rename(columns={'_merge': 'custom_name'})
    test_custom_name = merge(df1, df2, on='col1', how='outer', indicator='custom_name')
    tm.assert_frame_equal(test_custom_name, df_result_custom_name)
    test_custom_name = df1.merge(df2, on='col1', how='outer', indicator='custom_name')
    tm.assert_frame_equal(test_custom_name, df_result_custom_name)
    msg = 'indicator option can only accept boolean or string arguments'
    with pytest.raises(ValueError, match=msg):
        merge(df1, df2, on='col1', how='outer', indicator=5)
    with pytest.raises(ValueError, match=msg):
        df1.merge(df2, on='col1', how='outer', indicator=5)
    test2 = merge(df1, df2, on='col1', how='left', indicator=True)
    assert (test2._merge != 'right_only').all()
    test2 = df1.merge(df2, on='col1', how='left', indicator=True)
    assert (test2._merge != 'right_only').all()
    test3 = merge(df1, df2, on='col1', how='right', indicator=True)
    assert (test3._merge != 'left_only').all()
    test3 = df1.merge(df2, on='col1', how='right', indicator=True)
    assert (test3._merge != 'left_only').all()
    test4 = merge(df1, df2, on='col1', how='inner', indicator=True)
    assert (test4._merge == 'both').all()
    test4 = df1.merge(df2, on='col1', how='inner', indicator=True)
    assert (test4._merge == 'both').all()
    for i in ['_right_indicator', '_left_indicator', '_merge']:
        df_badcolumn = DataFrame({'col1': [1, 2], i: [2, 2]})
        msg = 'Cannot use `indicator=True` option when data contains a column named {}|Cannot use name of an existing column for indicator column'.format(i)
        with pytest.raises(ValueError, match=msg):
            merge(df1, df_badcolumn, on='col1', how='outer', indicator=True)
        with pytest.raises(ValueError, match=msg):
            df1.merge(df_badcolumn, on='col1', how='outer', indicator=True)
    df_badcolumn = DataFrame({'col1': [1, 2], 'custom_column_name': [2, 2]})
    msg = 'Cannot use name of an existing column for indicator column'
    with pytest.raises(ValueError, match=msg):
        merge(df1, df_badcolumn, on='col1', how='outer', indicator='custom_column_name')
    with pytest.raises(ValueError, match=msg):
        df1.merge(df_badcolumn, on='col1', how='outer', indicator='custom_column_name')
    df3 = DataFrame({'col1': [0, 1], 'col2': ['a', 'b']})
    df4 = DataFrame({'col1': [1, 1, 3], 'col2': ['b', 'x', 'y']})
    hand_coded_result = DataFrame({'col1': [0, 1, 1, 3], 'col2': ['a', 'b', 'x', 'y']})
    hand_coded_result['_merge'] = Categorical(['left_only', 'both', 'right_only', 'right_only'], categories=['left_only', 'right_only', 'both'])
    test5 = merge(df3, df4, on=['col1', 'col2'], how='outer', indicator=True)
    tm.assert_frame_equal(test5, hand_coded_result)
    test5 = df3.merge(df4, on=['col1', 'col2'], how='outer', indicator=True)
    tm.assert_frame_equal(test5, hand_coded_result)