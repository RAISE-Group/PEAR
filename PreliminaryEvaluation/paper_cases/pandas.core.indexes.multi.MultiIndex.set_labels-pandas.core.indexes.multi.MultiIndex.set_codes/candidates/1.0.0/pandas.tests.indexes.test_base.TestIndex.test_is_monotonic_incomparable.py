@pytest.mark.parametrize('attr', ['is_monotonic_increasing', 'is_monotonic_decreasing', '_is_strictly_monotonic_increasing', '_is_strictly_monotonic_decreasing'])
def test_is_monotonic_incomparable(self, attr):
    index = Index([5, datetime.now(), 7])
    assert not getattr(index, attr)