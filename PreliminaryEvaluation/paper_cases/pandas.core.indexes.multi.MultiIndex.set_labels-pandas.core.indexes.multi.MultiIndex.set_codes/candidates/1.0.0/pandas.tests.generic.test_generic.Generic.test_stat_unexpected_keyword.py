def test_stat_unexpected_keyword(self):
    obj = self._construct(5)
    starwars = 'Star Wars'
    errmsg = 'unexpected keyword'
    with pytest.raises(TypeError, match=errmsg):
        obj.max(epic=starwars)
    with pytest.raises(TypeError, match=errmsg):
        obj.var(epic=starwars)
    with pytest.raises(TypeError, match=errmsg):
        obj.sum(epic=starwars)
    with pytest.raises(TypeError, match=errmsg):
        obj.any(epic=starwars)