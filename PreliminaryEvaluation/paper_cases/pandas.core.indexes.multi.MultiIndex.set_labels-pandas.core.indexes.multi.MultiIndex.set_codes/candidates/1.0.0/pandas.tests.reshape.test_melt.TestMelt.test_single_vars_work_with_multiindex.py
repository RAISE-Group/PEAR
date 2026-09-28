def test_single_vars_work_with_multiindex(self):
    expected = DataFrame({'A': {0: 1.067683, 1: -1.321405, 2: -0.807333}, 'CAP': {0: 'B', 1: 'B', 2: 'B'}, 'value': {0: -1.110463, 1: 0.368915, 2: 0.08298}})
    result = self.df1.melt(['A'], ['B'], col_level=0)
    tm.assert_frame_equal(result, expected)