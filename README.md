# About
This is the small script for posting in your [octopress](https://github.com/imathis/octopress)-blog. It create `.markdown` in `source/_posts`
# How use it
You should run python-script `buildPost.py` with parameters (see below), but at first you must edit line
`md = buildmd.MD('/home/ssi/octopress/')`
and paste your octopress-root path(it must be absolute).
# Parameters and flags
* `-c` - flag for put comment-form to the end of created `.markdown`. It just copy all from `commentform.html` to the end.
* `-cat` or `--categories` - list of categories. They must be split by space and without quotes.
* `-ft` or `--filetitle` - this will be part of created `.markdown` name and URL. Must be without spaces.
* `-pt` or `--posttitle` - title of post. Must be quoted.