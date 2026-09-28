@pytest.mark.skip(reason='Categorical.take buggy')
def test_take_empty(self, data, na_value, na_cmp):
    super().test_take_empty(data, na_value, na_cmp)