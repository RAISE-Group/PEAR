def test_case_insensitive(self):
    self.cf.register_option('KanBAN', 1, 'doc')
    assert 'doc' in self.cf.describe_option('kanbaN', _print_desc=False)
    assert self.cf.get_option('kanBaN') == 1
    self.cf.set_option('KanBan', 2)
    assert self.cf.get_option('kAnBaN') == 2
    msg = "No such keys\\(s\\): 'no_such_option'"
    with pytest.raises(OptionError, match=msg):
        self.cf.get_option('no_such_option')
    self.cf.deprecate_option('KanBan')
    assert self.cf._is_deprecated('kAnBaN')