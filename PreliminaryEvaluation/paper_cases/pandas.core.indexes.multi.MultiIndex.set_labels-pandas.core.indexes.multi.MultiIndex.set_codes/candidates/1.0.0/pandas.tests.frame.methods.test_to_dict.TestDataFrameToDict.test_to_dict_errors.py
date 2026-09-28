@pytest.mark.parametrize('mapping', [list, defaultdict, []])
def test_to_dict_errors(self, mapping):
    df = DataFrame(np.random.randn(3, 3))
    with pytest.raises(TypeError):
        df.to_dict(into=mapping)