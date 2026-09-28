@pytest.mark.parametrize('other', [10, True, 'foo', Timedelta('1 day'), Timestamp('2018-01-01')], ids=lambda x: type(x).__name__)
def test_overlaps_invalid_type(self, constructor, other):
    interval_container = constructor.from_breaks(range(5))
    msg = f'`other` must be Interval-like, got {type(other).__name__}'
    with pytest.raises(TypeError, match=msg):
        interval_container.overlaps(other)