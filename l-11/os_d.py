import os


def demo_os_env():
    print(os.name)
    print(os.environ)
    db_conf = os.environ.get("DB_HOST"), os.environ.get("DB_PORT")
    print(db_conf)
    print(os.environ.get("key"))


def demo_os_dirs():
    cwd = os.getcwd()
    print(cwd)

    # "C://"
    # "/"
    subdir = os.path.join(cwd, "subdir")
    print("subdir: ", subdir)

    if os.path.isdir(subdir):
        print("subdir exist")
    else:
        os.mkdir(subdir)
        print(subdir)

    print("before: ", os.getcwd())
    os.chdir(subdir)
    print("after: ", os.getcwd())


def demo_walk():
    # for item in os.walk("."):
    #     print(item)
    # for root, dirs, files in os.walk("."):
    #     print(root)
    #     print(dirs)
    #     print(files)
    for root, dirs, files in os.walk(".", topdown=False):
        print("-*", root)
        for dir_ in dirs:
            print("--", dir_)
        for filename in files:
            print("---", filename)


def demo_path_parts():
    cwd = os.getcwd()
    print("cwd:", cwd)
    print("current base name:", os.path.basename(cwd))
    print("current dir name:", os.path.dirname(cwd))
    file = os.path.join(cwd, "os_d.py")
    print("file:", file)
    print("file name", os.path.basename(file))
    print("dir", os.path.dirname(file))
    print("is it a file?", os.path.isfile(file))
    print(os.path.split(file))
    print(os.path.split(cwd)[-1])


if __name__ == "__main__":
    # demo_os_env()
    # demo_os_dirs()
    # demo_walk()
    demo_path_parts()
