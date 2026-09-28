@pytest.fixture(params=['average', 'min', 'max', 'first', 'dense'])
def method(self, request):
    """
        Fixture for trying all rank methods
        """
    return request.param