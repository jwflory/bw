#!/usr/bin/python3

import argparse
import requests
import subprocess

from bye_wiki import __version__


WIKI_API_QUERY = "/api.php?action=query&format=json&prop=revisions" \
                 + "&rvprop=content&titles="


# TODO: Add support for specific revisions (a.k.a. oldid)
def get_mediawiki_content(insecure: bool, url: str, title: str) -> dict:
    """Return raw MediaWiki text from a wiki page title/name."""
    prefix = ""
    if insecure:
        prefix = "http://"
    else:
        prefix = "https://"
    query_url = prefix + url + WIKI_API_QUERY + title
    return requests.get(query_url).json()["query"]["pages"]


def clean_request_data(payload) -> str:
    """Clean up request made to MediaWiki API to return raw MediaWiki text."""
    page_id = list(payload.keys())[0]
    return payload[page_id]["revisions"][0]["*"]


def convert_mediawiki_to_markdown(mw_content: str, atx_off: bool) -> str:
    """Use pandoc via subprocess to convert temp. file to Markdown raw text."""
    pandoc_str = ["pandoc", "--from", "mediawiki", "--to", "markdown"]
    if atx_off is False:
        pandoc_str.append("--markdown-headings=atx")

    mediawiki_doc = subprocess.Popen(
        ("echo", mw_content),
        stdout=subprocess.PIPE,
    )
    return str(
        subprocess.check_output(pandoc_str, stdin=mediawiki_doc.stdout),
        "utf-8",
    )


def save_file(out_path: str, markdown_doc: str):
    """Save Markdown text to specified file path."""
    with open(out_path, "w") as file:
        file.write(str(markdown_doc))


def main():
    # Create main parser and subparser
    parser = argparse.ArgumentParser(
        description="Convert MediaWiki pages to Markdown."
    )

    parser.add_argument(
        "--atx-off",
        default=False,
        help="(Markdown only) Do not convert with Pandoc --markdown-headings=atx flag",
        action="store_true",
    )
    parser.add_argument(
        "-i",
        "--insecure",
        default=False,
        help="Use for http:// MediaWiki sites only (defaults to https://)",
        action="store_true",
    )
    parser.add_argument(
        "-u",
        "--url",
        default="en.wikipedia.org/w",
        help="Base URL for MediaWiki site (default: en.wikipedia.org/w)",
        metavar="URL",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--out",
        default="exported_markdown.txt",
        help="Path to saved data file",
        metavar="FILE",
        type=str,
    )
    parser.add_argument(
        "-t",
        "--title",
        help="Human-readable name of wiki page for project base",
        metavar="WIKI_PAGE_NAME",
        required=True,
        type=str,
    )
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__
    )
    args = parser.parse_args()

    raw_mw_content = get_mediawiki_content(args.insecure, args.url, args.title)
    mw_content = clean_request_data(raw_mw_content)
    md_doc = convert_mediawiki_to_markdown(mw_content, args.atx_off)
    save_file(args.out, md_doc)


if __name__ == "__main__":
    main()
