@pytest.fixture
def index(self, request):
    """
        Fixture for selectively parametrizing indices_dict via indirect parametrization
        (parametrize over indices_dict keys with indirect=True). Defaults to string
        index if no keys are provided.
        """
    key = getattr(request, 'param', 'string')
    return indices_dict[key].copy()