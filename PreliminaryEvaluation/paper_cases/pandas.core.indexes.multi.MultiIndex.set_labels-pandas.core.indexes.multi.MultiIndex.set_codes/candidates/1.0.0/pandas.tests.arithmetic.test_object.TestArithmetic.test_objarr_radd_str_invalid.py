@pytest.mark.parametrize('data', [[1, 2, 3], [1.1, 2.2, 3.3], [Timestamp('2011-01-01'), Timestamp('2011-01-02'), pd.NaT], ['x', 'y', 1]])
@pytest.mark.parametrize('dtype', [None, object])
def test_objarr_radd_str_invalid(self, dtype, data, box_with_array):
    ser = Series(data, dtype=dtype)
    ser = tm.box_expected(ser, box_with_array)
    with pytest.raises(TypeError):
        'foo_' + ser