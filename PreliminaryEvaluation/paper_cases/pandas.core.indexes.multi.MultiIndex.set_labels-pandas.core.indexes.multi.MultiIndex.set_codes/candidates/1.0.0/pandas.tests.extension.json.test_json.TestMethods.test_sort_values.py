@pytest.mark.parametrize('ascending', [True, False])
def test_sort_values(self, data_for_sorting, ascending):
    super().test_sort_values(data_for_sorting, ascending)