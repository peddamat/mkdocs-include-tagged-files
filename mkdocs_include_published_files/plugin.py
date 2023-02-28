import os
import typing
from typing import Optional

import frontmatter
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

import logging
log = logging.getLogger(f"mkdocs.plugins.{__name__}")


class IncludePublishedFilesPlugin(BasePlugin):
    def is_page_published(self, meta: typing.Dict):
        if 'publish' in meta:
            if meta['publish'] == True:
                return True

            return False

    def on_files(self, files: Files, *, config: MkDocsConfig) -> Optional[Files]:
        # Getting the root location of markdown source files
        base_docs_url = config["docs_dir"]

        for file in files.documentation_pages():
            abs_path = os.path.join(base_docs_url, file.src_uri)
            with open(abs_path, 'r') as raw_file:
                metadata = frontmatter.load(raw_file).metadata

                if not self.is_page_published(metadata):
                    log.info(f"IncludePublishedFilesPlugin skipping {file.src_uri}")
                    files.remove(file)

        return files

    def on_post_page(self, output: str, *, page: Page, config: MkDocsConfig) -> Optional[str]:
        if not self.is_page_published(page.meta):
            return ''

        return output
