@pytest.fixture(params=indexes)
def index(self, request):
    return request.param