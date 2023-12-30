#!/usr/bin/python3
import subprocess
import re


paths_dict = {"ast_code_samples/basic.c": "ast_dumps/basic_c_ast.txt",
              "ast_code_samples/basic.cpp": "ast_dumps/basic_cpp_ast.txt",
              "ast_code_samples/cppsyntax.cpp": "ast_dumps/cppsyntax_ast.txt"}


def get_clean_ast(source_file_path: str) -> str:
    command = ["clang", "-Xclang", "-ast-dump",
               "-fsyntax-only", source_file_path]
    result = subprocess.run(command, capture_output=True, text=True)
    # Remove ANSI escape codes
    clean_output = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)
    return clean_output


for k, v in paths_dict.items():
    with open(v, 'w') as file:
        file.write(get_clean_ast(k))
