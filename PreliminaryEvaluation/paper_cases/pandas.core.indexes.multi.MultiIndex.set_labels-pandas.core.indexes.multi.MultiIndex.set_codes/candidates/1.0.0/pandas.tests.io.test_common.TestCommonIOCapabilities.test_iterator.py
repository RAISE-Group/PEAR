def test_iterator(self):
    reader = pd.read_csv(StringIO(self.data1), chunksize=1)
    result = pd.concat(reader, ignore_index=True)
    expected = pd.read_csv(StringIO(self.data1))
    tm.assert_frame_equal(result, expected)
    it = pd.read_csv(StringIO(self.data1), chunksize=1)
    first = next(it)
    tm.assert_frame_equal(first, expected.iloc[[0]])
    tm.assert_frame_equal(pd.concat(it), expected.iloc[1:])