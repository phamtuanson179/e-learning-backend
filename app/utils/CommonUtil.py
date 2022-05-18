
class CommonUtil:

    def nested_dict(self, obj: object):
        if not  hasattr(obj,"__dict__"):
            return obj
        result = {}
        for key, val in obj.__dict__.items():
            element = []
            if isinstance(val, list):
                for item in val:
                    element.append(self.nested_dict(item))
            else:
                element = self.nested_dict(val)
            result[key] = element
        return result