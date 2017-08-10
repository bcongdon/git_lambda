import os
import tarfile


def setup(target_directory='/tmp/git',
          update_env=True):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tar = tarfile.open(os.path.join(dir_path, 'git-2.14.0.tar.gz'))
    tar.extractall(target_directory)
    git_path = os.path.join(target_directory, 'git')

    bin_path = os.path.join(git_path, 'bin')

    template_dir = os.path.join(
        git_path,
        'share',
        'git-core',
        'templates'
    )

    exec_path = os.path.join(
        git_path,
        'libexec',
        'git-core'
    )

    if update_env:
        os.environ['PATH'] = bin_path + ':' + os.environ['PATH']
        os.environ['GIT_TEMPLATE_DIR'] = template_dir
        os.environ['GIT_EXEC_PATH'] = exec_path
