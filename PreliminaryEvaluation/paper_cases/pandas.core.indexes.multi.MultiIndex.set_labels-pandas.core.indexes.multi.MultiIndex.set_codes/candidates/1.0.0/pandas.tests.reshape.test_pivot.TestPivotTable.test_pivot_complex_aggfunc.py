def test_pivot_complex_aggfunc(self):
    f = {'D': ['std'], 'E': ['sum']}
    expected = self.data.groupby(['A', 'B']).agg(f).unstack('B')
    result = self.data.pivot_table(index='A', columns='B', aggfunc=f)
    tm.assert_frame_equal(result, expected)