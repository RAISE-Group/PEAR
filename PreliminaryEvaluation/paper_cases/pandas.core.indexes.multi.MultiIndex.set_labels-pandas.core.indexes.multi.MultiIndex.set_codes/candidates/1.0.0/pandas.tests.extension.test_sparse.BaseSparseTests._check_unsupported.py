def _check_unsupported(self, data):
    if data.dtype == SparseDtype(int, 0):
        pytest.skip("Can't store nan in int array.")