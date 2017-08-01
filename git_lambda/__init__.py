import os
import tarfile


def setup(target_directory='/tmp/git',
          update_env=True):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tar = tarfile.open(os.path.join(dir_path, 'git-2.4.3.tar'))
    tar.extractall(target_directory)

    bin_path = os.path.join(target_directory, 'usr', 'bin')

    template_dir = os.path.join(
        target_directory,
        'usr',
        'shate',
        'git-core',
        'templates'
    )

    exec_path = os.path.join(
        target_directory,
        'libexec',
        'git-core'
    )

    if update_env:
        os.environ['PATH'] += ':' + bin_path
        os.environ['GIT_TEMPLATE_DIR'] = template_dir
        os.environ['GIT_EXEC_PATH'] = exec_path
