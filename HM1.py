import subprocess


def find_subprocess(path: str, text: str):
    result = subprocess.run(path, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    lst = result.stdout.split("\n")
    if result.returncode == 0:
        if text in lst:
            return True
        else:
            return False
    else:
        return False


print(find_subprocess("cat /etc/os-release", 'VERSION_ID="22.04"'))
