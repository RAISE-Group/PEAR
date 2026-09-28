@pytest.fixture(params=[[0, 'a', 1, 'b', 2, 'c']], ids=['mixedIndex'])
def indices(self, request):
    return Index(request.param)