from project import actions
import os

def test_clone_empty_url_repository():
    assert actions.clone_repo('') == False

def test_clone_wrong_url_repository():
    assert actions.clone_repo('https://thisisabadrepourl.git') == False

def test_naive_check_repo_validity_empty():
    from shutil import rmtree
    rmtree('tests/unit/empty_folder', ignore_errors=True)
    os.makedirs('tests/unit/empty_folder')
    assert actions.naive_check_repo_validity('tests/unit/empty_folder') == False

def test_naive_check_repo_validity_with_file():
    assert actions.naive_check_repo_validity('tests/unit/folder_with_cmakelists') == True

def test_build_repo_cmake_example_project():
    cwd = os.getcwd()
    source_folder = os.path.join(cwd, 'tests/unit/cmake_example_project')
    build_folder = os.path.join(cwd, 'tests/unit/build')
    assert actions.build_repo(source_folder, build_folder) == True

def test_build_repo_cmake_wrong_example_project_():
    cwd = os.getcwd()
    source_folder = os.path.join(cwd, 'tests/unit/cmake_example_wrong_project')
    build_folder = os.path.join(cwd, 'tests/unit/build')
    assert actions.build_repo(source_folder, build_folder) == False

def test_naive_check_empty_build_folder():
    assert actions.naive_check_build_folder('tests/unit/empty_folder') == False

def test_naive_check_nonempty_build_folder():
    assert actions.naive_check_build_folder('tests/unit/cmake_example_project') == True
