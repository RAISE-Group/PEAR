@pytest.mark.parametrize('klass,dtype,na_val', [(pd.Float64Index, np.float64, np.nan), (pd.DatetimeIndex, 'datetime64[ns]', pd.NaT)])
def test_index_ctor_infer_nan_nat(self, klass, dtype, na_val):
    na_list = [na_val, na_val]
    expected = klass(na_list)
    assert expected.dtype == dtype
    result = Index(na_list)
    tm.assert_index_equal(result, expected)
    result = Index(np.array(na_list))
    tm.assert_index_equal(result, expected)