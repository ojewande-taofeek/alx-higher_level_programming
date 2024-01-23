#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_files = dir(hidden_4)
    for name in all_files:
        if name.startswith("__"):
            pass
        else:
            print(name)
