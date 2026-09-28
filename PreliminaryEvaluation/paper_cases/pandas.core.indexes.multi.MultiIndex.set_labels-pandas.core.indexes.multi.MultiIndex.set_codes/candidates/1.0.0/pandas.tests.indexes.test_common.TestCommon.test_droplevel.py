def test_droplevel(self, indices):
    if isinstance(indices, MultiIndex):
        return
    assert indices.droplevel([]).equals(indices)
    for level in (indices.name, [indices.name]):
        if isinstance(indices.name, tuple) and level is indices.name:
            continue
        with pytest.raises(ValueError):
            indices.droplevel(level)
    for level in ('wrong', ['wrong']):
        with pytest.raises(KeyError, match="'Requested level \\(wrong\\) does not match index name \\(None\\)'"):
            indices.droplevel(level)