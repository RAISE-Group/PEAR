def _check_pairwise_moment(self, dispatch, name, **kwargs):

    def get_result(obj, obj2=None):
        return getattr(getattr(obj, dispatch)(**kwargs), name)(obj2)
    result = get_result(self.frame)
    result = result.loc[(slice(None), 1), 5]
    result.index = result.index.droplevel(1)
    expected = get_result(self.frame[1], self.frame[5])
    tm.assert_series_equal(result, expected, check_names=False)