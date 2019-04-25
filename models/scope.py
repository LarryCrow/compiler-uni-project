class Scope:
    def add_variable(self, var_name, var_type, options=None):
        self.variables.append({
            'name': var_name,
            'type': var_type,
            'options': options
        })

    # def is_variable_exist(self, name, one_level_search=True, scope=None):
    #     cur_scope = self if scope is None else scope
    #     for el in cur_scope.variables:
    #         if el['name'] == name:
    #             return el
    #     if not one_level_search and cur_scope.scope is not None:
    #         return cur_scope.is_variable_exist(name, one_level_search, cur_scope)
    #     return None

    def is_variable_exist(self, name):
        for el in self.variables:
            if el['name'] == name:
                return el
        return None

    def __init__(self, s_id, scope=None, variables=None):
        self.s_id = s_id
        self.scope = scope
        self.variables = variables if variables is not None else []
