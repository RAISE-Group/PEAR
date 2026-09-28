def test_basic_period_index_boolean_expression(self):
    df = tm.makeCustomDataframe(2, 2, data_gen_f=f, c_idx_type='p', r_idx_type='i')
    e = df < 2
    r = self.eval('df < 2', local_dict={'df': df})
    x = df < 2
    tm.assert_frame_equal(r, e)
    tm.assert_frame_equal(x, e)