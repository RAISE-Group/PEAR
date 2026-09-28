def test_regex_replace_list_obj(self):
    obj = {'a': list('ab..'), 'b': list('efgh'), 'c': list('helo')}
    dfobj = DataFrame(obj)
    to_replace_res = ['\\s*\\.\\s*', 'e|f|g']
    values = [np.nan, 'crap']
    res = dfobj.replace(to_replace_res, values, regex=True)
    expec = DataFrame({'a': ['a', 'b', np.nan, np.nan], 'b': ['crap'] * 3 + ['h'], 'c': ['h', 'crap', 'l', 'o']})
    tm.assert_frame_equal(res, expec)
    to_replace_res = ['\\s*(\\.)\\s*', '(e|f|g)']
    values = ['\\1\\1', '\\1_crap']
    res = dfobj.replace(to_replace_res, values, regex=True)
    expec = DataFrame({'a': ['a', 'b', '..', '..'], 'b': ['e_crap', 'f_crap', 'g_crap', 'h'], 'c': ['h', 'e_crap', 'l', 'o']})
    tm.assert_frame_equal(res, expec)
    to_replace_res = ['\\s*(\\.)\\s*', 'e']
    values = ['\\1\\1', 'crap']
    res = dfobj.replace(to_replace_res, values, regex=True)
    expec = DataFrame({'a': ['a', 'b', '..', '..'], 'b': ['crap', 'f', 'g', 'h'], 'c': ['h', 'crap', 'l', 'o']})
    tm.assert_frame_equal(res, expec)
    to_replace_res = ['\\s*(\\.)\\s*', 'e']
    values = ['\\1\\1', 'crap']
    res = dfobj.replace(value=values, regex=to_replace_res)
    expec = DataFrame({'a': ['a', 'b', '..', '..'], 'b': ['crap', 'f', 'g', 'h'], 'c': ['h', 'crap', 'l', 'o']})
    tm.assert_frame_equal(res, expec)