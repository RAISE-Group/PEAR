@pytest.mark.parametrize('pi_freq', ['D', 'W', 'Q', 'H'])
@pytest.mark.parametrize('dti_freq', [None, 'D'])
def test_dt64arr_add_sub_parr(self, dti_freq, pi_freq, box_with_array, box_with_array2):
    dti = pd.DatetimeIndex(['2011-01-01', '2011-01-02'], freq=dti_freq)
    pi = dti.to_period(pi_freq)
    dtarr = tm.box_expected(dti, box_with_array)
    parr = tm.box_expected(pi, box_with_array2)
    msg = '|'.join(['cannot (add|subtract)', 'unsupported operand', 'descriptor.*requires', 'ufunc.*cannot use operands'])
    assert_invalid_addsub_type(dtarr, parr, msg)