# git_lambda
🐙 Git binary package for the Python AWS Lambda runtime

`git_lambda` includes a tar archive of git binaries for use in AWS Lambda. Calling `git_lambda.setup()` unzips the binaries, puts them in the right spot, and updates the current process' `PATH` so that `git` can be called via a [subprocess](https://docs.python.org/3.6/library/subprocess.html)

## Usage
```python
import git_lambda

git_lambda.setup()

# git is now available in your $PATH for calling via a subprocess!
```

## Attribution

Package inspired by and binary provided [pimterry/lambda-git](https://github.com/pimterry/lambda-git)
