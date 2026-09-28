def get_loc(self, key, method=None, tolerance=None):
    """
        Get integer location for requested label

        Returns
        -------
        loc : int
        """
    try:
        return self._engine.get_loc(key)
    except KeyError:
        if is_integer(key):
            raise
        try:
            asdt, parsed, reso = parse_time_string(key, self.freq)
            key = asdt
        except TypeError:
            pass
        except DateParseError:
            raise KeyError(f"Cannot interpret '{key}' as period")
        try:
            key = Period(key, freq=self.freq)
        except ValueError:
            raise KeyError(key)
        try:
            ordinal = iNaT if key is NaT else key.ordinal
            if tolerance is not None:
                tolerance = self._convert_tolerance(tolerance, np.asarray(key))
            return self._int64index.get_loc(ordinal, method, tolerance)
        except KeyError:
            raise KeyError(key)