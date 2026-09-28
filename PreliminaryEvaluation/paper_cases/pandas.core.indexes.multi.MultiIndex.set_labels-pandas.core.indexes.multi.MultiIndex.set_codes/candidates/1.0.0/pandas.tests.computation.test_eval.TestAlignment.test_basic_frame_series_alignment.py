def test_basic_frame_series_alignment(self, engine, parser):

    def testit(r_idx_type, c_idx_type, index_name):
        df = tm.makeCustomDataframe(10, 10, data_gen_f=f, r_idx_type=r_idx_type, c_idx_type=c_idx_type)
        index = getattr(df, index_name)
        s = Series(np.random.randn(5), index[:5])
        if should_warn(df.index, s.index):
            with tm.assert_produces_warning(RuntimeWarning):
                res = pd.eval('df + s', engine=engine, parser=parser)
        else:
            res = pd.eval('df + s', engine=engine, parser=parser)
        if r_idx_type == 'dt' or c_idx_type == 'dt':
            expected = df.add(s) if engine == 'numexpr' else df + s
        else:
            expected = df + s
        tm.assert_frame_equal(res, expected)
    args = product(self.lhs_index_types, self.index_types, ('index', 'columns'))
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('always', RuntimeWarning)
        for r_idx_type, c_idx_type, index_name in args:
            testit(r_idx_type, c_idx_type, index_name)