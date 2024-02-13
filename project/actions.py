import zipfile
import io
import pathlib
import subprocess
import os
import shutil

# from flask import current_app as app

def _run_subprocess(args):
    try:
        process = subprocess.run(args, capture_output=True, check=True)
    except subprocess.CalledProcessError:
        raise Exception('Error CalledProcessError')
    if process.returncode != 0:
        raise Exception('Error calling subprocess')

def clone_repo(url, destination_folder=''):
    if len(url) == 0:
        return False
    if len(destination_folder):
        shutil.rmtree(destination_folder, ignore_errors=True)
    try:
        # Clone the repository into source folder
        _run_subprocess(["git", "clone", url, destination_folder])
    except:
        return False
    return True

def naive_check_repo_validity(path):
    return os.path.exists(os.path.join(path, 'CMakeLists.txt'))

def build_repo(path, build_folder='build'):
    # Create the build folder in the current path and build the project
    cwd = os.getcwd()
    shutil.rmtree(build_folder, ignore_errors=True)
    os.makedirs(build_folder)
    os.chdir(build_folder)
    try:
        _run_subprocess(["cmake", path])
        _run_subprocess(["cmake", "--build", "."])
    except:
        os.chdir(cwd)
        return False
    os.chdir(cwd)
    return True

def naive_check_build_folder(path):
    if not os.listdir(path):
        return False
    return True

def create_zip(path):
    cwd = os.getcwd()
    os.chdir(path)
    base_path = pathlib.Path('.')
    data = io.BytesIO()
    with zipfile.ZipFile(data, mode='w') as z:
        for f_name in base_path.rglob('*'):
            z.write(f_name)
    data.seek(0)
    os.chdir(cwd)
    return data
