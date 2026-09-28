def test_nested_flattening_consistent(self):
    df1 = json_normalize([{'A': {'B': 1}}])
    df2 = json_normalize({'dummy': [{'A': {'B': 1}}]}, 'dummy')
    tm.assert_frame_equal(df1, df2)