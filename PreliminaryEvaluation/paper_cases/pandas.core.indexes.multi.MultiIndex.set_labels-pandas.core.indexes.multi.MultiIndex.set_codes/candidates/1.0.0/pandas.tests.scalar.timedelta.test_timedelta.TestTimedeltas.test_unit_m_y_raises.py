@pytest.mark.parametrize('unit', ['Y', 'y', 'M'])
def test_unit_m_y_raises(self, unit):
    msg = "Units 'M' and 'Y' are no longer supported"
    with pytest.raises(ValueError, match=msg):
        Timedelta(10, unit)
    with pytest.raises(ValueError, match=msg):
        to_timedelta(10, unit)
    with pytest.raises(ValueError, match=msg):
        to_timedelta([1, 2], unit)