@pytest.fixture(params=[operator.eq, operator.ne])
def op(self, request):
    return request.param