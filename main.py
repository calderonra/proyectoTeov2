import sys
import ply.yacc as yacc
from parser_yacc import Cparser
#from TypeChecker import TypeChecker


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "codigo.c"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    Cparser = Cparser()
    parser = yacc.yacc(module=Cparser)
    text = file.read()
    ast = parser.parse(text, lexer=Cparser.scanner)
 #   typeChecker = TypeChecker()
#  typeChecker.visit(ast, None)   # or alternatively ast.accept(typeChecker)