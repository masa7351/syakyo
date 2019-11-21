rewriteFiles=('*.js', '*.jsx')

def copyFiles(copyPath, destinationPath):
    from shutil import copytree, ignore_patterns
    copytree(copyPath, destinationPath, ignore=ignore_patterns('node_modules', '*.gitignore', '*.git', 'README.md', '.vscode'))

def removeContents(destinationPath):
    from pathlib import Path
    from os.path import join
    p = Path(destinationPath)
    # glob multiple filetypes
    # https://stackoverflow.com/questions/4568580/python-glob-multiple-filetypes
    files = []
    for ext in rewriteFiles:
        files.extend(p.glob(join("**", ext)))
    # rewrite empty for mutch files
    for file in files:
        file.write_text('')

if __name__ == "__main__":
    import sys
    copyFiles(sys.argv[1], sys.argv[2])
    removeContents(sys.argv[2])