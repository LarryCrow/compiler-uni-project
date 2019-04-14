
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCOMMArightEQUALSnonassocLORnonassocLANDnonassocEQNEnonassocLEGELTGTleftPLUSMINUSleftMULDIVIDEINTDIVIDEMODULOrightPOWrightUMINUSLNOTleftLBRACERBRACELPARENRPARENLBRACKETRBRACKETBOOLEAN BREAK COLON COMMA COMMENT CONTINUE DATATYPE DIVIDE DO DOT DOUBLE ELSE EQ EQUALS ERROR FUNCTION GE GOTO GT ID IF INTDIVIDE INTEGER LAND LBRACE LBRACKET LE LNOT LOR LPAREN LT MINUS MODULO MUL NE NEWLINE NULL PLUS POW RBRACE RBRACKET RETURN RPAREN SEMI STRING STRUCTURE WHILEprogram :\n               | basic_blockbasic_block : stmt_listfunc_declaration : FUNCTION datatype id LPAREN params RPAREN LBRACE basic_block RBRACEstmt_list : stmt_list statement\n                 | statement\n    statement : expr SEMI\n              | var_declaration\n              | return\n              | assign\n              | func_declaration\n              | struct_declaration\n              | while\n              | BREAK SEMI\n              | CONTINUE SEMI\n              | GOTO ID SEMI\n              | goto_mark\n              | if-else\n    \n    while : WHILE LPAREN expr RPAREN LBRACE stmt_list RBRACE\n          | DO LBRACE stmt_list RBRACE WHILE LPAREN expr RPAREN SEMI\n    \n    if-else : IF LPAREN expr RPAREN LBRACE stmt_list RBRACE\n            | IF LPAREN expr RPAREN LBRACE stmt_list RBRACE ELSE LBRACE stmt_list RBRACE\n    \n    struct_declaration : STRUCTURE id LBRACE params RBRACE\n    \n    expr : ID DOT ID\n    params :\n              | param\n              | params COMMA paramparam : DATATYPE IDexpr : ID LPAREN args RPARENargs :\n            | expr\n            | args COMMA expr\n    var_declaration : datatype id EQUALS expr SEMI\n    assign : ID EQUALS expr SEMI\n    return : RETURN expr SEMI\n           | RETURN SEMI\n    expr : expr PLUS expr\n            | expr MINUS expr\n            | expr MUL expr\n            | expr DIVIDE expr\n            | expr INTDIVIDE expr\n            | expr MODULO expr\n            | expr POW exprexpr : expr LE expr\n            | expr GE expr\n            | expr LT expr\n            | expr GT expr\n            | expr EQ expr\n            | expr NE exprexpr : MINUS expr %prec UMINUS\n            | expr LAND expr\n            | expr LOR expr\n            | LNOT exprexpr : id\n            | INTEGER\n            | DOUBLE\n            | BOOLEAN\n            | STRING\n            | NULL\n            | LPAREN expr RPAREN\n    expr : datatype LBRACKET expr RBRACKET\n    \n    expr : ID LBRACKET expr RBRACKET\n    goto_mark : ID COLONdatatype : DATATYPEid : ID'
    
_lr_action_items = {'$end':([0,1,2,3,4,6,7,8,9,10,11,16,17,35,36,52,53,59,69,90,99,108,119,121,133,135,139,140,143,],[-1,0,-2,-3,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-63,-36,-16,-35,-34,-33,-23,-19,-21,-4,-20,-22,]),'BREAK':([0,3,4,6,7,8,9,10,11,16,17,35,36,52,53,59,69,73,90,99,103,108,119,121,124,126,129,131,132,133,135,139,140,141,142,143,],[12,12,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-63,-36,12,-16,-35,12,-34,-33,-23,12,12,12,12,12,-19,-21,-4,-20,12,12,-22,]),'CONTINUE':([0,3,4,6,7,8,9,10,11,16,17,35,36,52,53,59,69,73,90,99,103,108,119,121,124,126,129,131,132,133,135,139,140,141,142,143,],[13,13,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-63,-36,13,-16,-35,13,-34,-33,-23,13,13,13,13,13,-19,-21,-4,-20,13,13,-22,]),'GOTO':([0,3,4,6,7,8,9,10,11,16,17,35,36,52,53,59,69,73,90,99,103,108,119,121,124,126,129,131,132,133,135,139,140,141,142,143,],[14,14,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-63,-36,14,-16,-35,14,-34,-33,-23,14,14,14,14,14,-19,-21,-4,-20,14,14,-22,]),'ID':([0,3,4,6,7,8,9,10,11,14,16,17,18,19,20,27,28,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,65,69,70,72,73,74,90,98,99,103,106,108,114,119,121,124,126,129,130,131,132,133,135,139,140,141,142,143,],[15,15,-6,-8,-9,-10,-11,-12,-13,54,-17,-18,61,61,61,67,61,67,-64,-5,-7,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,-14,-15,91,61,61,61,-63,61,-36,67,61,15,61,-16,61,-35,15,61,-34,123,-33,-23,15,15,15,61,15,15,-19,-21,-4,-20,15,15,-22,]),'MINUS':([0,3,4,5,6,7,8,9,10,11,15,16,17,18,19,20,21,22,23,24,25,26,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,58,59,60,61,63,64,65,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,96,97,98,99,102,103,104,105,106,107,108,109,110,118,119,121,124,126,129,130,131,132,133,134,135,139,140,141,142,143,],[19,19,-6,38,-8,-9,-10,-11,-12,-13,-65,-17,-18,19,19,19,-54,-55,-56,-57,-58,-59,19,-5,-7,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-14,-15,19,19,19,-63,38,-65,-50,-53,19,38,-36,19,19,19,-37,-38,-39,-40,-41,-42,-43,38,38,38,38,38,38,38,38,-16,-24,38,38,38,-60,38,19,-35,38,19,38,-29,19,-62,-34,-61,38,38,-33,-23,19,19,19,19,19,19,-19,38,-21,-4,-20,19,19,-22,]),'LNOT':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,58,59,65,69,72,73,74,90,98,99,103,106,108,119,121,124,126,129,130,131,132,133,135,139,140,141,142,143,],[20,20,-6,-8,-9,-10,-11,-12,-13,-17,-18,20,20,20,20,-5,-7,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-14,-15,20,20,20,-63,20,-36,20,20,20,-16,20,-35,20,20,-34,-33,-23,20,20,20,20,20,20,-19,-21,-4,-20,20,20,-22,]),'INTEGER':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,58,59,65,69,72,73,74,90,98,99,103,106,108,119,121,124,126,129,130,131,132,133,135,139,140,141,142,143,],[22,22,-6,-8,-9,-10,-11,-12,-13,-17,-18,22,22,22,22,-5,-7,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-14,-15,22,22,22,-63,22,-36,22,22,22,-16,22,-35,22,22,-34,-33,-23,22,22,22,22,22,22,-19,-21,-4,-20,22,22,-22,]),'DOUBLE':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,58,59,65,69,72,73,74,90,98,99,103,106,108,119,121,124,126,129,130,131,132,133,135,139,140,141,142,143,],[23,23,-6,-8,-9,-10,-11,-12,-13,-17,-18,23,23,23,23,-5,-7,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-14,-15,23,23,23,-63,23,-36,23,23,23,-16,23,-35,23,23,-34,-33,-23,23,23,23,23,23,23,-19,-21,-4,-20,23,23,-22,]),'BOOLEAN':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,58,59,65,69,72,73,74,90,98,99,103,106,108,119,121,124,126,129,130,131,132,133,135,139,140,141,142,143,],[24,24,-6,-8,-9,-10,-11,-12,-13,-17,-18,24,24,24,24,-5,-7,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-14,-15,24,24,24,-63,24,-36,24,24,24,-16,24,-35,24,24,-34,-33,-23,24,24,24,24,24,24,-19,-21,-4,-20,24,24,-22,]),'STRING':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,58,59,65,69,72,73,74,90,98,99,103,106,108,119,121,124,126,129,130,131,132,133,135,139,140,141,142,143,],[25,25,-6,-8,-9,-10,-11,-12,-13,-17,-18,25,25,25,25,-5,-7,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-14,-15,25,25,25,-63,25,-36,25,25,25,-16,25,-35,25,25,-34,-33,-23,25,25,25,25,25,25,-19,-21,-4,-20,25,25,-22,]),'NULL':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,58,59,65,69,72,73,74,90,98,99,103,106,108,119,121,124,126,129,130,131,132,133,135,139,140,141,142,143,],[26,26,-6,-8,-9,-10,-11,-12,-13,-17,-18,26,26,26,26,-5,-7,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-14,-15,26,26,26,-63,26,-36,26,26,26,-16,26,-35,26,26,-34,-33,-23,26,26,26,26,26,26,-19,-21,-4,-20,26,26,-22,]),'LPAREN':([0,3,4,6,7,8,9,10,11,15,16,17,18,19,20,28,31,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,58,59,61,65,67,69,72,73,74,90,98,99,100,103,106,108,119,121,124,125,126,129,130,131,132,133,135,139,140,141,142,143,],[18,18,-6,-8,-9,-10,-11,-12,-13,56,-17,-18,18,18,18,18,72,74,-5,-7,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-14,-15,18,18,18,-63,56,18,-65,-36,18,18,18,-16,18,-35,111,18,18,-34,-33,-23,18,130,18,18,18,18,18,-19,-21,-4,-20,18,18,-22,]),'RETURN':([0,3,4,6,7,8,9,10,11,16,17,35,36,52,53,59,69,73,90,99,103,108,119,121,124,126,129,131,132,133,135,139,140,141,142,143,],[28,28,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-63,-36,28,-16,-35,28,-34,-33,-23,28,28,28,28,28,-19,-21,-4,-20,28,28,-22,]),'FUNCTION':([0,3,4,6,7,8,9,10,11,16,17,35,36,52,53,59,69,73,90,99,103,108,119,121,124,126,129,131,132,133,135,139,140,141,142,143,],[29,29,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-63,-36,29,-16,-35,29,-34,-33,-23,29,29,29,29,29,-19,-21,-4,-20,29,29,-22,]),'STRUCTURE':([0,3,4,6,7,8,9,10,11,16,17,35,36,52,53,59,69,73,90,99,103,108,119,121,124,126,129,131,132,133,135,139,140,141,142,143,],[30,30,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-63,-36,30,-16,-35,30,-34,-33,-23,30,30,30,30,30,-19,-21,-4,-20,30,30,-22,]),'WHILE':([0,3,4,6,7,8,9,10,11,16,17,35,36,52,53,59,69,73,90,99,103,108,116,119,121,124,126,129,131,132,133,135,139,140,141,142,143,],[31,31,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-63,-36,31,-16,-35,31,-34,125,-33,-23,31,31,31,31,31,-19,-21,-4,-20,31,31,-22,]),'DO':([0,3,4,6,7,8,9,10,11,16,17,35,36,52,53,59,69,73,90,99,103,108,119,121,124,126,129,131,132,133,135,139,140,141,142,143,],[32,32,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-63,-36,32,-16,-35,32,-34,-33,-23,32,32,32,32,32,-19,-21,-4,-20,32,32,-22,]),'IF':([0,3,4,6,7,8,9,10,11,16,17,35,36,52,53,59,69,73,90,99,103,108,119,121,124,126,129,131,132,133,135,139,140,141,142,143,],[33,33,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-63,-36,33,-16,-35,33,-34,-33,-23,33,33,33,33,33,-19,-21,-4,-20,33,33,-22,]),'DATATYPE':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,28,29,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,58,59,65,69,72,73,74,90,98,99,101,103,106,108,111,119,121,122,124,126,129,130,131,132,133,135,139,140,141,142,143,],[34,34,-6,-8,-9,-10,-11,-12,-13,-17,-18,34,34,34,34,34,-5,-7,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-14,-15,34,34,34,-63,34,-36,34,34,34,-16,34,-35,114,34,34,-34,114,-33,-23,114,34,34,34,34,34,34,-19,-21,-4,-20,34,34,-22,]),'RBRACE':([3,4,6,7,8,9,10,11,16,17,35,36,52,53,59,69,90,99,101,103,108,112,113,119,121,123,128,129,131,133,135,136,139,140,142,143,],[-3,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-63,-36,-16,-35,-25,116,-34,121,-26,-33,-23,-28,-27,133,135,-19,-21,139,-4,-20,143,-22,]),'SEMI':([5,12,13,15,21,22,23,24,25,26,28,54,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,96,105,107,109,110,137,],[36,52,53,-65,-54,-55,-56,-57,-58,-59,69,90,-65,-50,-53,99,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-51,-52,-24,108,-60,-29,-62,-61,119,140,]),'PLUS':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[37,-65,-54,-55,-56,-57,-58,-59,37,-65,-50,-53,37,-37,-38,-39,-40,-41,-42,-43,37,37,37,37,37,37,37,37,-24,37,37,37,-60,37,37,37,-29,-62,-61,37,37,37,]),'MUL':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[39,-65,-54,-55,-56,-57,-58,-59,39,-65,-50,-53,39,39,39,-39,-40,-41,-42,-43,39,39,39,39,39,39,39,39,-24,39,39,39,-60,39,39,39,-29,-62,-61,39,39,39,]),'DIVIDE':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[40,-65,-54,-55,-56,-57,-58,-59,40,-65,-50,-53,40,40,40,-39,-40,-41,-42,-43,40,40,40,40,40,40,40,40,-24,40,40,40,-60,40,40,40,-29,-62,-61,40,40,40,]),'INTDIVIDE':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[41,-65,-54,-55,-56,-57,-58,-59,41,-65,-50,-53,41,41,41,-39,-40,-41,-42,-43,41,41,41,41,41,41,41,41,-24,41,41,41,-60,41,41,41,-29,-62,-61,41,41,41,]),'MODULO':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[42,-65,-54,-55,-56,-57,-58,-59,42,-65,-50,-53,42,42,42,-39,-40,-41,-42,-43,42,42,42,42,42,42,42,42,-24,42,42,42,-60,42,42,42,-29,-62,-61,42,42,42,]),'POW':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[43,-65,-54,-55,-56,-57,-58,-59,43,-65,-50,-53,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-24,43,43,43,-60,43,43,43,-29,-62,-61,43,43,43,]),'LE':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[44,-65,-54,-55,-56,-57,-58,-59,44,-65,-50,-53,44,-37,-38,-39,-40,-41,-42,-43,None,None,None,None,44,44,44,44,-24,44,44,44,-60,44,44,44,-29,-62,-61,44,44,44,]),'GE':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[45,-65,-54,-55,-56,-57,-58,-59,45,-65,-50,-53,45,-37,-38,-39,-40,-41,-42,-43,None,None,None,None,45,45,45,45,-24,45,45,45,-60,45,45,45,-29,-62,-61,45,45,45,]),'LT':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[46,-65,-54,-55,-56,-57,-58,-59,46,-65,-50,-53,46,-37,-38,-39,-40,-41,-42,-43,None,None,None,None,46,46,46,46,-24,46,46,46,-60,46,46,46,-29,-62,-61,46,46,46,]),'GT':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[47,-65,-54,-55,-56,-57,-58,-59,47,-65,-50,-53,47,-37,-38,-39,-40,-41,-42,-43,None,None,None,None,47,47,47,47,-24,47,47,47,-60,47,47,47,-29,-62,-61,47,47,47,]),'EQ':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[48,-65,-54,-55,-56,-57,-58,-59,48,-65,-50,-53,48,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,None,None,48,48,-24,48,48,48,-60,48,48,48,-29,-62,-61,48,48,48,]),'NE':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[49,-65,-54,-55,-56,-57,-58,-59,49,-65,-50,-53,49,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,None,None,49,49,-24,49,49,49,-60,49,49,49,-29,-62,-61,49,49,49,]),'LAND':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[50,-65,-54,-55,-56,-57,-58,-59,50,-65,-50,-53,50,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,None,50,-24,50,50,50,-60,50,50,50,-29,-62,-61,50,50,50,]),'LOR':([5,15,21,22,23,24,25,26,60,61,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,102,104,105,107,109,110,118,134,],[51,-65,-54,-55,-56,-57,-58,-59,51,-65,-50,-53,51,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-51,None,-24,51,51,51,-60,51,51,51,-29,-62,-61,51,51,51,]),'DOT':([15,61,],[55,55,]),'LBRACKET':([15,27,34,61,62,],[57,65,-64,57,65,]),'EQUALS':([15,66,67,],[58,98,-65,]),'COLON':([15,],[59,]),'RPAREN':([21,22,23,24,25,26,56,60,61,63,64,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,96,102,104,105,107,109,111,113,118,120,123,128,134,],[-54,-55,-56,-57,-58,-59,-30,96,-65,-50,-53,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-51,-52,-24,105,-31,-60,115,117,-29,-62,-61,-25,-26,-32,127,-28,-27,137,]),'COMMA':([21,22,23,24,25,26,56,61,63,64,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,96,101,105,107,109,111,112,113,118,120,123,128,],[-54,-55,-56,-57,-58,-59,-30,-65,-50,-53,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-51,-52,-24,106,-31,-60,-25,-29,-62,-61,-25,122,-26,-32,122,-28,-27,]),'RBRACKET':([21,22,23,24,25,26,61,63,64,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,94,96,97,105,107,109,],[-54,-55,-56,-57,-58,-59,-65,-50,-53,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-51,-52,-24,107,-60,109,-29,-62,-61,]),'LBRACE':([32,67,71,115,117,127,138,],[73,-65,101,124,126,132,141,]),'ELSE':([135,],[138,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'basic_block':([0,132,],[2,136,]),'stmt_list':([0,73,124,126,132,141,],[3,103,129,131,3,142,]),'statement':([0,3,73,103,124,126,129,131,132,141,142,],[4,35,4,35,4,4,35,35,4,4,35,]),'expr':([0,3,18,19,20,28,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,58,65,72,73,74,98,103,106,124,126,129,130,131,132,141,142,],[5,5,60,63,64,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,94,95,97,102,5,104,110,5,118,5,5,5,134,5,5,5,5,]),'var_declaration':([0,3,73,103,124,126,129,131,132,141,142,],[6,6,6,6,6,6,6,6,6,6,6,]),'return':([0,3,73,103,124,126,129,131,132,141,142,],[7,7,7,7,7,7,7,7,7,7,7,]),'assign':([0,3,73,103,124,126,129,131,132,141,142,],[8,8,8,8,8,8,8,8,8,8,8,]),'func_declaration':([0,3,73,103,124,126,129,131,132,141,142,],[9,9,9,9,9,9,9,9,9,9,9,]),'struct_declaration':([0,3,73,103,124,126,129,131,132,141,142,],[10,10,10,10,10,10,10,10,10,10,10,]),'while':([0,3,73,103,124,126,129,131,132,141,142,],[11,11,11,11,11,11,11,11,11,11,11,]),'goto_mark':([0,3,73,103,124,126,129,131,132,141,142,],[16,16,16,16,16,16,16,16,16,16,16,]),'if-else':([0,3,73,103,124,126,129,131,132,141,142,],[17,17,17,17,17,17,17,17,17,17,17,]),'id':([0,3,18,19,20,27,28,30,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,58,65,70,72,73,74,98,103,106,124,126,129,130,131,132,141,142,],[21,21,21,21,21,66,21,71,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,100,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'datatype':([0,3,18,19,20,28,29,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,58,65,72,73,74,98,103,106,124,126,129,130,131,132,141,142,],[27,27,62,62,62,62,70,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,27,62,62,27,62,27,27,27,62,27,27,27,27,]),'args':([56,],[92,]),'params':([101,111,],[112,120,]),'param':([101,111,122,],[113,113,128,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> <empty>','program',0,'p_program','doh_parser.py',54),
  ('program -> basic_block','program',1,'p_program','doh_parser.py',55),
  ('basic_block -> stmt_list','basic_block',1,'p_basic_block','doh_parser.py',63),
  ('func_declaration -> FUNCTION datatype id LPAREN params RPAREN LBRACE basic_block RBRACE','func_declaration',9,'p_func_declaration','doh_parser.py',68),
  ('stmt_list -> stmt_list statement','stmt_list',2,'p_stmt_list','doh_parser.py',78),
  ('stmt_list -> statement','stmt_list',1,'p_stmt_list','doh_parser.py',79),
  ('statement -> expr SEMI','statement',2,'p_stmt','doh_parser.py',88),
  ('statement -> var_declaration','statement',1,'p_stmt','doh_parser.py',89),
  ('statement -> return','statement',1,'p_stmt','doh_parser.py',90),
  ('statement -> assign','statement',1,'p_stmt','doh_parser.py',91),
  ('statement -> func_declaration','statement',1,'p_stmt','doh_parser.py',92),
  ('statement -> struct_declaration','statement',1,'p_stmt','doh_parser.py',93),
  ('statement -> while','statement',1,'p_stmt','doh_parser.py',94),
  ('statement -> BREAK SEMI','statement',2,'p_stmt','doh_parser.py',95),
  ('statement -> CONTINUE SEMI','statement',2,'p_stmt','doh_parser.py',96),
  ('statement -> GOTO ID SEMI','statement',3,'p_stmt','doh_parser.py',97),
  ('statement -> goto_mark','statement',1,'p_stmt','doh_parser.py',98),
  ('statement -> if-else','statement',1,'p_stmt','doh_parser.py',99),
  ('while -> WHILE LPAREN expr RPAREN LBRACE stmt_list RBRACE','while',7,'p_loops','doh_parser.py',113),
  ('while -> DO LBRACE stmt_list RBRACE WHILE LPAREN expr RPAREN SEMI','while',9,'p_loops','doh_parser.py',114),
  ('if-else -> IF LPAREN expr RPAREN LBRACE stmt_list RBRACE','if-else',7,'p_if_else','doh_parser.py',124),
  ('if-else -> IF LPAREN expr RPAREN LBRACE stmt_list RBRACE ELSE LBRACE stmt_list RBRACE','if-else',11,'p_if_else','doh_parser.py',125),
  ('struct_declaration -> STRUCTURE id LBRACE params RBRACE','struct_declaration',5,'p_struct_declaration','doh_parser.py',135),
  ('expr -> ID DOT ID','expr',3,'p_struct_field','doh_parser.py',142),
  ('params -> <empty>','params',0,'p_params','doh_parser.py',153),
  ('params -> param','params',1,'p_params','doh_parser.py',154),
  ('params -> params COMMA param','params',3,'p_params','doh_parser.py',155),
  ('param -> DATATYPE ID','param',2,'p_param_declaration','doh_parser.py',176),
  ('expr -> ID LPAREN args RPAREN','expr',4,'p_func_call','doh_parser.py',186),
  ('args -> <empty>','args',0,'p_arguments','doh_parser.py',191),
  ('args -> expr','args',1,'p_arguments','doh_parser.py',192),
  ('args -> args COMMA expr','args',3,'p_arguments','doh_parser.py',193),
  ('var_declaration -> datatype id EQUALS expr SEMI','var_declaration',5,'p_var_declaration','doh_parser.py',209),
  ('assign -> ID EQUALS expr SEMI','assign',4,'p_assign','doh_parser.py',215),
  ('return -> RETURN expr SEMI','return',3,'p_return','doh_parser.py',221),
  ('return -> RETURN SEMI','return',2,'p_return','doh_parser.py',222),
  ('expr -> expr PLUS expr','expr',3,'p_math_expressions','doh_parser.py',236),
  ('expr -> expr MINUS expr','expr',3,'p_math_expressions','doh_parser.py',237),
  ('expr -> expr MUL expr','expr',3,'p_math_expressions','doh_parser.py',238),
  ('expr -> expr DIVIDE expr','expr',3,'p_math_expressions','doh_parser.py',239),
  ('expr -> expr INTDIVIDE expr','expr',3,'p_math_expressions','doh_parser.py',240),
  ('expr -> expr MODULO expr','expr',3,'p_math_expressions','doh_parser.py',241),
  ('expr -> expr POW expr','expr',3,'p_math_expressions','doh_parser.py',242),
  ('expr -> expr LE expr','expr',3,'p_conditionals','doh_parser.py',263),
  ('expr -> expr GE expr','expr',3,'p_conditionals','doh_parser.py',264),
  ('expr -> expr LT expr','expr',3,'p_conditionals','doh_parser.py',265),
  ('expr -> expr GT expr','expr',3,'p_conditionals','doh_parser.py',266),
  ('expr -> expr EQ expr','expr',3,'p_conditionals','doh_parser.py',267),
  ('expr -> expr NE expr','expr',3,'p_conditionals','doh_parser.py',268),
  ('expr -> MINUS expr','expr',2,'p_logical_operation','doh_parser.py',284),
  ('expr -> expr LAND expr','expr',3,'p_logical_operation','doh_parser.py',285),
  ('expr -> expr LOR expr','expr',3,'p_logical_operation','doh_parser.py',286),
  ('expr -> LNOT expr','expr',2,'p_logical_operation','doh_parser.py',287),
  ('expr -> id','expr',1,'p_literals','doh_parser.py',299),
  ('expr -> INTEGER','expr',1,'p_literals','doh_parser.py',300),
  ('expr -> DOUBLE','expr',1,'p_literals','doh_parser.py',301),
  ('expr -> BOOLEAN','expr',1,'p_literals','doh_parser.py',302),
  ('expr -> STRING','expr',1,'p_literals','doh_parser.py',303),
  ('expr -> NULL','expr',1,'p_literals','doh_parser.py',304),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_literals','doh_parser.py',305),
  ('expr -> datatype LBRACKET expr RBRACKET','expr',4,'p_array_init','doh_parser.py',314),
  ('expr -> ID LBRACKET expr RBRACKET','expr',4,'p_index','doh_parser.py',321),
  ('goto_mark -> ID COLON','goto_mark',2,'p_goto_mark','doh_parser.py',327),
  ('datatype -> DATATYPE','datatype',1,'p_datatype','doh_parser.py',332),
  ('id -> ID','id',1,'p_id','doh_parser.py',337),
]
