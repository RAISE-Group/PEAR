@pytest.mark.skip(reason="Memory usage doesn't match")
def test_memory_usage(self, data):
    super().test_memory_usage(data)