def test_concatlike_dtypes_coercion(self):
    for typ1, vals1 in self.data.items():
        for typ2, vals2 in self.data.items():
            vals3 = vals2
            exp_index_dtype = None
            exp_series_dtype = None
            if typ1 == typ2:
                continue
            elif typ1 == 'category' or typ2 == 'category':
                continue
            if typ1 == 'bool' and typ2 in ('int64', 'float64'):
                exp_series_dtype = typ2
            elif typ2 == 'bool' and typ1 in ('int64', 'float64'):
                exp_series_dtype = typ1
            elif typ1 == 'datetime64[ns, US/Eastern]' or typ2 == 'datetime64[ns, US/Eastern]' or typ1 == 'timedelta64[ns]' or (typ2 == 'timedelta64[ns]'):
                exp_index_dtype = object
                exp_series_dtype = object
            exp_data = vals1 + vals2
            exp_data3 = vals1 + vals2 + vals3
            res = pd.Index(vals1).append(pd.Index(vals2))
            exp = pd.Index(exp_data, dtype=exp_index_dtype)
            tm.assert_index_equal(res, exp)
            res = pd.Index(vals1).append([pd.Index(vals2), pd.Index(vals3)])
            exp = pd.Index(exp_data3, dtype=exp_index_dtype)
            tm.assert_index_equal(res, exp)
            res = pd.Series(vals1).append(pd.Series(vals2), ignore_index=True)
            exp = pd.Series(exp_data, dtype=exp_series_dtype)
            tm.assert_series_equal(res, exp, check_index_type=True)
            res = pd.concat([pd.Series(vals1), pd.Series(vals2)], ignore_index=True)
            tm.assert_series_equal(res, exp, check_index_type=True)
            res = pd.Series(vals1).append([pd.Series(vals2), pd.Series(vals3)], ignore_index=True)
            exp = pd.Series(exp_data3, dtype=exp_series_dtype)
            tm.assert_series_equal(res, exp)
            res = pd.concat([pd.Series(vals1), pd.Series(vals2), pd.Series(vals3)], ignore_index=True)
            tm.assert_series_equal(res, exp)