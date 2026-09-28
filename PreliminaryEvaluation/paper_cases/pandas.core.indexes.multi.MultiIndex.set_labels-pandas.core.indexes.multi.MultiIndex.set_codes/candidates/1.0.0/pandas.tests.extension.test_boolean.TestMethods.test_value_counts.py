@pytest.mark.skip(reason='uses nullable integer')
def test_value_counts(self, all_data, dropna):
    return super().test_value_counts(all_data, dropna)