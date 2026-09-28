@pytest.mark.slow
def test_complex_series_frame_alignment(self, engine, parser):
    import random
    args = product(self.lhs_index_types, self.index_types, self.index_types, self.index_types)
    n = 3
    m1 = 5
    m2 = 2 * m1
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('always', RuntimeWarning)
        for r1, r2, c1, c2 in args:
            index_name = random.choice(['index', 'columns'])
            obj_name = random.choice(['df', 'df2'])
            df = tm.makeCustomDataframe(m1, n, data_gen_f=f, r_idx_type=r1, c_idx_type=c1)
            df2 = tm.makeCustomDataframe(m2, n, data_gen_f=f, r_idx_type=r2, c_idx_type=c2)
            index = getattr(locals().get(obj_name), index_name)
            s = Series(np.random.randn(n), index[:n])
            if r2 == 'dt' or c2 == 'dt':
                if engine == 'numexpr':
                    expected2 = df2.add(s)
                else:
                    expected2 = df2 + s
            else:
                expected2 = df2 + s
            if r1 == 'dt' or c1 == 'dt':
                if engine == 'numexpr':
                    expected = expected2.add(df)
                else:
                    expected = expected2 + df
            else:
                expected = expected2 + df
            if should_warn(df2.index, s.index, df.index):
                with tm.assert_produces_warning(RuntimeWarning):
                    res = pd.eval('df2 + s + df', engine=engine, parser=parser)
            else:
                res = pd.eval('df2 + s + df', engine=engine, parser=parser)
            assert res.shape == expected.shape
            tm.assert_frame_equal(res, expected)