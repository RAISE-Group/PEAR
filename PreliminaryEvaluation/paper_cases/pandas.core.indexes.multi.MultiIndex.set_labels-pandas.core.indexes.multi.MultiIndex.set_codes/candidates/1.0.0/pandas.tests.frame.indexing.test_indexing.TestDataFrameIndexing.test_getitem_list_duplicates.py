def test_getitem_list_duplicates(self):
    df = DataFrame(np.random.randn(4, 4), columns=list('AABC'))
    df.columns.name = 'foo'
    result = df[['B', 'C']]
    assert result.columns.name == 'foo'
    expected = df.iloc[:, 2:]
    tm.assert_frame_equal(result, expected)