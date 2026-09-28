@pytest.mark.skip(reason='Setting a dict as a scalar')
def test_fillna_series(self):
    """We treat dictionaries as a mapping in fillna, not a scalar."""