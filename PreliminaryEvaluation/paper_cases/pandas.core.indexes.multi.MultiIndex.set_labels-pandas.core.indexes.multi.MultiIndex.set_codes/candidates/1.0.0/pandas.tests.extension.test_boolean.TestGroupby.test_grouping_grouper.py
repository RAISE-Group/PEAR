def test_grouping_grouper(self, data_for_grouping):
    df = pd.DataFrame({'A': ['B', 'B', None, None, 'A', 'A', 'B'], 'B': data_for_grouping})
    gr1 = df.groupby('A').grouper.groupings[0]
    gr2 = df.groupby('B').grouper.groupings[0]
    tm.assert_numpy_array_equal(gr1.grouper, df.A.values)
    tm.assert_extension_array_equal(gr2.grouper, data_for_grouping)