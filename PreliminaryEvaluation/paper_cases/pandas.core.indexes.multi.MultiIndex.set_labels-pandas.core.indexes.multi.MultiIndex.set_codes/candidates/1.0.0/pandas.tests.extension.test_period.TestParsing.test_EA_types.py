@pytest.mark.parametrize('engine', ['c', 'python'])
def test_EA_types(self, engine, data):
    super().test_EA_types(engine, data)