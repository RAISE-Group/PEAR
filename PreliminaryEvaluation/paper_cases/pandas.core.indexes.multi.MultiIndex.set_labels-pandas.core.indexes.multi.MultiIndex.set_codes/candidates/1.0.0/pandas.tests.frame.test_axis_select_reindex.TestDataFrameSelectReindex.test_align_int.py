def test_align_int(self, int_frame):
    other = DataFrame(index=range(5), columns=['A', 'B', 'C'])
    af, bf = int_frame.align(other, join='inner', axis=1, method='pad')
    tm.assert_index_equal(bf.columns, other.columns)