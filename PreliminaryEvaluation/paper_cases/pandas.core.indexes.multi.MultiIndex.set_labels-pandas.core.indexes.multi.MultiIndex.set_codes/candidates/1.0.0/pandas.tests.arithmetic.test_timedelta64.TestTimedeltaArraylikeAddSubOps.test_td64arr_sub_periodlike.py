@pytest.mark.parametrize('pi_freq', ['D', 'W', 'Q', 'H'])
@pytest.mark.parametrize('tdi_freq', [None, 'H'])
def test_td64arr_sub_periodlike(self, box_with_array, tdi_freq, pi_freq):
    tdi = TimedeltaIndex(['1 hours', '2 hours'], freq=tdi_freq)
    dti = Timestamp('2018-03-07 17:16:40') + tdi
    pi = dti.to_period(pi_freq)
    tdi = tm.box_expected(tdi, box_with_array)
    with pytest.raises(TypeError):
        tdi - pi
    with pytest.raises(TypeError):
        tdi - pi[0]
    with pytest.raises(TypeError):
        pi[0] - tdi