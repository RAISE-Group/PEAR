@pytest.mark.xfail(reason='GH#17035 (len of floats is casted back to floats)')
def test_margins_dtype_len(self):
    mi_val = list(product(['bar', 'foo'], ['one', 'two'])) + [('All', '')]
    mi = MultiIndex.from_tuples(mi_val, names=('A', 'B'))
    expected = DataFrame({'dull': [1, 1, 2, 1, 5], 'shiny': [2, 0, 2, 2, 6]}, index=mi).rename_axis('C', axis=1)
    expected['All'] = expected['dull'] + expected['shiny']
    result = self.data.pivot_table(values='D', index=['A', 'B'], columns='C', margins=True, aggfunc=len, fill_value=0)
    tm.assert_frame_equal(expected, result)