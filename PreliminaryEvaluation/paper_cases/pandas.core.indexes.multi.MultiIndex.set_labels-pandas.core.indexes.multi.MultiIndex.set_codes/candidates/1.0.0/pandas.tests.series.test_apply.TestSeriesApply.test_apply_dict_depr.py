def test_apply_dict_depr(self):
    tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'], index=pd.date_range('1/1/2000', periods=10))
    msg = 'nested renamer is not supported'
    with pytest.raises(SpecificationError, match=msg):
        tsdf.A.agg({'foo': ['sum', 'mean']})