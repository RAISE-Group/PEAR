@pytest.mark.xfail(reason='bad is-na for empty data')
def test_from_sequence_from_cls(self, data):
    super().test_from_sequence_from_cls(data)