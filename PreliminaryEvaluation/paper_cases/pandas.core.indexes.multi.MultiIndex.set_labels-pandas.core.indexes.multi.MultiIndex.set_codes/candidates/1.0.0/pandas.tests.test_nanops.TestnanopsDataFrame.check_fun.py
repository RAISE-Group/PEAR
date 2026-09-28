def check_fun(self, testfunc, targfunc, testar, empty_targfunc=None, **kwargs):
    targar = testar
    if testar.endswith('_nan') and hasattr(self, testar[:-4]):
        targar = testar[:-4]
    testarval = getattr(self, testar)
    targarval = getattr(self, targar)
    self.check_fun_data(testfunc, targfunc, testarval, targarval, empty_targfunc=empty_targfunc, **kwargs)