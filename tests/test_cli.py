import subprocess
import json
import os
import sys

sys.path.insert(0,os.path.abspath(os.path.join(__file__, '..', '..')))

def run(args):
    cmd = ['python','main.py'] + args
    result = subprocess.run(cmd,capture_output=True,text=True)
    return result


def test_file_txt(tmp_path,monkeypatch):
    src = os.path.join('examples','puzzle.txt')
    dst = tmp_path/'p.txt'
    import shutil;shutil.copy(src,dst)
    res = run(['--file',str(dst)])
    assert 'Initial board:' in res.stdout


def test_file_json(tmp_path):
    src = os.path.join('examples','puzzle.json')
    dst = tmp_path/'p.json'
    import shutil;shutil.copy(src,dst)
    res = run(['--file',str(dst),'--no-visual'])
    assert 'Solved board:' in res.stdout
