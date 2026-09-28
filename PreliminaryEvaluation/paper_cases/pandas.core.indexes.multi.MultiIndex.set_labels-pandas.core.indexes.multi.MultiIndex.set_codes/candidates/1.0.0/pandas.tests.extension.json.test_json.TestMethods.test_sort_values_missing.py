@pytest.mark.parametrize('ascending', [True, False])
def test_sort_values_missing(self, data_missing_for_sorting, ascending):
    super().test_sort_values_missing(data_missing_for_sorting, ascending)