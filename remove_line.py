import re
import os
import shutil
from log_color import log,LogLevel

def get_permissions(path):
    init_path = os.path.expanduser(path)
    if os.access(init_path, os.F_OK):
        log("\nGiven file path is exist.",LogLevel.INFO)
    if os.access(init_path, os.R_OK):
        log("\nFile is accessible to read",LogLevel.DEBUG)
    if os.access(init_path, os.W_OK):
        log("\nFile is accessible to write",LogLevel.PASS)
    if os.access(init_path, os.X_OK):
        log("\nFile is accessible to execute",LogLevel.WARN)


def copy_file(source_path = None,target_path = "/Users/magu/bakfile/"):
    try:
        init_source_path ,init_target_path = os.path.expanduser(source_path),os.path.expanduser(target_path)
        if os.path.isfile(init_source_path):
            if os.path.isdir(init_target_path):
                shutil.copy(init_source_path,init_target_path)
                log("\nfile copied successfully !!",LogLevel.PASS)
                return True
            log("dir path is not exist !!",LogLevel.DEBUG)
            return False
        log("file path is not exist !!",LogLevel.DEBUG)
        return False
    except Exception as error:
        log(error,LogLevel.DEBUG)
        return False
    

def get_line_number(source_path):
    count = -1
    file = open(os.path.expanduser(source_path),'rU')
    for count,line in enumerate(file):
        pass
    file.close()
    count += 1
    return count


def remove_line(keyword,source_path):
    init_source_path = os.path.expanduser(source_path)
    if isinstance(keyword,str):
        if os.path.isfile(init_source_path):
            copy_file(source_path=init_source_path)
            log(f"file with the name <{init_source_path}> is backed up",LogLevel.PASS)
            counter = 0
            with open(init_source_path,"r") as f:
                lines = f.readlines()
                #print(lines)
            with open(init_source_path,"w",encoding="utf-8") as f_w:
                for line in lines:
                    if keyword in line:
                        counter += 1
                        log(f"\n The line with the content \n<{line}> \nhas been deleted",LogLevel.INFO)
                        continue
                    f_w.write(line)
            f_w.close()
            log(f"total of {counter} lines were deleted this time",LogLevel.PASS)
        else:
            log(f"\nfile path <{init_source_path}> is not exist !!",LogLevel.DEBUG)
            return False
    else:
        log("\nkeyword must be string",LogLevel.DEBUG)
    return False
                
remove_line("https://cn.pornhub.com","~/.zsh_history")