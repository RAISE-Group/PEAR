@pytest.mark.parametrize('engine', ['c', 'python'])
def test_EA_types(self, engine, data):
    expected_msg = '.*must implement _from_sequence_of_strings.*'
    with pytest.raises(NotImplementedError, match=expected_msg):
        super().test_EA_types(engine, data)