@pytest.mark.parametrize('as_index', [True, False])
def test_groupby_extension_agg(self, as_index, data_for_grouping):
    super().test_groupby_extension_agg(as_index, data_for_grouping)