@pytest.fixture(params=[IntervalIndex, partial(Index, dtype='interval')], ids=['IntervalIndex', 'Index'])
def constructor(self, request):
    return request.param