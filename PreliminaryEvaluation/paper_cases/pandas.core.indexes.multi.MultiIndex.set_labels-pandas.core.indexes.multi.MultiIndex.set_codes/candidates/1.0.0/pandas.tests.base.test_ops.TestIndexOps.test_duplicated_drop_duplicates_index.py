def test_duplicated_drop_duplicates_index(self):
    for original in self.objs:
        if isinstance(original, Index):
            if original.is_boolean():
                result = original.drop_duplicates()
                expected = Index([False, True], name='a')
                tm.assert_index_equal(result, expected)
                continue
            expected = np.array([False] * len(original), dtype=bool)
            duplicated = original.duplicated()
            tm.assert_numpy_array_equal(duplicated, expected)
            assert duplicated.dtype == bool
            result = original.drop_duplicates()
            tm.assert_index_equal(result, original)
            assert result is not original
            assert not original.has_duplicates
            idx = original[list(range(len(original))) + [5, 3]]
            expected = np.array([False] * len(original) + [True, True], dtype=bool)
            duplicated = idx.duplicated()
            tm.assert_numpy_array_equal(duplicated, expected)
            assert duplicated.dtype == bool
            tm.assert_index_equal(idx.drop_duplicates(), original)
            base = [False] * len(idx)
            base[3] = True
            base[5] = True
            expected = np.array(base)
            duplicated = idx.duplicated(keep='last')
            tm.assert_numpy_array_equal(duplicated, expected)
            assert duplicated.dtype == bool
            result = idx.drop_duplicates(keep='last')
            tm.assert_index_equal(result, idx[~expected])
            base = [False] * len(original) + [True, True]
            base[3] = True
            base[5] = True
            expected = np.array(base)
            duplicated = idx.duplicated(keep=False)
            tm.assert_numpy_array_equal(duplicated, expected)
            assert duplicated.dtype == bool
            result = idx.drop_duplicates(keep=False)
            tm.assert_index_equal(result, idx[~expected])
            with pytest.raises(TypeError, match='drop_duplicates\\(\\) got an unexpected keyword argument'):
                idx.drop_duplicates(inplace=True)
        else:
            expected = Series([False] * len(original), index=original.index, name='a')
            tm.assert_series_equal(original.duplicated(), expected)
            result = original.drop_duplicates()
            tm.assert_series_equal(result, original)
            assert result is not original
            idx = original.index[list(range(len(original))) + [5, 3]]
            values = original._values[list(range(len(original))) + [5, 3]]
            s = Series(values, index=idx, name='a')
            expected = Series([False] * len(original) + [True, True], index=idx, name='a')
            tm.assert_series_equal(s.duplicated(), expected)
            tm.assert_series_equal(s.drop_duplicates(), original)
            base = [False] * len(idx)
            base[3] = True
            base[5] = True
            expected = Series(base, index=idx, name='a')
            tm.assert_series_equal(s.duplicated(keep='last'), expected)
            tm.assert_series_equal(s.drop_duplicates(keep='last'), s[~np.array(base)])
            base = [False] * len(original) + [True, True]
            base[3] = True
            base[5] = True
            expected = Series(base, index=idx, name='a')
            tm.assert_series_equal(s.duplicated(keep=False), expected)
            tm.assert_series_equal(s.drop_duplicates(keep=False), s[~np.array(base)])
            s.drop_duplicates(inplace=True)
            tm.assert_series_equal(s, original)