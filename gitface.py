# GiTenth gitface

import os

def check_git_exist(path=None):
    if path == None:
        path = os.getcwd()
    if os.path.exists(os.path.join(path, ".git")):
        status = os.system("cd %s%sgit status >%s" % (path, os.linesep,
                                                      os.devnull))
        if status == 0:
            return True
    return False

def view_git_status(path=None):
    if not check_git_exist(path):
        raise Exception("no .git directory found.")
    if path == None:
        path = os.getcwd()
    stat_cmd = "cd %s%sgit status" % (path, os.linesep)
    status = os.popen(stat_cmd).read()
    spl_msg = [EL.split(" ") for EL in status.split("\n") if not \
                    (EL == "" or "(use" in EL)]
    print(spl_msg)
    unstaged, untracked = False, False
    for line in spl_msg[1:]:
        if not unstaged:
            if "not" in line and "staged" in line:
                unstaged = True
                continue
        if not untracked and line[0] == "Untracked":
            untracked = True
            continue
    result = {
        "branch": spl_msg[0][2],
        "unstaged": unstaged,
        "untracked": untracked
    }
    return result

