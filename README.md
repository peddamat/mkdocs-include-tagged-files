# MkDocs Include Published Files
A simple plugin that only allows files containing `publish: true` in their frontmatter to be output by MkDocs.

## Installation
Run `pip install --upgrade mkdocs-include-published-files`

## Configuration
Basic Configuration in the `mkdocs.yml` file:
```yaml
plugins:
  - mkdocs_include_published_files
```

This configuration will exclude all files that have one of the tags "confidential" or "excluded" in their frontmatter.
For example this file will be excluded:
```markdown
---
tags: ["confidential", "someothertag"]
---
# Content
```

By default, the plugin strips leading `#`-symbols from tags, so the tag `#excluded` will be treated the same as `excluded`.
If you want to disable this behavior set the config value `strip_leading_hashtags` to `false`.
