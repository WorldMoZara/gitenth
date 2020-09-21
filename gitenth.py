#!/usr/bin/env python3
# GiTenth
# a simple tool to manage git repository.

# Package from Python
import os

# Package from Python Package Index

# Package from GiTenth
import i18n, u_box

LOCALE = "zh_cn"

def give_error(errtype: str, *args):
    box = u_box.uMsgBox(i18n.MESSAGE_TEXT[LOCALE]["error"],
                        i18n.MESSAGE_TEXT[LOCALE][errtype] % args,
                        i18n.CHOICE_TEXT[LOCALE]["ok"])
    box.show()

def git_init():
    pass

def git_clone():
    pass

def g10_exit(*args, **kwargs):
    exit()

EXECSTACK = {
    "git-init": git_init,
    "git-clone": git_clone
}

def main():
    while True:
        HOMEPG_LOCALE_TEXT = i18n.HOMEPG_TEXT[LOCALE]
        homepage = u_box.uListBox("GiTenth", list(HOMEPG_LOCALE_TEXT.values()))
        homepage.show()
        h_result = homepage.result
        if h_result == HOMEPG_LOCALE_TEXT["exit"]:
            exit()
        INFUNC = False
        for key, value in HOMEPG_LOCALE_TEXT.items():
            if h_result == value:
                INFUNC = True
                try:
                    EXECSTACK[key]()
                except KeyError:
                    give_error("function-wip", h_result)
                break
        else:
            if not INFUNC:
                give_error("function-not-exist", h_result)

if __name__ == "__main__":
    # from optparse import OptionParser
    # parser = OptionParser()
    # parser.add_option("")
    # main(*parser.parse_args())
    main()

