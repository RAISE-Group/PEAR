def test_basic_frame_alignment(self, engine, parser):
    args = product(self.lhs_index_types, self.index_types, self.index_types)
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('always', RuntimeWarning)
        for lr_idx_type, rr_idx_type, c_idx_type in args:
            df = tm.makeCustomDataframe(10, 10, data_gen_f=f, r_idx_type=lr_idx_type, c_idx_type=c_idx_type)
            df2 = tm.makeCustomDataframe(20, 10, data_gen_f=f, r_idx_type=rr_idx_type, c_idx_type=c_idx_type)
            if should_warn(df.index, df2.index):
                with tm.assert_produces_warning(RuntimeWarning):
                    res = pd.eval('df + df2', engine=engine, parser=parser)
            else:
                res = pd.eval('df + df2', engine=engine, parser=parser)
            tm.assert_frame_equal(res, df + df2)