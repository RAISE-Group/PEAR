def _format_strings(self) -> List[str]:
    if self.float_format is None:
        float_format = get_option('display.float_format')
        if float_format is None:
            fmt_str = '{{x: .{prec:d}g}}'.format(prec=get_option('display.precision'))
            float_format = lambda x: fmt_str.format(x=x)
    else:
        float_format = self.float_format
    formatter = self.formatter if self.formatter is not None else lambda x: pprint_thing(x, escape_chars=('\t', '\r', '\n'))

    def _format(x):
        if self.na_rep is not None and is_scalar(x) and isna(x):
            try:
                if x is None:
                    return 'None'
                elif x is NA:
                    return str(NA)
                elif x is NaT or np.isnat(x):
                    return 'NaT'
            except (TypeError, ValueError):
                pass
            return self.na_rep
        elif isinstance(x, PandasObject):
            return '{x}'.format(x=x)
        else:
            return '{x}'.format(x=formatter(x))
    vals = self.values
    if isinstance(vals, Index):
        vals = vals._values
    elif isinstance(vals, ABCSparseArray):
        vals = vals.values
    is_float_type = lib.map_infer(vals, is_float) & notna(vals)
    leading_space = self.leading_space
    if leading_space is None:
        leading_space = is_float_type.any()
    fmt_values = []
    for i, v in enumerate(vals):
        if not is_float_type[i] and leading_space:
            fmt_values.append(' {v}'.format(v=_format(v)))
        elif is_float_type[i]:
            fmt_values.append(float_format(v))
        else:
            if leading_space is False:
                tpl = '{v}'
            else:
                tpl = ' {v}'
            fmt_values.append(tpl.format(v=_format(v)))
    return fmt_values