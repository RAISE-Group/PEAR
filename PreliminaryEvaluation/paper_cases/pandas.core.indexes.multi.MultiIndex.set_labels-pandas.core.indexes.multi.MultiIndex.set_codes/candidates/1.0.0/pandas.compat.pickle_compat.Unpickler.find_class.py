def find_class(self, module, name):
    key = (module, name)
    module, name = _class_locations_map.get(key, key)
    return super().find_class(module, name)