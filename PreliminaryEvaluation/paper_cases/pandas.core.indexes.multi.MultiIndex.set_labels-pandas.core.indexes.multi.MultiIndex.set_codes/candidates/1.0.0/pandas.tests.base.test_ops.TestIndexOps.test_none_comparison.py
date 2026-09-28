def test_none_comparison(self):
    for o in self.is_valid_objs:
        if isinstance(o, Series):
            o[0] = np.nan
            result = o == None
            assert not result.iat[0]
            assert not result.iat[1]
            result = o != None
            assert result.iat[0]
            assert result.iat[1]
            result = None == o
            assert not result.iat[0]
            assert not result.iat[1]
            result = None != o
            assert result.iat[0]
            assert result.iat[1]
            if is_datetime64_dtype(o) or is_datetime64tz_dtype(o):
                with pytest.raises(TypeError):
                    None > o
                with pytest.raises(TypeError):
                    o > None
            else:
                result = None > o
                assert not result.iat[0]
                assert not result.iat[1]
                result = o < None
                assert not result.iat[0]
                assert not result.iat[1]