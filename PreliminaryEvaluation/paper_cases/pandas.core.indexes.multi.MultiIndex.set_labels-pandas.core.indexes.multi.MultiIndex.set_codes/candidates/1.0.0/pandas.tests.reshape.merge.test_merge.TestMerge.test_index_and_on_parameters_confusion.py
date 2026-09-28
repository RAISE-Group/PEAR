def test_index_and_on_parameters_confusion(self):
    msg = "right_index parameter must be of type bool, not <class 'list'>"
    with pytest.raises(ValueError, match=msg):
        merge(self.df, self.df2, how='left', left_index=False, right_index=['key1', 'key2'])
    msg = "left_index parameter must be of type bool, not <class 'list'>"
    with pytest.raises(ValueError, match=msg):
        merge(self.df, self.df2, how='left', left_index=['key1', 'key2'], right_index=False)
    with pytest.raises(ValueError, match=msg):
        merge(self.df, self.df2, how='left', left_index=['key1', 'key2'], right_index=['key1', 'key2'])