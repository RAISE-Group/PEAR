def test_unique_id(self):
    df = pd.DataFrame({'a': [1, 3, 5, 6], 'b': [2, 4, 12, 21]})
    result = df.style.render(uuid='test')
    assert 'test' in result
    ids = re.findall('id="(.*?)"', result)
    assert np.unique(ids).size == len(ids)