#!/usr/bin/env python3
from shutil import which
from pathlib import Path

import os
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from academic.import_bibtex import parse_bibtex_entry, slugify
from academic.editFM import EditableFM

_ROOT = os.path.dirname(__file__)

def parse_conf():
    conf_bib = os.path.join(os.path.abspath(_ROOT), '../assets/pubs/conf.bib')
    print(conf_bib)
    assert(os.path.exists(conf_bib))

    confs = {}
    parser = BibTexParser(common_strings=True)
    bib_database =  bibtexparser.load(open(conf_bib), parser)
    for entry in bib_database.entries:
        id = entry['ID']
        del entry['ID']
        confs[id] = entry
    return confs

def read_bib():
    confs = parse_conf()

    pub_dir = "publication"
    parser = BibTexParser(common_strings=True)
    pub_bib = os.path.join(os.path.abspath(_ROOT), '../assets/pubs/pub.bib')
    bib_database = bibtexparser.load(open(pub_bib), parser)

    for i, entry in enumerate(bib_database.entries):
        if 'crossref' in entry:
            title = entry['title']
            conf = confs[entry['crossref']]
            entry.update(conf)
            entry['title'] = title
            del entry['crossref']

        url = entry.get('url')
        if url:
            del entry['url']

        parse_bibtex_entry(entry)

        bundle_path = f"content/{pub_dir}/{slugify(entry['ID'])}"
        markdown_path = os.path.join(bundle_path, "index.md")
        page = EditableFM(Path(bundle_path))
        page.load(Path("index.md"))

        static_dir = os.path.join(_ROOT, '../static')
        resource_dir = os.path.join(static_dir, f"pubs/{entry['year']}/{entry['ID']}")
        abstract = resource_dir + '-abstract.md'
        if os.path.exists(abstract):
            page.fm['abstract'] = open(abstract).read()

        slides = resource_dir + '-slides.pdf'
        if os.path.exists(slides):
            page.fm['url_slides'] = os.path.relpath(slides, static_dir)

        paper = resource_dir + '.pdf'
        if os.path.exists(paper):
            page.fm['url_paper'] = os.path.relpath(paper, static_dir)

        if url:
            page.fm['url_code'] = url
        page.dump()

def main():
    read_bib()

if __name__ == '__main__':
    main()
