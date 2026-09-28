@pytest.fixture(params=[tm.makeDateIndex(10), date_range('20130110', periods=10, freq='-1D')], ids=['index_inc', 'index_dec'])
def indices(self, request):
    return request.param