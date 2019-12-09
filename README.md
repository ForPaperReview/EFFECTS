# EFFECTS
Automated verification tool for temporal properties

To Compile:

ocamllex lexer.mll
menhir parser.mly
ocamlc -c ast.mli
ocamlc -c parser.mli
ocamlc -c parser.ml
ocamlc -c lexer.ml
ocamlc -c Askz3.ml
ocamlc -c Rewriting.ml
ocamlc -o trs parser.cmo lexer.cmo Askz3.cmo Rewriting.cmo

Example:
./trs src/effect/ex1.ee src/effect/output.txt > src/effect/output.txt 2>&1
