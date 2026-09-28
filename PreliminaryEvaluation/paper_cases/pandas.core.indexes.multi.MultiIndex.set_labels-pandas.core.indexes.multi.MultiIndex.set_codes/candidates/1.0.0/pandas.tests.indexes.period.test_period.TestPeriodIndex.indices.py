@pytest.fixture(params=[tm.makePeriodIndex(10), period_range('20130101', periods=10, freq='D')[::-1]], ids=['index_inc', 'index_dec'])
def indices(self, request):
    return request.param