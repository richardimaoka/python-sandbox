When Pylance in vscode complains that `(module) sqlalchemy Import "sqlalchemy" could not be resolved from sourcePylancereportMissingModuleSource`
https://github.com/microsoft/pylance-release/issues/52#issuecomment-653745462

> Pylance doesn't know which search paths will be used at the time you execute your Python code. You need to tell it. By default, Pylance will assume that the search paths will include the root of the workspace you open. It also automatically adds a subdirectory called "src" if it's present, since it's common practice to place your code within a subdirectory of that name. Any other subdirectories that should be included in the search path must be specified using the "python.analysis.extraPaths" setting.

so this worked! :

```
{
  "python.pythonPath": "/home/richardimaoka/.pyenv/shims/python",
  "python.analysis.extraPaths": [
    "lib/python3.9/site-packages"
  ]
}
```