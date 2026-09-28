def test_series_frame_commutativity(self, engine, parser):
    args = product(self.lhs_index_types, self.index_types, ('+', '*'), ('index', 'columns'))
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('always', RuntimeWarning)
        for r_idx_type, c_idx_type, op, index_name in args:
            df = tm.makeCustomDataframe(10, 10, data_gen_f=f, r_idx_type=r_idx_type, c_idx_type=c_idx_type)
            index = getattr(df, index_name)
            s = Series(np.random.randn(5), index[:5])
            lhs = f's {op} df'
            rhs = f'df {op} s'
            if should_warn(df.index, s.index):
                with tm.assert_produces_warning(RuntimeWarning):
                    a = pd.eval(lhs, engine=engine, parser=parser)
                with tm.assert_produces_warning(RuntimeWarning):
                    b = pd.eval(rhs, engine=engine, parser=parser)
            else:
                a = pd.eval(lhs, engine=engine, parser=parser)
                b = pd.eval(rhs, engine=engine, parser=parser)
            if r_idx_type != 'dt' and c_idx_type != 'dt':
                if engine == 'numexpr':
                    tm.assert_frame_equal(a, b)