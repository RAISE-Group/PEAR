def test_append_series(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        ss = tm.makeStringSeries()
        ts = tm.makeTimeSeries()
        ns = Series(np.arange(100))
        store.append('ss', ss)
        result = store['ss']
        tm.assert_series_equal(result, ss)
        assert result.name is None
        store.append('ts', ts)
        result = store['ts']
        tm.assert_series_equal(result, ts)
        assert result.name is None
        ns.name = 'foo'
        store.append('ns', ns)
        result = store['ns']
        tm.assert_series_equal(result, ns)
        assert result.name == ns.name
        expected = ns[ns > 60]
        result = store.select('ns', 'foo>60')
        tm.assert_series_equal(result, expected)
        expected = ns[(ns > 70) & (ns.index < 90)]
        result = store.select('ns', 'foo>70 and index<90')
        tm.assert_series_equal(result, expected)
        mi = DataFrame(np.random.randn(5, 1), columns=['A'])
        mi['B'] = np.arange(len(mi))
        mi['C'] = 'foo'
        mi.loc[3:5, 'C'] = 'bar'
        mi.set_index(['C', 'B'], inplace=True)
        s = mi.stack()
        s.index = s.index.droplevel(2)
        store.append('mi', s)
        tm.assert_series_equal(store['mi'], s)