def test_binops_level(self):

    def _check_op(opname):
        op = getattr(DataFrame, opname)
        month_sums = self.ymd.sum(level='month')
        result = op(self.ymd, month_sums, level='month')
        broadcasted = self.ymd.groupby(level='month').transform(np.sum)
        expected = op(self.ymd, broadcasted)
        tm.assert_frame_equal(result, expected)
        op = getattr(Series, opname)
        result = op(self.ymd['A'], month_sums['A'], level='month')
        broadcasted = self.ymd['A'].groupby(level='month').transform(np.sum)
        expected = op(self.ymd['A'], broadcasted)
        expected.name = 'A'
        tm.assert_series_equal(result, expected)
    _check_op('sub')
    _check_op('add')
    _check_op('mul')
    _check_op('div')