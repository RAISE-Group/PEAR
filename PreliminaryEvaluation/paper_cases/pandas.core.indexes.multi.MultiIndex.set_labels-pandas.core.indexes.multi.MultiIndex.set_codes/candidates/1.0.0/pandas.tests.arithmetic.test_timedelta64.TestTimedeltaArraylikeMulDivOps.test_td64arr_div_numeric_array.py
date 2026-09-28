@pytest.mark.parametrize('vector', [np.array([20, 30, 40]), pd.Index([20, 30, 40]), Series([20, 30, 40])], ids=lambda x: type(x).__name__)
def test_td64arr_div_numeric_array(self, box_with_array, vector, any_real_dtype):
    xbox = get_upcast_box(box_with_array, vector)
    tdser = pd.Series(['59 Days', '59 Days', 'NaT'], dtype='m8[ns]')
    vector = vector.astype(any_real_dtype)
    expected = Series(['2.95D', '1D 23H 12m', 'NaT'], dtype='timedelta64[ns]')
    tdser = tm.box_expected(tdser, box_with_array)
    expected = tm.box_expected(expected, xbox)
    result = tdser / vector
    tm.assert_equal(result, expected)
    pattern = 'true_divide cannot use operands|cannot perform __div__|cannot perform __truediv__|unsupported operand|Cannot divide'
    with pytest.raises(TypeError, match=pattern):
        vector / tdser
    if not isinstance(vector, pd.Index):
        result = tdser / vector.astype(object)
        if box_with_array is pd.DataFrame:
            expected = [tdser.iloc[0, n] / vector[n] for n in range(len(vector))]
        else:
            expected = [tdser[n] / vector[n] for n in range(len(tdser))]
        expected = tm.box_expected(expected, xbox)
        tm.assert_equal(result, expected)
    with pytest.raises(TypeError, match=pattern):
        vector.astype(object) / tdser