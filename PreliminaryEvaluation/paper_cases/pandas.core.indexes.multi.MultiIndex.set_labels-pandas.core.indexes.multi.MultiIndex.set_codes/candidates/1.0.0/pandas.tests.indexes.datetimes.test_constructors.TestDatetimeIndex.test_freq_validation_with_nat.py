@pytest.mark.parametrize('dt_cls', [DatetimeIndex, DatetimeArray._from_sequence])
def test_freq_validation_with_nat(self, dt_cls):
    msg = 'Inferred frequency None from passed values does not conform to passed frequency D'
    with pytest.raises(ValueError, match=msg):
        dt_cls([pd.NaT, pd.Timestamp('2011-01-01')], freq='D')
    with pytest.raises(ValueError, match=msg):
        dt_cls([pd.NaT, pd.Timestamp('2011-01-01').value], freq='D')