def test_to_csv_single_level_multi_index(self):
    index = pd.Index([(1,), (2,), (3,)])
    df = pd.DataFrame([[1, 2, 3]], columns=index)
    df = df.reindex(columns=[(1,), (3,)])
    expected = ',1,3\n0,1,3\n'
    result = df.to_csv(line_terminator='\n')
    tm.assert_almost_equal(result, expected)