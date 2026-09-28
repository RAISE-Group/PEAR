@pytest.mark.parametrize('get_dummies_kwargs,expected', [({'data': pd.DataFrame({'ä': ['a']})}, pd.DataFrame({'ä_a': [1]}, dtype=np.uint8)), ({'data': pd.DataFrame({'x': ['ä']})}, pd.DataFrame({'x_ä': [1]}, dtype=np.uint8)), ({'data': pd.DataFrame({'x': ['a']}), 'prefix': 'ä'}, pd.DataFrame({'ä_a': [1]}, dtype=np.uint8)), ({'data': pd.DataFrame({'x': ['a']}), 'prefix_sep': 'ä'}, pd.DataFrame({'xäa': [1]}, dtype=np.uint8))])
def test_dataframe_dummies_unicode(self, get_dummies_kwargs, expected):
    result = get_dummies(**get_dummies_kwargs)
    tm.assert_frame_equal(result, expected)