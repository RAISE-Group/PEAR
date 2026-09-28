@pytest.fixture(params=[[2 ** 63, 2 ** 63 + 10, 2 ** 63 + 15, 2 ** 63 + 20, 2 ** 63 + 25], [2 ** 63 + 25, 2 ** 63 + 20, 2 ** 63 + 15, 2 ** 63 + 10, 2 ** 63]], ids=['index_inc', 'index_dec'])
def indices(self, request):
    return UInt64Index(request.param)