@pytest.fixture(params=['uint8', 'i8', np.float64, bool, None])
def dtype(self, request):
    return np.dtype(request.param)