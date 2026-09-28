def _repr_attrs(self):
    out = super()._repr_attrs()
    hours = ','.join((f"{st.strftime('%H:%M')}-{en.strftime('%H:%M')}" for st, en in zip(self.start, self.end)))
    attrs = [f'{self._prefix}={hours}']
    out += ': ' + ', '.join(attrs)
    return out