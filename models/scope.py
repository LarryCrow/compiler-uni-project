class Scope:
    def add_variable(self, name, type):
        self.variables.append({
            'name': name,
            'type': type
        })

    def is_variable_exist(self, name):
        for el in self.variables:
            if el['name'] == name:
                return el
        return None

    def __init__(self, s_id, scope=None, variables=None):
        self.s_id = s_id
        self.scope = scope
        self.variables = variables if variables is not None else []
