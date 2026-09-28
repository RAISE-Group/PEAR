def test_from_records_with_index_data(self):
    df = DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'])
    data = np.random.randn(10)
    df1 = DataFrame.from_records(df, index=data)
    tm.assert_index_equal(df1.index, Index(data))