def apply_standard(self):
    if self.result_type in ['reduce', None] and (not self.dtypes.apply(is_extension_array_dtype).any()) and (not self.agg_axis._has_complex_internals):
        values = self.values
        index = self.obj._get_axis(self.axis)
        labels = self.agg_axis
        empty_arr = np.empty(len(index), dtype=values.dtype)
        dummy = self.obj._constructor_sliced(empty_arr, index=index, dtype=values.dtype)
        try:
            result = libreduction.compute_reduction(values, self.f, axis=self.axis, dummy=dummy, labels=labels)
        except ValueError as err:
            if 'Function does not reduce' not in str(err):
                raise
        except TypeError:
            if not self.ignore_failures:
                raise
        except ZeroDivisionError:
            pass
        else:
            return self.obj._constructor_sliced(result, index=labels)
    results, res_index = self.apply_series_generator()
    return self.wrap_results(results, res_index)