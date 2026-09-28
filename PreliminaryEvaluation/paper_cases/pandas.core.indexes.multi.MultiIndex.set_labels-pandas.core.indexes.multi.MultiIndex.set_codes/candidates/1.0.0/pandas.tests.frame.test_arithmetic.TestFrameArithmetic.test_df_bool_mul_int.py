def test_df_bool_mul_int(self):
    df = pd.DataFrame([[False, True], [False, False]])
    result = df * 1
    kinds = result.dtypes.apply(lambda x: x.kind)
    assert (kinds == 'i').all()
    result = 1 * df
    kinds = result.dtypes.apply(lambda x: x.kind)
    assert (kinds == 'i').all()