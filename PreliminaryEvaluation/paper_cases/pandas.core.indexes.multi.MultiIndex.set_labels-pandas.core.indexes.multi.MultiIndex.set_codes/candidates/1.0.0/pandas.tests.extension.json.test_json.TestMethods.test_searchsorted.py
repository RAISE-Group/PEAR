@pytest.mark.skip(reason="Can't compare dicts.")
def test_searchsorted(self, data_for_sorting):
    super().test_searchsorted(data_for_sorting)