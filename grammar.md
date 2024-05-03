Grammar Rules
-------------

The rules for this interpreter are highlighted here in BNF syntax.

<L> :: = <assignment>

<assignment> ::= VARIABLE SETTO <expression>
               | VARIABLE SETTO <flow>

<flow> ::= VARIABLE CONNECT <flow_functions>

<flow_functions> ::= <flow_function_call> CONNECT <flow_functions>
                    | <flow_function_call>

<flow_function_call> ::= VARIABLE LPAREN <params> RPAREN

<expression> ::= <expression> PLUS <term>
               | <expression> MINUS <term>
               | <term>
               | <string>
               | <expression> TIMES <exponent>
               | <expression> DIVIDE <exponent>
               | <expression> GT <expression>
               | <expression> LT <expression>
               | <expression> GTEQ <expression>
               | <expression> LTEQ <expression>
               | <expression> EQ <expression>
               | <expression> UQ <expression>
               | <expression> AND <expression>
               | <expression> OR <expression>
               | NOT <expression>
               | IF LPAREN <expression> RPAREN THEN <expression> ELSE <expression>

<term> ::= <term> TIMES <exponent>
          | <term> DIVIDE <exponent>
          | <exponent>

<exponent> ::= <factor> EXP <factor>
             | <factor>

<factor> ::= NUMBER
           | VARIABLE
           | <function_call>

<function_call> ::= VARIABLE LPAREN RPAREN
                  | VARIABLE LPAREN <params> RPAREN

<params> ::= <params> COMMA <expression>
            | <expression>

<string> ::= STRING

