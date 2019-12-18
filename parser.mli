
(* The type of tokens. *)

type token = 
  | VOIDT
  | VAR of (string)
  | UNDERLINE
  | TRUEE of (bool)
  | TRUE
  | STRING of (string)
  | SIMI
  | SHARP
  | RSPEC
  | RPAR
  | REQUIRE
  | RBRACK
  | POWER
  | PLUS
  | OMEGA
  | NEGATION
  | MINUS
  | LTEQ
  | LT
  | LSPEC
  | LPAR
  | LBRACK
  | KLEENE
  | INTT
  | INTE of (int)
  | INCLUDE
  | IF
  | GTEQ
  | GT
  | FALSEE of (bool)
  | FALSE
  | EVENTKEY
  | EVENT of (string)
  | EQEQ
  | EQ
  | EOF
  | ENTIL
  | ENSURE
  | EMPTY
  | ELSE
  | DISJ
  | CONJ
  | CONCAT
  | COMMA
  | CHOICE
  | BOOLT

(* This exception is raised by the monolithic API functions. *)

exception Error

(* The monolithic API. *)

val prog: (Lexing.lexbuf -> token) -> Lexing.lexbuf -> (Ast.program)

val ee: (Lexing.lexbuf -> token) -> Lexing.lexbuf -> (Ast.entilment)
