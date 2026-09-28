@pytest.fixture(params=[[1.5, 2, 3, 4, 5], [0.0, 2.5, 5.0, 7.5, 10.0], [5, 4, 3, 2, 1.5], [10.0, 7.5, 5.0, 2.5, 0.0]], ids=['mixed', 'float', 'mixed_dec', 'float_dec'])
def indices(self, request):
    return Float64Index(request.param)