def test_regex_replace_scalar(self, mix_ab):
    obj = {'a': list('ab..'), 'b': list('efgh')}
    dfobj = DataFrame(obj)
    dfmix = DataFrame(mix_ab)
    res = dfobj.replace('\\s*\\.\\s*', np.nan, regex=True)
    tm.assert_frame_equal(dfobj, res.fillna('.'))
    res = dfmix.replace('\\s*\\.\\s*', np.nan, regex=True)
    tm.assert_frame_equal(dfmix, res.fillna('.'))
    res = dfobj.replace('\\s*(\\.)\\s*', '\\1\\1\\1', regex=True)
    objc = obj.copy()
    objc['a'] = ['a', 'b', '...', '...']
    expec = DataFrame(objc)
    tm.assert_frame_equal(res, expec)
    res = dfmix.replace('\\s*(\\.)\\s*', '\\1\\1\\1', regex=True)
    mixc = mix_ab.copy()
    mixc['b'] = ['a', 'b', '...', '...']
    expec = DataFrame(mixc)
    tm.assert_frame_equal(res, expec)
    res = dfobj.replace(re.compile('\\s*\\.\\s*'), np.nan, regex=True)
    tm.assert_frame_equal(dfobj, res.fillna('.'))
    res = dfmix.replace(re.compile('\\s*\\.\\s*'), np.nan, regex=True)
    tm.assert_frame_equal(dfmix, res.fillna('.'))
    res = dfobj.replace(re.compile('\\s*(\\.)\\s*'), '\\1\\1\\1')
    objc = obj.copy()
    objc['a'] = ['a', 'b', '...', '...']
    expec = DataFrame(objc)
    tm.assert_frame_equal(res, expec)
    res = dfmix.replace(re.compile('\\s*(\\.)\\s*'), '\\1\\1\\1')
    mixc = mix_ab.copy()
    mixc['b'] = ['a', 'b', '...', '...']
    expec = DataFrame(mixc)
    tm.assert_frame_equal(res, expec)
    res = dfmix.replace(regex=re.compile('\\s*(\\.)\\s*'), value='\\1\\1\\1')
    mixc = mix_ab.copy()
    mixc['b'] = ['a', 'b', '...', '...']
    expec = DataFrame(mixc)
    tm.assert_frame_equal(res, expec)
    res = dfmix.replace(regex='\\s*(\\.)\\s*', value='\\1\\1\\1')
    mixc = mix_ab.copy()
    mixc['b'] = ['a', 'b', '...', '...']
    expec = DataFrame(mixc)
    tm.assert_frame_equal(res, expec)