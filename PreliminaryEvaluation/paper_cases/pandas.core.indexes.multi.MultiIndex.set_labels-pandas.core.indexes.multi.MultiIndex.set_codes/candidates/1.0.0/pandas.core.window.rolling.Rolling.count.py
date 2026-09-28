@Substitution(name='rolling')
@Appender(_shared_docs['count'])
def count(self):
    if self.is_freq_type:
        window_func = self._get_roll_func('roll_count')
        return self._apply(window_func, center=self.center, name='count')
    return super().count()