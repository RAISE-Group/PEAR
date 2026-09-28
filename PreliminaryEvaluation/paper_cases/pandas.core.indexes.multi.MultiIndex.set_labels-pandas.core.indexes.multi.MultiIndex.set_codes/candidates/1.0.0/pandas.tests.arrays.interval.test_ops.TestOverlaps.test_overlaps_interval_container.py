@pytest.mark.parametrize('other_constructor', [IntervalArray, IntervalIndex])
def test_overlaps_interval_container(self, constructor, other_constructor):
    interval_container = constructor.from_breaks(range(5))
    other_container = other_constructor.from_breaks(range(5))
    with pytest.raises(NotImplementedError):
        interval_container.overlaps(other_container)