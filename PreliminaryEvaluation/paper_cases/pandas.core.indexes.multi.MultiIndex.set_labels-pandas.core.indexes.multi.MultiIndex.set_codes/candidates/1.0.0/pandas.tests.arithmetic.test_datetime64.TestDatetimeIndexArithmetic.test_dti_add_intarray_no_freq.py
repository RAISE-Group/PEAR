@pytest.mark.parametrize('int_holder', [np.array, pd.Index])
def test_dti_add_intarray_no_freq(self, int_holder):
    dti = pd.DatetimeIndex(['2016-01-01', 'NaT', '2017-04-05 06:07:08'])
    other = int_holder([9, 4, -1])
    msg = '|'.join(['cannot subtract DatetimeArray from', 'Addition/subtraction of integers'])
    assert_invalid_addsub_type(dti, other, msg)