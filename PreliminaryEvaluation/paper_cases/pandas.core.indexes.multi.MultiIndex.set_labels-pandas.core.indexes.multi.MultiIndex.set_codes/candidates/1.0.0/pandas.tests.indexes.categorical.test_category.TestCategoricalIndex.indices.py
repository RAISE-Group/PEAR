@pytest.fixture
def indices(self, request):
    return tm.makeCategoricalIndex(100)