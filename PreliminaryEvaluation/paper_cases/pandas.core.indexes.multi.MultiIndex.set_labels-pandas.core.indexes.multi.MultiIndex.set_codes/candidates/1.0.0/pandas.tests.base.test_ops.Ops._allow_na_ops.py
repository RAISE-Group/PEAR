def _allow_na_ops(self, obj):
    """Whether to skip test cases including NaN"""
    if isinstance(obj, Index) and obj.is_boolean() or not obj._can_hold_na:
        return False
    return True