def test_concatlike_same_dtypes(self):
    for typ1, vals1 in self.data.items():
        vals2 = vals1
        vals3 = vals1
        if typ1 == 'category':
            exp_data = pd.Categorical(list(vals1) + list(vals2))
            exp_data3 = pd.Categorical(list(vals1) + list(vals2) + list(vals3))
        else:
            exp_data = vals1 + vals2
            exp_data3 = vals1 + vals2 + vals3
        res = pd.Index(vals1).append(pd.Index(vals2))
        exp = pd.Index(exp_data)
        tm.assert_index_equal(res, exp)
        res = pd.Index(vals1).append([pd.Index(vals2), pd.Index(vals3)])
        exp = pd.Index(exp_data3)
        tm.assert_index_equal(res, exp)
        i1 = pd.Index(vals1, name='x')
        i2 = pd.Index(vals2, name='y')
        res = i1.append(i2)
        exp = pd.Index(exp_data)
        tm.assert_index_equal(res, exp)
        i1 = pd.Index(vals1, name='x')
        i2 = pd.Index(vals2, name='x')
        res = i1.append(i2)
        exp = pd.Index(exp_data, name='x')
        tm.assert_index_equal(res, exp)
        with pytest.raises(TypeError, match='all inputs must be Index'):
            pd.Index(vals1).append(vals2)
        with pytest.raises(TypeError, match='all inputs must be Index'):
            pd.Index(vals1).append([pd.Index(vals2), vals3])
        res = pd.Series(vals1).append(pd.Series(vals2), ignore_index=True)
        exp = pd.Series(exp_data)
        tm.assert_series_equal(res, exp, check_index_type=True)
        res = pd.concat([pd.Series(vals1), pd.Series(vals2)], ignore_index=True)
        tm.assert_series_equal(res, exp, check_index_type=True)
        res = pd.Series(vals1).append([pd.Series(vals2), pd.Series(vals3)], ignore_index=True)
        exp = pd.Series(exp_data3)
        tm.assert_series_equal(res, exp)
        res = pd.concat([pd.Series(vals1), pd.Series(vals2), pd.Series(vals3)], ignore_index=True)
        tm.assert_series_equal(res, exp)
        s1 = pd.Series(vals1, name='x')
        s2 = pd.Series(vals2, name='y')
        res = s1.append(s2, ignore_index=True)
        exp = pd.Series(exp_data)
        tm.assert_series_equal(res, exp, check_index_type=True)
        res = pd.concat([s1, s2], ignore_index=True)
        tm.assert_series_equal(res, exp, check_index_type=True)
        s1 = pd.Series(vals1, name='x')
        s2 = pd.Series(vals2, name='x')
        res = s1.append(s2, ignore_index=True)
        exp = pd.Series(exp_data, name='x')
        tm.assert_series_equal(res, exp, check_index_type=True)
        res = pd.concat([s1, s2], ignore_index=True)
        tm.assert_series_equal(res, exp, check_index_type=True)
        msg = "cannot concatenate object of type '.+'; only Series and DataFrame objs are valid"
        with pytest.raises(TypeError, match=msg):
            pd.Series(vals1).append(vals2)
        with pytest.raises(TypeError, match=msg):
            pd.Series(vals1).append([pd.Series(vals2), vals3])
        with pytest.raises(TypeError, match=msg):
            pd.concat([pd.Series(vals1), vals2])
        with pytest.raises(TypeError, match=msg):
            pd.concat([pd.Series(vals1), pd.Series(vals2), vals3])