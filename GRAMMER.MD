# Grammer Rules for Parser

**factor** : 
- INT | FLOAT
- (PLUS | MINUS) factor
- LEFTPAREN expr RPAREN

**term**:
- factor((MULT|DIV) factor)*

**expr**:
- term((PLUS|MINUS) term)*