bye_wiki (bw)
=============

[![License: BSD 3-Clause License][1]][2]

Say goodbye to your wikis!
Python command-line wrapper to convert MediaWiki pages to other formats with `pandoc`


## About

bye_wiki (`bw`) is a Python command-line script to convert MediaWiki pages into other formats like AsciiDoc and Markdown.

This makes it easier to migrate documentation and wiki pages from a MediaWiki server to somewhere else.
Regardless of whatever "somewhere else" means for you, this tool provides a basic conversion for you to work with the information from a new format.
bye_wiki is more or less a fancy wrapper for `requests` and `pandoc`.


## How to use

**NOTE**:
You must already have [pandoc][3] installed on your system for this script to work!

Once you have `pandoc`, the easiest way to get started with bye_wiki is to install from PyPI:

```sh
pip install --user bye-wiki
```

The CLI `--help` menu provides more detailed information about how to use bye_wiki.
Some examples are below:

### Example 1

Convert _El Ten Eleven_ Wikipedia page to a Markdown document.

```sh
bw --title "El Ten Eleven" --out ~/ete.md
```

### Example 2

Convert _Fedora_Linux_38_Release_Party_Schedule_ from the [Fedora Project][4] MediaWiki to an AsciiDoc document.

```sh
bw --url fedoraproject.org/w --format asciidoc --title "Fedora_Linux_38_Release_Party_Schedule" --out licensing.adoc
```

### Example 3

Convert _MusicBrainz Principles_ from the [MusicBrainz][5] MediaWiki to a Markdown document, with the `--markdown-headings=atx` flag excluded from the `pandoc` command:

```sh
bw --url wiki.musicbrainz.org --title MusicBrainz_Principles --out mb-principles.md --atx-off
```

_Hint_:
If you are not sure whether you want `--atx-off` or not, you do not.
ATX is the more popular format for Markdown documents, but some writers may prefer to not have ATX-style headers.


## How to contribute

See [CONTRIBUTING.md][6].


## Legal

Licensed under [BSD 3-Clause License][2].

[1]: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
[2]: https://opensource.org/licenses/BSD-3-Clause "BSD-3-Clause License - opensource.org"
[3]: https://pandoc.org/
[4]: https://getfedora.org
[5]: https://musicbrainz.org
[6]: https://github.com/jwflory/bw/blob/main/.github/CONTRIBUTING.md "How to contribute to the project"
