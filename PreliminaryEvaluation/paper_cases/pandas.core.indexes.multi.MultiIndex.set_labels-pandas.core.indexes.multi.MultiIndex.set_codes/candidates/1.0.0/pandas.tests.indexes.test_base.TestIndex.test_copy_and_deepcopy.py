@pytest.mark.parametrize('index', ['int', 'uint', 'float'], indirect=True)
def test_copy_and_deepcopy(self, index):
    new_copy2 = index.copy(dtype=int)
    assert new_copy2.dtype.kind == 'i'