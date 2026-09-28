def _maybe_coerce_merge_keys(self):
    for lk, rk, name in zip(self.left_join_keys, self.right_join_keys, self.join_names):
        if len(lk) and (not len(rk)) or (not len(lk) and len(rk)):
            continue
        lk_is_cat = is_categorical_dtype(lk)
        rk_is_cat = is_categorical_dtype(rk)
        lk_is_object = is_object_dtype(lk)
        rk_is_object = is_object_dtype(rk)
        if lk_is_cat and rk_is_cat:
            if lk.is_dtype_equal(rk):
                continue
        elif lk_is_cat or rk_is_cat:
            pass
        elif is_dtype_equal(lk.dtype, rk.dtype):
            continue
        msg = 'You are trying to merge on {lk_dtype} and {rk_dtype} columns. If you wish to proceed you should use pd.concat'.format(lk_dtype=lk.dtype, rk_dtype=rk.dtype)
        if is_numeric_dtype(lk) and is_numeric_dtype(rk):
            if lk.dtype.kind == rk.dtype.kind:
                continue
            elif is_integer_dtype(rk) and is_float_dtype(lk):
                if not (lk == lk.astype(rk.dtype))[~np.isnan(lk)].all():
                    warnings.warn('You are merging on int and float columns where the float values are not equal to their int representation', UserWarning)
                continue
            elif is_float_dtype(rk) and is_integer_dtype(lk):
                if not (rk == rk.astype(lk.dtype))[~np.isnan(rk)].all():
                    warnings.warn('You are merging on int and float columns where the float values are not equal to their int representation', UserWarning)
                continue
            elif lib.infer_dtype(lk, skipna=False) == lib.infer_dtype(rk, skipna=False):
                continue
        elif lk_is_object and is_bool_dtype(rk) or (is_bool_dtype(lk) and rk_is_object):
            pass
        elif lk_is_object and is_numeric_dtype(rk) or (is_numeric_dtype(lk) and rk_is_object):
            inferred_left = lib.infer_dtype(lk, skipna=False)
            inferred_right = lib.infer_dtype(rk, skipna=False)
            bool_types = ['integer', 'mixed-integer', 'boolean', 'empty']
            string_types = ['string', 'unicode', 'mixed', 'bytes', 'empty']
            if inferred_left in bool_types and inferred_right in bool_types:
                pass
            elif inferred_left in string_types and inferred_right not in string_types or (inferred_right in string_types and inferred_left not in string_types):
                raise ValueError(msg)
        elif needs_i8_conversion(lk) and (not needs_i8_conversion(rk)):
            raise ValueError(msg)
        elif not needs_i8_conversion(lk) and needs_i8_conversion(rk):
            raise ValueError(msg)
        elif is_datetime64tz_dtype(lk) and (not is_datetime64tz_dtype(rk)):
            raise ValueError(msg)
        elif not is_datetime64tz_dtype(lk) and is_datetime64tz_dtype(rk):
            raise ValueError(msg)
        elif lk_is_object and rk_is_object:
            continue
        if name in self.left.columns:
            typ = lk.categories.dtype if lk_is_cat else object
            self.left = self.left.assign(**{name: self.left[name].astype(typ)})
        if name in self.right.columns:
            typ = rk.categories.dtype if rk_is_cat else object
            self.right = self.right.assign(**{name: self.right[name].astype(typ)})