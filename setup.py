from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent

setup(
    name='mkdocs-include-published-files',
    version='1.0.0',
    packages=['mkdocs_include_published_files'],
    url='https://github.com/peddamat/mkdocs-include-published-files',
    license='MIT',
    author='Sam Peddamatham <peddamat@gmail.com>',
    author_email='peddamat@gmail.com',
    description='A mkdocs plugin that only includes files containing `publish: true` in their frontmatter.',
    long_description=(this_directory / "README.md").read_text(),
    long_description_content_type='text/markdown',
    keywords=['mkdocs', 'mkdocs-plugin'],
    install_requires=['mkdocs', 'python-frontmatter'],

    entry_points={
        'mkdocs.plugins': [
            'mkdocs_include_published_files = mkdocs_include_published_files.plugin:IncludePublishedFilesPlugin',
        ]
    },
)
