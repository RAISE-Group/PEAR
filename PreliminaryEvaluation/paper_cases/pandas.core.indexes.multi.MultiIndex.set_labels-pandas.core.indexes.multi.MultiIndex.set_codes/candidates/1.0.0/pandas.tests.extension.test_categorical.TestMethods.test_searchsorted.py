def test_searchsorted(self, data_for_sorting):
    if not data_for_sorting.ordered:
        raise pytest.skip(reason='searchsorted requires ordered data.')