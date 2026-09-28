@pytest.fixture(params=['dense', 'sparse'])
def sparse(self, request):
    return request.param == 'sparse'