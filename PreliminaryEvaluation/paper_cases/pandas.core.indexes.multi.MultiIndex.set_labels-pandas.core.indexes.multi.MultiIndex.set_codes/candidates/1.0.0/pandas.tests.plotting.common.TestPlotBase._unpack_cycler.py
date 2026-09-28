def _unpack_cycler(self, rcParams, field='color'):
    """
        Auxiliary function for correctly unpacking cycler after MPL >= 1.5
        """
    return [v[field] for v in rcParams['axes.prop_cycle']]