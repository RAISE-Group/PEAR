@pytest.fixture(params=[range(0, 20, 2), range(19, -1, -1)], ids=['index_inc', 'index_dec'])
def indices(self, request):
    return Int64Index(request.param)