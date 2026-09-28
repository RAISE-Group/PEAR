@pytest.fixture(params=[RangeIndex(start=0, stop=20, step=2, name='foo'), RangeIndex(start=18, stop=-1, step=-2, name='bar')], ids=['index_inc', 'index_dec'])
def indices(self, request):
    return request.param