import cx_Freeze

executables = [cx_Freeze.Executable('main.py', base="Win32GUI")]

cx_Freeze.setup(
    name = "FlappyBird",
    options = {
        "build_exe" : {"packages" : ["pygame"], "include_files": ["assets"]}},
        executables = executables    
)
