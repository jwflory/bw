How to contribute
=================

This page provides guidelines on how to work on and contribute to this project.
Following all steps here improve your chances of getting changes merged upstream.


## Set up a development environment

bye_wiki uses [Pipenv][1] to manage dependencies.
See Pipenv documentation for [how to install Pipenv][2].

Once you have Pipenv installed, run the following commands in a Linux shell / terminal:

```sh
git clone https://github.com/jwflory/bw.git
cd bw/
pipenv shell
pipenv sync --dev
```

You should be able to type `bw --help` after running `pipenv sync`.


## How to submit contributions

For now, the bar is low for new contributions since this is a hobby project.
But if you want to work on this or improve it, I am happy to accept contributions and package them in PyPI.
Please try to explain the purpose/reasoning by any changes you propose, in order to help me understand.

[1]: https://pipenv.pypa.io/
[2]: https://pipenv.pypa.io/en/latest/install/#installing-pipenv
