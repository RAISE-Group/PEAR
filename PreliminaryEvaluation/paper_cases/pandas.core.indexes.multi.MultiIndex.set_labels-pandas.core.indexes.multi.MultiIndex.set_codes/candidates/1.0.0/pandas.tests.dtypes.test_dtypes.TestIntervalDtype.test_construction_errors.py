@pytest.mark.parametrize('subtype', ['xx', 'IntervalA', 'Interval[foo]'])
def test_construction_errors(self, subtype):
    msg = 'could not construct IntervalDtype'
    with pytest.raises(TypeError, match=msg):
        IntervalDtype(subtype)