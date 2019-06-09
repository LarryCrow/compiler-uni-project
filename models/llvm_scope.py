class Scope_llvm:
  def add_variable(self, var_type, var_name, llvm_name, options=None):
        self.variables.append({
            'type': var_type,
            'name': var_name,
            'llvm_name': llvm_name,
            'options': options
        })

  def is_variable_exist(self, name, one_level_search=False, scope=None):
      cur_scope = self if scope is None else scope
      for el in cur_scope.variables:
          if el['name'] == name:
              return el
      if not one_level_search and cur_scope.scope is not None:
          return cur_scope.is_variable_exist(name, one_level_search, cur_scope.scope)
      return None

  def get_llvm_name(self, name, one_level_search=False, scope = None):
      cur_scope = self if scope is None else scope
      for el in cur_scope.variables:
          if el['name'] == name:
              return el['llvm_name']
      if not one_level_search and cur_scope.scope is not None:
          return cur_scope.get_llvm_name(name, one_level_search, cur_scope.scope)
      return None


  def get_llvm_var(self, name, one_level_search=False, scope = None):
      cur_scope = self if scope is None else scope
      for el in cur_scope.variables:
          if el['name'] == name:
              return el
      if not one_level_search and cur_scope.scope is not None:
          return cur_scope.get_llvm_var(name, one_level_search, cur_scope.scope)
      return None


  def change_llvm_name(self, name, llvm_name):
      for el in self.variables:
          if el['name'] == name:
              el['llvm_name'] = llvm_name
              break

  def __init__(self, scope=None, variables=None):
      self.scope = scope
      self.variables = variables if variables is not None else []