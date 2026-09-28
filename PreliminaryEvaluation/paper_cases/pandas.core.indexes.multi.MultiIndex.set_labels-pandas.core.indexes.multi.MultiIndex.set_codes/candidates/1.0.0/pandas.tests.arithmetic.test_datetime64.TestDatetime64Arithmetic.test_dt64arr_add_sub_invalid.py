@pytest.mark.parametrize('other', [3.14, np.array([2.0, 3.0]), pd.Period('2011-01-01', freq='D')])
@pytest.mark.parametrize('dti_freq', [None, 'D'])
def test_dt64arr_add_sub_invalid(self, dti_freq, other, box_with_array):
    dti = DatetimeIndex(['2011-01-01', '2011-01-02'], freq=dti_freq)
    dtarr = tm.box_expected(dti, box_with_array)
    msg = '|'.join(['unsupported operand type', 'cannot (add|subtract)', 'cannot use operands with types', "ufunc '?(add|subtract)'? cannot use operands with types"])
    assert_invalid_addsub_type(dtarr, other, msg)