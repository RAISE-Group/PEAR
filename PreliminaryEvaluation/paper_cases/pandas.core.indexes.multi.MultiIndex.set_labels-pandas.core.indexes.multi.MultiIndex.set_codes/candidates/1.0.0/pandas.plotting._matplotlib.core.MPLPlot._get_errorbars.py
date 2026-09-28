def _get_errorbars(self, label=None, index=None, xerr=True, yerr=True):
    errors = {}
    for kw, flag in zip(['xerr', 'yerr'], [xerr, yerr]):
        if flag:
            err = self.errors[kw]
            if isinstance(err, (ABCDataFrame, dict)):
                if label is not None and label in err.keys():
                    err = err[label]
                else:
                    err = None
            elif index is not None and err is not None:
                err = err[index]
            if err is not None:
                errors[kw] = err
    return errors