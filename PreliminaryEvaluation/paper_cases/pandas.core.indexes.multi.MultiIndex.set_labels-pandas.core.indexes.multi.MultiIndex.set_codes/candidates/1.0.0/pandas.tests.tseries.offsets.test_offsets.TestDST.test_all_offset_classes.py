@pytest.mark.parametrize('tup', offset_classes)
def test_all_offset_classes(self, tup):
    offset, test_values = tup
    first = Timestamp(test_values[0], tz='US/Eastern') + offset()
    second = Timestamp(test_values[1], tz='US/Eastern')
    assert first == second