def test_sub_fail(self):
    index = tm.makeStringIndex(100)
    with pytest.raises(TypeError):
        index - 'a'
    with pytest.raises(TypeError):
        index - index
    with pytest.raises(TypeError):
        index - index.tolist()
    with pytest.raises(TypeError):
        index.tolist() - index