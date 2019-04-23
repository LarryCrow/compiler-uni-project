
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCOMMArightEQUALSnonassocLORnonassocLANDnonassocBORnonassocBANDnonassocEQNEnonassocLEGELTGTleftPLUSMINUSleftMULDIVIDEINTDIVIDEMODULOrightPOWrightUMINUSLNOTleftLBRACERBRACELPARENRPARENLBRACKETRBRACKETBAND BOOL BOR BREAK COLON COMMA COMMENT CONTINUE DATATYPE DIVIDE DO DOT DOUBLE ELSE EQ EQUALS ERROR FUNCTION GE GOTO GT ID IF INTDIVIDE INTEGER LAND LBRACE LBRACKET LE LNOT LOR LPAREN LT MINUS MODULO MUL NE NEWLINE NULL PLUS POW RBRACE RBRACKET RETURN RPAREN SEMI STRING STRUCTURE VOID WHILEprogram :\n               | basic_blockbasic_block : stmt_listfunc_declaration : FUNCTION datatype id LPAREN params RPAREN LBRACE basic_block RBRACEstmt_list : stmt_list statement\n                 | statement\n    statement : expr SEMI\n              | var_declaration\n              | return\n              | assign\n              | func_declaration\n              | struct_declaration\n              | while\n              | BREAK SEMI\n              | CONTINUE SEMI\n              | GOTO ID SEMI\n              | goto_mark\n              | if-else\n    \n    while : WHILE LPAREN expr RPAREN LBRACE stmt_list RBRACE\n          | DO LBRACE stmt_list RBRACE WHILE LPAREN expr RPAREN SEMI\n    \n    while : WHILE LPAREN error RPAREN LBRACE stmt_list RBRACE\n          | WHILE error expr RPAREN LBRACE stmt_list RBRACE\n          | WHILE LPAREN expr error LBRACE stmt_list RBRACE\n    \n    if-else : IF LPAREN expr RPAREN LBRACE stmt_list RBRACE\n            | IF LPAREN expr RPAREN LBRACE stmt_list RBRACE ELSE LBRACE stmt_list RBRACE\n    \n    struct_declaration : STRUCTURE id LBRACE struct_params RBRACE\n    \n    struct_params : struct_param\n                  | struct_params COMMA struct_param\n    \n    struct_param : DATATYPE ID\n                 | func_declaration\n    params :\n              | param\n              | params COMMA paramparam : DATATYPE IDexpr : ID LPAREN args RPARENargs :\n            | expr\n            | args COMMA expr\n    var_declaration : datatype id EQUALS expr SEMI\n                    | datatype id SEMI\n                    | ID id EQUALS LBRACE args RBRACE SEMI\n    assign : ID EQUALS expr SEMI\n              | ID EQUALS LBRACE args RBRACE SEMI\n              | ID DOT ID EQUALS expr SEMI\n    return : RETURN expr SEMI\n           | RETURN SEMI\n    expr : expr PLUS expr\n            | expr MINUS expr\n            | expr MUL expr\n            | expr DIVIDE expr\n            | expr INTDIVIDE expr\n            | expr MODULO expr\n            | expr POW exprexpr : expr LE expr\n            | expr GE expr\n            | expr LT expr\n            | expr GT expr\n            | expr EQ expr\n            | expr NE exprexpr : MINUS expr %prec UMINUS\n            | expr LAND expr\n            | expr LOR expr\n            | LNOT expr\n    expr : expr BAND expr\n         | expr BOR expr\n    expr : id\n            | int\n            | double\n            | bool\n            | str\n            | void\n            | NULL\n            | LPAREN expr RPARENint : INTEGERdouble : DOUBLEbool : BOOLstr : STRINGvoid : VOID\n    expr : datatype LBRACKET RBRACKET id\n         | datatype LBRACKET RBRACKET id EQUALS datatype LBRACKET INTEGER RBRACKET\n    expr : ID LBRACKET expr RBRACKETgoto_mark : ID COLONdatatype : DATATYPEid : ID'
    
_lr_action_items = {'$end':([0,1,2,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,102,113,114,126,147,151,161,162,174,178,179,180,181,183,189,190,193,],[-1,0,-2,-3,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-82,-46,-16,-40,-45,-42,-39,-26,-43,-44,-41,-19,-23,-21,-22,-24,-4,-20,-25,]),'BREAK':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,83,102,113,114,120,126,147,151,154,155,156,157,159,161,162,168,169,170,171,173,174,176,178,179,180,181,183,189,190,191,192,193,],[12,12,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-82,-46,12,-16,-40,-45,12,-42,-39,-26,12,12,12,12,12,-43,-44,12,12,12,12,12,-41,12,-19,-23,-21,-22,-24,-4,-20,12,12,-25,]),'CONTINUE':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,83,102,113,114,120,126,147,151,154,155,156,157,159,161,162,168,169,170,171,173,174,176,178,179,180,181,183,189,190,191,192,193,],[13,13,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-82,-46,13,-16,-40,-45,13,-42,-39,-26,13,13,13,13,13,-43,-44,13,13,13,13,13,-41,13,-19,-23,-21,-22,-24,-4,-20,13,13,-25,]),'GOTO':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,83,102,113,114,120,126,147,151,154,155,156,157,159,161,162,168,169,170,171,173,174,176,178,179,180,181,183,189,190,191,192,193,],[14,14,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-82,-46,14,-16,-40,-45,14,-42,-39,-26,14,14,14,14,14,-43,-44,14,14,14,14,14,-41,14,-19,-23,-21,-22,-24,-4,-20,14,14,-25,]),'ID':([0,3,4,6,7,8,9,10,11,14,15,16,17,18,19,20,28,30,32,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,68,69,78,79,81,82,83,84,102,108,111,112,113,114,120,123,125,126,128,134,147,150,151,154,155,156,157,159,161,162,168,169,170,171,172,173,174,176,178,179,180,181,183,189,190,191,192,193,],[15,15,-6,-8,-9,-10,-11,-12,-13,62,63,-17,-18,71,71,71,63,71,63,-83,-5,-7,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-14,-15,71,71,71,109,-82,-46,63,71,71,15,71,-16,71,63,71,-40,-45,15,71,71,-42,71,153,-39,166,-26,15,15,15,15,15,-43,-44,15,15,15,15,71,15,-41,15,-19,-23,-21,-22,-24,-4,-20,15,15,-25,]),'MINUS':([0,3,4,5,6,7,8,9,10,11,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,65,67,69,70,71,73,74,77,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,107,108,110,112,113,114,117,119,120,121,122,123,124,125,126,128,129,130,142,145,147,151,154,155,156,157,159,161,162,168,169,170,171,172,173,174,176,178,179,180,181,182,183,188,189,190,191,192,193,],[19,19,-6,44,-8,-9,-10,-11,-12,-13,-84,-17,-18,19,19,19,-66,-67,-68,-69,-70,-71,-72,-74,19,-75,-76,-77,-78,-5,-7,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-14,-15,-84,19,19,19,-82,44,-84,-60,-63,44,-46,19,19,19,19,-47,-48,-49,-50,-51,-52,-53,44,44,44,44,44,44,44,44,44,44,-16,44,44,44,19,-73,19,-40,-45,44,44,19,44,-35,19,-81,19,-42,19,-79,44,44,44,-39,-26,19,19,19,19,19,-43,-44,19,19,19,19,19,19,-41,19,-19,-23,-21,-22,44,-24,-80,-4,-20,19,19,-25,]),'LNOT':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,84,102,108,112,113,114,120,123,125,126,128,147,151,154,155,156,157,159,161,162,168,169,170,171,172,173,174,176,178,179,180,181,183,189,190,191,192,193,],[20,20,-6,-8,-9,-10,-11,-12,-13,-17,-18,20,20,20,20,-5,-7,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-14,-15,20,20,20,-82,-46,20,20,20,20,-16,20,20,-40,-45,20,20,20,-42,20,-39,-26,20,20,20,20,20,-43,-44,20,20,20,20,20,20,-41,20,-19,-23,-21,-22,-24,-4,-20,20,20,-25,]),'NULL':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,84,102,108,112,113,114,120,123,125,126,128,147,151,154,155,156,157,159,161,162,168,169,170,171,172,173,174,176,178,179,180,181,183,189,190,191,192,193,],[27,27,-6,-8,-9,-10,-11,-12,-13,-17,-18,27,27,27,27,-5,-7,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-14,-15,27,27,27,-82,-46,27,27,27,27,-16,27,27,-40,-45,27,27,27,-42,27,-39,-26,27,27,27,27,27,-43,-44,27,27,27,27,27,27,-41,27,-19,-23,-21,-22,-24,-4,-20,27,27,-25,]),'LPAREN':([0,3,4,6,7,8,9,10,11,15,16,17,18,19,20,30,33,35,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,65,67,69,71,78,81,82,83,84,102,108,112,113,114,115,120,123,125,126,128,147,151,154,155,156,157,158,159,161,162,168,169,170,171,172,173,174,176,178,179,180,181,183,189,190,191,192,193,],[18,18,-6,-8,-9,-10,-11,-12,-13,64,-17,-18,18,18,18,18,81,84,-5,-7,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-14,-15,-84,18,18,18,-82,64,-46,18,18,18,18,-16,18,18,-40,-45,131,18,18,18,-42,18,-39,-26,18,18,18,18,172,18,-43,-44,18,18,18,18,18,18,-41,18,-19,-23,-21,-22,-24,-4,-20,18,18,-25,]),'RETURN':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,83,102,113,114,120,126,147,151,154,155,156,157,159,161,162,168,169,170,171,173,174,176,178,179,180,181,183,189,190,191,192,193,],[30,30,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-82,-46,30,-16,-40,-45,30,-42,-39,-26,30,30,30,30,30,-43,-44,30,30,30,30,30,-41,30,-19,-23,-21,-22,-24,-4,-20,30,30,-25,]),'FUNCTION':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,83,102,113,114,116,120,126,147,151,152,154,155,156,157,159,161,162,168,169,170,171,173,174,176,178,179,180,181,183,189,190,191,192,193,],[31,31,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-82,-46,31,-16,-40,-45,31,31,-42,-39,-26,31,31,31,31,31,31,-43,-44,31,31,31,31,31,-41,31,-19,-23,-21,-22,-24,-4,-20,31,31,-25,]),'STRUCTURE':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,83,102,113,114,120,126,147,151,154,155,156,157,159,161,162,168,169,170,171,173,174,176,178,179,180,181,183,189,190,191,192,193,],[32,32,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-82,-46,32,-16,-40,-45,32,-42,-39,-26,32,32,32,32,32,-43,-44,32,32,32,32,32,-41,32,-19,-23,-21,-22,-24,-4,-20,32,32,-25,]),'WHILE':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,83,102,113,114,120,126,140,147,151,154,155,156,157,159,161,162,168,169,170,171,173,174,176,178,179,180,181,183,189,190,191,192,193,],[33,33,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-82,-46,33,-16,-40,-45,33,-42,158,-39,-26,33,33,33,33,33,-43,-44,33,33,33,33,33,-41,33,-19,-23,-21,-22,-24,-4,-20,33,33,-25,]),'DO':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,83,102,113,114,120,126,147,151,154,155,156,157,159,161,162,168,169,170,171,173,174,176,178,179,180,181,183,189,190,191,192,193,],[34,34,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-82,-46,34,-16,-40,-45,34,-42,-39,-26,34,34,34,34,34,-43,-44,34,34,34,34,34,-41,34,-19,-23,-21,-22,-24,-4,-20,34,34,-25,]),'IF':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,83,102,113,114,120,126,147,151,154,155,156,157,159,161,162,168,169,170,171,173,174,176,178,179,180,181,183,189,190,191,192,193,],[35,35,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-82,-46,35,-16,-40,-45,35,-42,-39,-26,35,35,35,35,35,-43,-44,35,35,35,35,35,-41,35,-19,-23,-21,-22,-24,-4,-20,35,35,-25,]),'INTEGER':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,84,102,108,112,113,114,120,123,125,126,128,147,151,154,155,156,157,159,161,162,168,169,170,171,172,173,174,175,176,178,179,180,181,183,189,190,191,192,193,],[29,29,-6,-8,-9,-10,-11,-12,-13,-17,-18,29,29,29,29,-5,-7,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-14,-15,29,29,29,-82,-46,29,29,29,29,-16,29,29,-40,-45,29,29,29,-42,29,-39,-26,29,29,29,29,29,-43,-44,29,29,29,29,29,29,-41,184,29,-19,-23,-21,-22,-24,-4,-20,29,29,-25,]),'DOUBLE':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,84,102,108,112,113,114,120,123,125,126,128,147,151,154,155,156,157,159,161,162,168,169,170,171,172,173,174,176,178,179,180,181,183,189,190,191,192,193,],[36,36,-6,-8,-9,-10,-11,-12,-13,-17,-18,36,36,36,36,-5,-7,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-14,-15,36,36,36,-82,-46,36,36,36,36,-16,36,36,-40,-45,36,36,36,-42,36,-39,-26,36,36,36,36,36,-43,-44,36,36,36,36,36,36,-41,36,-19,-23,-21,-22,-24,-4,-20,36,36,-25,]),'BOOL':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,84,102,108,112,113,114,120,123,125,126,128,147,151,154,155,156,157,159,161,162,168,169,170,171,172,173,174,176,178,179,180,181,183,189,190,191,192,193,],[37,37,-6,-8,-9,-10,-11,-12,-13,-17,-18,37,37,37,37,-5,-7,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-14,-15,37,37,37,-82,-46,37,37,37,37,-16,37,37,-40,-45,37,37,37,-42,37,-39,-26,37,37,37,37,37,-43,-44,37,37,37,37,37,37,-41,37,-19,-23,-21,-22,-24,-4,-20,37,37,-25,]),'STRING':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,84,102,108,112,113,114,120,123,125,126,128,147,151,154,155,156,157,159,161,162,168,169,170,171,172,173,174,176,178,179,180,181,183,189,190,191,192,193,],[38,38,-6,-8,-9,-10,-11,-12,-13,-17,-18,38,38,38,38,-5,-7,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-14,-15,38,38,38,-82,-46,38,38,38,38,-16,38,38,-40,-45,38,38,38,-42,38,-39,-26,38,38,38,38,38,-43,-44,38,38,38,38,38,38,-41,38,-19,-23,-21,-22,-24,-4,-20,38,38,-25,]),'VOID':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,84,102,108,112,113,114,120,123,125,126,128,147,151,154,155,156,157,159,161,162,168,169,170,171,172,173,174,176,178,179,180,181,183,189,190,191,192,193,],[39,39,-6,-8,-9,-10,-11,-12,-13,-17,-18,39,39,39,39,-5,-7,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-14,-15,39,39,39,-82,-46,39,39,39,39,-16,39,39,-40,-45,39,39,39,-42,39,-39,-26,39,39,39,39,39,-43,-44,39,39,39,39,39,39,-41,39,-19,-23,-21,-22,-24,-4,-20,39,39,-25,]),'DATATYPE':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,31,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,84,102,108,112,113,114,116,120,123,125,126,128,131,146,147,151,152,154,155,156,157,159,161,162,165,168,169,170,171,172,173,174,176,178,179,180,181,183,189,190,191,192,193,],[40,40,-6,-8,-9,-10,-11,-12,-13,-17,-18,40,40,40,40,40,-5,-7,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-14,-15,40,40,40,-82,-46,40,40,40,40,-16,40,40,-40,-45,134,40,40,40,-42,40,150,40,-39,-26,134,40,40,40,40,40,-43,-44,150,40,40,40,40,40,40,-41,40,-19,-23,-21,-22,-24,-4,-20,40,40,-25,]),'RBRACE':([3,4,6,7,8,9,10,11,16,17,21,22,23,24,25,26,27,29,36,37,38,39,41,42,60,61,63,69,71,73,74,78,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,108,110,113,114,120,122,124,125,126,127,129,132,133,135,142,143,147,151,153,161,162,167,168,169,170,171,173,174,178,179,180,181,183,185,188,189,190,192,193,],[-3,-6,-8,-9,-10,-11,-12,-13,-17,-18,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-5,-7,-14,-15,-84,-82,-84,-60,-63,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-64,-65,-16,-37,-36,-73,-40,-45,140,-35,-81,-36,-42,144,-79,151,-27,-30,-38,160,-39,-26,-29,-43,-44,-28,178,179,180,181,183,-41,-19,-23,-21,-22,-24,189,-80,-4,-20,193,-25,]),'SEMI':([5,12,13,15,21,22,23,24,25,26,27,29,30,36,37,38,39,62,63,71,73,74,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,107,110,122,124,129,130,144,145,160,186,188,],[42,60,61,-84,-66,-67,-68,-69,-70,-71,-72,-74,78,-75,-76,-77,-78,102,-84,-84,-60,-63,113,114,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-64,-65,126,-73,-35,-81,-79,147,161,162,174,190,-80,]),'PLUS':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[43,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,43,-84,-60,-63,43,-47,-48,-49,-50,-51,-52,-53,43,43,43,43,43,43,43,43,43,43,43,43,43,-73,43,43,43,-35,-81,-79,43,43,43,43,-80,]),'MUL':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[45,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,45,-84,-60,-63,45,45,45,-49,-50,-51,-52,-53,45,45,45,45,45,45,45,45,45,45,45,45,45,-73,45,45,45,-35,-81,-79,45,45,45,45,-80,]),'DIVIDE':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[46,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,46,-84,-60,-63,46,46,46,-49,-50,-51,-52,-53,46,46,46,46,46,46,46,46,46,46,46,46,46,-73,46,46,46,-35,-81,-79,46,46,46,46,-80,]),'INTDIVIDE':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[47,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,47,-84,-60,-63,47,47,47,-49,-50,-51,-52,-53,47,47,47,47,47,47,47,47,47,47,47,47,47,-73,47,47,47,-35,-81,-79,47,47,47,47,-80,]),'MODULO':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[48,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,48,-84,-60,-63,48,48,48,-49,-50,-51,-52,-53,48,48,48,48,48,48,48,48,48,48,48,48,48,-73,48,48,48,-35,-81,-79,48,48,48,48,-80,]),'POW':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[49,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,49,-84,-60,-63,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-73,49,49,49,-35,-81,-79,49,49,49,49,-80,]),'LE':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[50,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,50,-84,-60,-63,50,-47,-48,-49,-50,-51,-52,-53,None,None,None,None,50,50,50,50,50,50,50,50,50,-73,50,50,50,-35,-81,-79,50,50,50,50,-80,]),'GE':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[51,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,51,-84,-60,-63,51,-47,-48,-49,-50,-51,-52,-53,None,None,None,None,51,51,51,51,51,51,51,51,51,-73,51,51,51,-35,-81,-79,51,51,51,51,-80,]),'LT':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[52,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,52,-84,-60,-63,52,-47,-48,-49,-50,-51,-52,-53,None,None,None,None,52,52,52,52,52,52,52,52,52,-73,52,52,52,-35,-81,-79,52,52,52,52,-80,]),'GT':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[53,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,53,-84,-60,-63,53,-47,-48,-49,-50,-51,-52,-53,None,None,None,None,53,53,53,53,53,53,53,53,53,-73,53,53,53,-35,-81,-79,53,53,53,53,-80,]),'EQ':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[54,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,54,-84,-60,-63,54,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,None,None,54,54,54,54,54,54,54,-73,54,54,54,-35,-81,-79,54,54,54,54,-80,]),'NE':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[55,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,55,-84,-60,-63,55,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,None,None,55,55,55,55,55,55,55,-73,55,55,55,-35,-81,-79,55,55,55,55,-80,]),'LAND':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[56,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,56,-84,-60,-63,56,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,None,56,-64,-65,56,56,56,-73,56,56,56,-35,-81,-79,56,56,56,56,-80,]),'LOR':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[57,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,57,-84,-60,-63,57,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,None,-64,-65,57,57,57,-73,57,57,57,-35,-81,-79,57,57,57,57,-80,]),'BAND':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[58,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,58,-84,-60,-63,58,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,58,58,None,58,58,58,58,-73,58,58,58,-35,-81,-79,58,58,58,58,-80,]),'BOR':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,117,119,121,122,124,129,130,142,145,182,188,],[59,-84,-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,59,-84,-60,-63,59,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,59,59,-64,None,59,59,59,-73,59,59,59,-35,-81,-79,59,59,59,59,-80,]),'LBRACKET':([15,28,40,71,72,163,],[65,75,-83,65,75,175,]),'EQUALS':([15,63,66,76,109,129,],[67,-84,106,112,128,146,]),'DOT':([15,],[68,]),'COLON':([15,],[69,]),'RPAREN':([21,22,23,24,25,26,27,29,36,37,38,39,63,64,70,71,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,110,117,118,119,121,122,124,129,131,142,148,149,166,177,182,188,],[-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,-36,110,-84,-60,-63,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-64,-65,122,-37,-73,136,138,139,141,-35,-81,-79,-31,-38,164,-32,-34,-33,186,-80,]),'COMMA':([21,22,23,24,25,26,27,29,36,37,38,39,63,64,71,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,108,110,122,124,125,127,129,131,132,133,135,142,143,148,149,153,166,167,177,188,189,],[-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,-36,-84,-60,-63,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-64,-65,123,-37,-36,-73,-35,-81,-36,123,-79,-31,152,-27,-30,-38,123,165,-32,-29,-34,-28,-33,-80,-4,]),'RBRACKET':([21,22,23,24,25,26,27,29,36,37,38,39,63,71,73,74,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,105,110,122,124,129,184,188,],[-66,-67,-68,-69,-70,-71,-72,-74,-75,-76,-77,-78,-84,-84,-60,-63,111,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-64,-65,124,-73,-35,-81,-79,188,-80,]),'error':([21,22,23,24,25,26,27,29,33,36,37,38,39,63,71,73,74,81,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,110,117,122,124,129,188,],[-66,-67,-68,-69,-70,-71,-72,-74,82,-75,-76,-77,-78,-84,-84,-60,-63,118,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-64,-65,-73,137,-35,-81,-79,-80,]),'LBRACE':([34,63,67,80,106,136,137,138,139,141,164,187,],[83,-84,108,116,125,154,155,156,157,159,176,191,]),'ELSE':([183,],[187,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'basic_block':([0,176,],[2,185,]),'stmt_list':([0,83,154,155,156,157,159,176,191,],[3,120,168,169,170,171,173,3,192,]),'statement':([0,3,83,120,154,155,156,157,159,168,169,170,171,173,176,191,192,],[4,41,4,41,4,4,4,4,4,41,41,41,41,41,4,4,41,]),'expr':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,84,108,112,120,123,125,128,154,155,156,157,159,168,169,170,171,172,173,176,191,192,],[5,5,70,73,74,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,117,119,5,121,104,130,5,142,104,145,5,5,5,5,5,5,5,5,5,182,5,5,5,5,]),'var_declaration':([0,3,83,120,154,155,156,157,159,168,169,170,171,173,176,191,192,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'return':([0,3,83,120,154,155,156,157,159,168,169,170,171,173,176,191,192,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'assign':([0,3,83,120,154,155,156,157,159,168,169,170,171,173,176,191,192,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'func_declaration':([0,3,83,116,120,152,154,155,156,157,159,168,169,170,171,173,176,191,192,],[9,9,9,135,9,135,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'struct_declaration':([0,3,83,120,154,155,156,157,159,168,169,170,171,173,176,191,192,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'while':([0,3,83,120,154,155,156,157,159,168,169,170,171,173,176,191,192,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'goto_mark':([0,3,83,120,154,155,156,157,159,168,169,170,171,173,176,191,192,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'if-else':([0,3,83,120,154,155,156,157,159,168,169,170,171,173,176,191,192,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'id':([0,3,15,18,19,20,28,30,32,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,79,81,82,83,84,108,111,112,120,123,125,128,154,155,156,157,159,168,169,170,171,172,173,176,191,192,],[21,21,66,21,21,21,76,21,80,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,115,21,21,21,21,21,129,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'int':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,84,108,112,120,123,125,128,154,155,156,157,159,168,169,170,171,172,173,176,191,192,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'double':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,84,108,112,120,123,125,128,154,155,156,157,159,168,169,170,171,172,173,176,191,192,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'bool':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,84,108,112,120,123,125,128,154,155,156,157,159,168,169,170,171,172,173,176,191,192,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'str':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,84,108,112,120,123,125,128,154,155,156,157,159,168,169,170,171,172,173,176,191,192,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'void':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,84,108,112,120,123,125,128,154,155,156,157,159,168,169,170,171,172,173,176,191,192,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'datatype':([0,3,18,19,20,30,31,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,84,108,112,120,123,125,128,146,154,155,156,157,159,168,169,170,171,172,173,176,191,192,],[28,28,72,72,72,72,79,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,28,72,72,72,28,72,72,72,163,28,28,28,28,28,28,28,28,28,72,28,28,28,28,]),'args':([64,108,125,],[103,127,143,]),'struct_params':([116,],[132,]),'struct_param':([116,152,],[133,167,]),'params':([131,],[148,]),'param':([131,165,],[149,177,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> <empty>','program',0,'p_program','doh_parser.py',34),
  ('program -> basic_block','program',1,'p_program','doh_parser.py',35),
  ('basic_block -> stmt_list','basic_block',1,'p_basic_block','doh_parser.py',43),
  ('func_declaration -> FUNCTION datatype id LPAREN params RPAREN LBRACE basic_block RBRACE','func_declaration',9,'p_func_declaration','doh_parser.py',48),
  ('stmt_list -> stmt_list statement','stmt_list',2,'p_stmt_list','doh_parser.py',53),
  ('stmt_list -> statement','stmt_list',1,'p_stmt_list','doh_parser.py',54),
  ('statement -> expr SEMI','statement',2,'p_stmt','doh_parser.py',63),
  ('statement -> var_declaration','statement',1,'p_stmt','doh_parser.py',64),
  ('statement -> return','statement',1,'p_stmt','doh_parser.py',65),
  ('statement -> assign','statement',1,'p_stmt','doh_parser.py',66),
  ('statement -> func_declaration','statement',1,'p_stmt','doh_parser.py',67),
  ('statement -> struct_declaration','statement',1,'p_stmt','doh_parser.py',68),
  ('statement -> while','statement',1,'p_stmt','doh_parser.py',69),
  ('statement -> BREAK SEMI','statement',2,'p_stmt','doh_parser.py',70),
  ('statement -> CONTINUE SEMI','statement',2,'p_stmt','doh_parser.py',71),
  ('statement -> GOTO ID SEMI','statement',3,'p_stmt','doh_parser.py',72),
  ('statement -> goto_mark','statement',1,'p_stmt','doh_parser.py',73),
  ('statement -> if-else','statement',1,'p_stmt','doh_parser.py',74),
  ('while -> WHILE LPAREN expr RPAREN LBRACE stmt_list RBRACE','while',7,'p_loops','doh_parser.py',88),
  ('while -> DO LBRACE stmt_list RBRACE WHILE LPAREN expr RPAREN SEMI','while',9,'p_loops','doh_parser.py',89),
  ('while -> WHILE LPAREN error RPAREN LBRACE stmt_list RBRACE','while',7,'p_loops_error','doh_parser.py',99),
  ('while -> WHILE error expr RPAREN LBRACE stmt_list RBRACE','while',7,'p_loops_error','doh_parser.py',100),
  ('while -> WHILE LPAREN expr error LBRACE stmt_list RBRACE','while',7,'p_loops_error','doh_parser.py',101),
  ('if-else -> IF LPAREN expr RPAREN LBRACE stmt_list RBRACE','if-else',7,'p_if_else','doh_parser.py',108),
  ('if-else -> IF LPAREN expr RPAREN LBRACE stmt_list RBRACE ELSE LBRACE stmt_list RBRACE','if-else',11,'p_if_else','doh_parser.py',109),
  ('struct_declaration -> STRUCTURE id LBRACE struct_params RBRACE','struct_declaration',5,'p_struct_declaration','doh_parser.py',119),
  ('struct_params -> struct_param','struct_params',1,'p_struct_params','doh_parser.py',126),
  ('struct_params -> struct_params COMMA struct_param','struct_params',3,'p_struct_params','doh_parser.py',127),
  ('struct_param -> DATATYPE ID','struct_param',2,'p_struct_param','doh_parser.py',137),
  ('struct_param -> func_declaration','struct_param',1,'p_struct_param','doh_parser.py',138),
  ('params -> <empty>','params',0,'p_params','doh_parser.py',147),
  ('params -> param','params',1,'p_params','doh_parser.py',148),
  ('params -> params COMMA param','params',3,'p_params','doh_parser.py',149),
  ('param -> DATATYPE ID','param',2,'p_param_declaration','doh_parser.py',159),
  ('expr -> ID LPAREN args RPAREN','expr',4,'p_func_call','doh_parser.py',164),
  ('args -> <empty>','args',0,'p_arguments','doh_parser.py',169),
  ('args -> expr','args',1,'p_arguments','doh_parser.py',170),
  ('args -> args COMMA expr','args',3,'p_arguments','doh_parser.py',171),
  ('var_declaration -> datatype id EQUALS expr SEMI','var_declaration',5,'p_var_declaration','doh_parser.py',183),
  ('var_declaration -> datatype id SEMI','var_declaration',3,'p_var_declaration','doh_parser.py',184),
  ('var_declaration -> ID id EQUALS LBRACE args RBRACE SEMI','var_declaration',7,'p_var_declaration','doh_parser.py',185),
  ('assign -> ID EQUALS expr SEMI','assign',4,'p_assign','doh_parser.py',197),
  ('assign -> ID EQUALS LBRACE args RBRACE SEMI','assign',6,'p_assign','doh_parser.py',198),
  ('assign -> ID DOT ID EQUALS expr SEMI','assign',6,'p_assign','doh_parser.py',199),
  ('return -> RETURN expr SEMI','return',3,'p_return','doh_parser.py',210),
  ('return -> RETURN SEMI','return',2,'p_return','doh_parser.py',211),
  ('expr -> expr PLUS expr','expr',3,'p_math_expressions','doh_parser.py',220),
  ('expr -> expr MINUS expr','expr',3,'p_math_expressions','doh_parser.py',221),
  ('expr -> expr MUL expr','expr',3,'p_math_expressions','doh_parser.py',222),
  ('expr -> expr DIVIDE expr','expr',3,'p_math_expressions','doh_parser.py',223),
  ('expr -> expr INTDIVIDE expr','expr',3,'p_math_expressions','doh_parser.py',224),
  ('expr -> expr MODULO expr','expr',3,'p_math_expressions','doh_parser.py',225),
  ('expr -> expr POW expr','expr',3,'p_math_expressions','doh_parser.py',226),
  ('expr -> expr LE expr','expr',3,'p_conditionals','doh_parser.py',247),
  ('expr -> expr GE expr','expr',3,'p_conditionals','doh_parser.py',248),
  ('expr -> expr LT expr','expr',3,'p_conditionals','doh_parser.py',249),
  ('expr -> expr GT expr','expr',3,'p_conditionals','doh_parser.py',250),
  ('expr -> expr EQ expr','expr',3,'p_conditionals','doh_parser.py',251),
  ('expr -> expr NE expr','expr',3,'p_conditionals','doh_parser.py',252),
  ('expr -> MINUS expr','expr',2,'p_logical_operation','doh_parser.py',268),
  ('expr -> expr LAND expr','expr',3,'p_logical_operation','doh_parser.py',269),
  ('expr -> expr LOR expr','expr',3,'p_logical_operation','doh_parser.py',270),
  ('expr -> LNOT expr','expr',2,'p_logical_operation','doh_parser.py',271),
  ('expr -> expr BAND expr','expr',3,'p_bitwise_operation','doh_parser.py',284),
  ('expr -> expr BOR expr','expr',3,'p_bitwise_operation','doh_parser.py',285),
  ('expr -> id','expr',1,'p_literals','doh_parser.py',294),
  ('expr -> int','expr',1,'p_literals','doh_parser.py',295),
  ('expr -> double','expr',1,'p_literals','doh_parser.py',296),
  ('expr -> bool','expr',1,'p_literals','doh_parser.py',297),
  ('expr -> str','expr',1,'p_literals','doh_parser.py',298),
  ('expr -> void','expr',1,'p_literals','doh_parser.py',299),
  ('expr -> NULL','expr',1,'p_literals','doh_parser.py',300),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_literals','doh_parser.py',301),
  ('int -> INTEGER','int',1,'p_const_int','doh_parser.py',309),
  ('double -> DOUBLE','double',1,'p_const_double','doh_parser.py',314),
  ('bool -> BOOL','bool',1,'p_const_bool','doh_parser.py',319),
  ('str -> STRING','str',1,'p_const_string','doh_parser.py',324),
  ('void -> VOID','void',1,'p_void','doh_parser.py',329),
  ('expr -> datatype LBRACKET RBRACKET id','expr',4,'p_array_init','doh_parser.py',335),
  ('expr -> datatype LBRACKET RBRACKET id EQUALS datatype LBRACKET INTEGER RBRACKET','expr',9,'p_array_init','doh_parser.py',336),
  ('expr -> ID LBRACKET expr RBRACKET','expr',4,'p_index','doh_parser.py',345),
  ('goto_mark -> ID COLON','goto_mark',2,'p_goto_mark','doh_parser.py',350),
  ('datatype -> DATATYPE','datatype',1,'p_datatype','doh_parser.py',355),
  ('id -> ID','id',1,'p_id','doh_parser.py',360),
]
