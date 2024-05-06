import os, sys
if __name__=='__main__':
    with os.scandir('.') as files:
        for i, file in enumerate(sorted([f for f in files if f.is_file() and f.name.startswith('test') and f.name[-4:].lower()=='.txt'], key = lambda x: x.name)):
            print(i,file.name)
            new_name = str(i + 1)+'.txt'

            print(f"rename {file.name} to {new_name} ", file=sys.stderr)

            os.rename(file, new_name)

            