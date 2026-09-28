def test_global_scope(self, engine, parser):
    e = '_var_s * 2'
    tm.assert_numpy_array_equal(_var_s * 2, pd.eval(e, engine=engine, parser=parser))