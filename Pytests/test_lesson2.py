import subprocess
from HM1_2 import find_subprocess
import zlib

tst = "/home/ubuntu/tst"
out = "/home/ubuntu/out"
folder1 = "/home/ubuntu/folder1"

def crc32(cmd):
    with open(cmd, 'rb') as g:
        hash = 0
        while True:
            s = g.read(65536)
            if not s:
                break
            hash = zlib.crc32(s, hash)
        return "%08X" % (hash & 0xFFFFFFFF)


def test_step1():
    res1 = find_subprocess(f"cd {tst}; 7z a {out}/arx2", "Everything is Ok")
    res2 = find_subprocess(f"ls {out}", "arx27z")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    res1 = find_subprocess(f"cd {out}; 7z e arx2.7z -o{folder1} -y", "Everything is Ok")
    res2 = find_subprocess(f"ls {folder1}", "testtxt")
    assert res1 and res2, "test2 FAIL"


def test_step3():
    assert find_subprocess(f"cd {out}; 7z l out.7z", "1 files")



def test_step4():
    assert find_subprocess(f"cd {out}; 7z t arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    assert find_subprocess(f"cd {out}; 7z d arx2.7z", "Everything is Ok"), "test5 FAIL"


def test_step6():
    assert find_subprocess(f"cd {out}; 7z u arx2.7z", "Everything is Ok"), "test6 FAIL"

def test_step7():
    assert find_subprocess(f"cd {out} && 7z x /home/ubuntu/out/out1/out.7z", "Everything is Ok")

def test_step8():
    res1 = crc32(f"{out}/out.7z").lower()
    assert find_subprocess(f"crc32 {out}/out.7z", res1), "test8 FAIL"
