def test_regex_replace_list_mixed_inplace(self, mix_ab):
    dfmix = DataFrame(mix_ab)
    to_replace_res = ['\\s*\\.\\s*', 'a']
    values = [np.nan, 'crap']
    res = dfmix.copy()
    res.replace(to_replace_res, values, inplace=True, regex=True)
    expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b', np.nan, np.nan]})
    tm.assert_frame_equal(res, expec)
    to_replace_res = ['\\s*(\\.)\\s*', '(a|b)']
    values = ['\\1\\1', '\\1_crap']
    res = dfmix.copy()
    res.replace(to_replace_res, values, inplace=True, regex=True)
    expec = DataFrame({'a': mix_ab['a'], 'b': ['a_crap', 'b_crap', '..', '..']})
    tm.assert_frame_equal(res, expec)
    to_replace_res = ['\\s*(\\.)\\s*', 'a', '(b)']
    values = ['\\1\\1', 'crap', '\\1_crap']
    res = dfmix.copy()
    res.replace(to_replace_res, values, inplace=True, regex=True)
    expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b_crap', '..', '..']})
    tm.assert_frame_equal(res, expec)
    to_replace_res = ['\\s*(\\.)\\s*', 'a', '(b)']
    values = ['\\1\\1', 'crap', '\\1_crap']
    res = dfmix.copy()
    res.replace(regex=to_replace_res, value=values, inplace=True)
    expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b_crap', '..', '..']})
    tm.assert_frame_equal(res, expec)