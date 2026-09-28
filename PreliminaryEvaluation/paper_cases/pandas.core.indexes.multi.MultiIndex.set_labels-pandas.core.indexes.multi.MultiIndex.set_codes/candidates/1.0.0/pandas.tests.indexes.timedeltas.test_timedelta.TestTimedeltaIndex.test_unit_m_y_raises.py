@pytest.mark.parametrize('unit', ['Y', 'y', 'M'])
def test_unit_m_y_raises(self, unit):
    msg = "Units 'M' and 'Y' are no longer supported"
    with pytest.raises(ValueError, match=msg):
        TimedeltaIndex([1, 3, 7], unit)