def test_iloc_empty_list_indexer_is_ok(self):
    df = tm.makeCustomDataframe(5, 2)
    tm.assert_frame_equal(df.iloc[:, []], df.iloc[:, :0], check_index_type=True, check_column_type=True)
    tm.assert_frame_equal(df.iloc[[], :], df.iloc[:0, :], check_index_type=True, check_column_type=True)
    tm.assert_frame_equal(df.iloc[[]], df.iloc[:0, :], check_index_type=True, check_column_type=True)