@pytest.mark.parametrize('index', ['int', 'range'], indirect=True)
def test_astype(self, index):
    casted = index.astype('i8')
    casted.get_loc(5)
    index.name = 'foobar'
    casted = index.astype('i8')
    assert casted.name == 'foobar'