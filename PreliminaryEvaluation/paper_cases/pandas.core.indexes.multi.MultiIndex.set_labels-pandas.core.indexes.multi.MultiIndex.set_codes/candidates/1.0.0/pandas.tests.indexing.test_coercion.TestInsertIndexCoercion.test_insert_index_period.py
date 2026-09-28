@pytest.mark.parametrize('insert, coerced_val, coerced_dtype', [(pd.Period('2012-01', freq='M'), '2012-01', 'period[M]'), (pd.Timestamp('2012-01-01'), pd.Timestamp('2012-01-01'), np.object), (1, 1, np.object), ('x', 'x', np.object)])
def test_insert_index_period(self, insert, coerced_val, coerced_dtype):
    obj = pd.PeriodIndex(['2011-01', '2011-02', '2011-03', '2011-04'], freq='M')
    assert obj.dtype == 'period[M]'
    data = [pd.Period('2011-01', freq='M'), coerced_val, pd.Period('2011-02', freq='M'), pd.Period('2011-03', freq='M'), pd.Period('2011-04', freq='M')]
    if isinstance(insert, pd.Period):
        exp = pd.PeriodIndex(data, freq='M')
        self._assert_insert_conversion(obj, insert, exp, coerced_dtype)
    else:
        msg = "Unexpected keyword arguments {'freq'}"
        with pytest.raises(TypeError, match=msg):
            pd.Index(data, freq='M')