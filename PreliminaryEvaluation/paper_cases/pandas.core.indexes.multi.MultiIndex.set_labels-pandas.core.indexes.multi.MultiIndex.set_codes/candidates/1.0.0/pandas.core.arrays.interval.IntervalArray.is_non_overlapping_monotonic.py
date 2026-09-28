@property
@Appender(_interval_shared_docs['is_non_overlapping_monotonic'] % _shared_docs_kwargs)
def is_non_overlapping_monotonic(self):
    if self.closed == 'both':
        return bool((self.right[:-1] < self.left[1:]).all() or (self.left[:-1] > self.right[1:]).all())
    return bool((self.right[:-1] <= self.left[1:]).all() or (self.left[:-1] >= self.right[1:]).all())