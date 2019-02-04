# Deployment and stable release

The last step is the deployment and creating a stable release.

Here we explain how you can package your module in a way that ImJoy can install
it as a requirement via the `pip` command

### Create a pip package

#### Setup
In order to create a package that can be installed via the `pip` command, you have

1. Add an empty file **`__init__.py`** into the `pkgcode` folder.
2. Specify a `setup.py` file - a simple python file in the root folder
that specifies our package.

!!! note "<a href="https://github.com/muellerflorian/ImJoy-demo-project/blob/master/setup.py" target="_blank"> **setup.py**</a>"
      ```python
      from setuptools import setup, find_packages

      requirements = ['numpy']

      setup(
            name='pkgcode',
            version='0.1.0',
            description='What is going on.',
            url='http://whatever',
            author='Florian MUELLER',
            author_email='muellerf.research@gmail.com',
            license='MIT',
            packages=find_packages(),
            include_package_data=True,
            install_requires=requirements,
            zip_safe=False)
      ```

The important fields to adjust for your own package in `setup.py` are:

-   `requirements`: contains all requirements of your package
-   `name`: this has to be the name of the folder containing your modules, e.g. `pkgcode` for our demo project.
     This is not necessarily the name of your package.
-   `version`: version of your package. You can specify what you want,
    <a href="https://semver.org/" target="_blank"> semantic versioning</a>
     is recommended.
-   `description`, `url`, `author`, `author_email`: self-explanatory fields.
-   `licence`: licence type of your repository. If you are not sure which license you should use , check out
     <a href="https://choosealicense.com" target="_blank"> choosealicense.com</a>.


#### Publish and test

You can then push you changes to **GitHub**. Please note that it is not necessary
that you up-load your package to the Package Index.

In order to **test your module**, you can use the `pip` terminal command,
which should result in a successful install as indicated in the `Output` tab.

!!! note "Test pip module"

    ```bash tab="Pip install"
    pip install git+https://github.com/muellerflorian/ImJoy-demo-project#egg=ImJoy-demo-project
    ```

    ```bash tab="Output"
    Successfully built imjoydemoproject
    Installing collected packages: imjoydemoproject
    Successfully installed imjoydemoproject-0.1.0
    ```

You can then test if the module works by launching Python in the terminal with
`python`. In the Python terminal, you can call the function that calculates the sine function:

```python
from imjoydemoproject import outils
outils.calc_sine(50)
```

More information about pip packaging can be found
<a href="https://packaging.python.org/tutorials/packaging-projects/" target="_blank">**here**</a>.

### Add requirement to ImJoy plugin

Now you can specify this package as a requirement in your ImJoy plugin, which will
be automatically installed.

For our example, this requirement will only be considered for the `stable` release,
i.e. for the tag `stable`

!!! note "<a href="https://github.com/muellerflorian/ImJoy-demo-project/blob/master/imjoy-plugins/Sine%20Calculator.imjoy.html#L24" target="_blank"> **Sine Calculator.imjoy.html**</a>"
    ```json
    "requirements": { "stable": ["pip:git+https://github.com/muellerflorian/ImJoy-demo-project@1a6bce14eb512e1414de2c7cc9eec9da1fee8ce7#egg=ImJoy-demo-project"]}
    ```

The general syntax of such a requirement is

```json
"requirements": ["pip:git+https://github.com/{username}/{reponame}@{tagname}#egg={reponame}"]
```
 with the following fields

* `username`: name of the GitHub account.
* `reponame`: name of the GitHub repository.
* `tagname`: allows passing of tag. This can be a commit hash tag, a Git tag,
   or a GitHub release, or a commit hash tag. This provides precise control **which version of the repository is installed**.
   This is especially important when update your repository.
* `eggname`: this is usually the name of your repository. This is recommended for an install of a Git repository,
   and tells pip what to call the repository for dependency checks.

Please note that once a package is installed, it will not be upgraded unless you specify a
new tag specified after the `@` symbol.


## Import module from GitHub
We can now load the module for the stable release from GitHub.
Please note that the alphanumeric characters after the `@` specify a certain commit.

!!! note "<a href="https://github.com/muellerflorian/ImJoy-demo-project/blob/master/imjoy-plugins/Sine%20Calculator.imjoy.html#L39" target="_blank"> **Sine Calculator.imjoy.html**</a>"
    ```python
    elif 'stable' == api.TAG:
        from imjoydemoproject import outils
    ```

You can now change the `tag` in the toolbar of the menu, and save the plugin.
Now, our pip module will be loaded.

More information about installing GitHub packages in ImJoy can be found
<a href="https://imjoy.io/docs/#/development?id=install-package-from-github" target="_blank">here</a>.
