# Text Replacer

A barebones "Custom autocorrect"/text replacement plugin for Zim.

Edit: now there's two of 'em! `inserttext.py` works like the Symbol list plugin, and doesn't require you to write a json

### How to use

1. Move `textreplacer.py` into the plugins folder
2. Create your replacements json and copy its full path
	* see `example.json` for reference
	* on Linux, moving `example.json` to `~/.local/share/zim/plugins/text_replacements.json` is enough to get going; you can skip the rest of the steps
3. Enable the plugin in Zim and click "Configure"
4. Paste in the path from step 2 and click "OK"

From now on, every time you type one of the words you specified it will get replaced with the replacement you've chosen; this can be undone via undo (Ctrl+Z).

To reload the json, toggle the plugin off and on again, or restart Zim.

#### json format

```json
{
	"coeur": "cœur",
	"zw": "[[https://zim-wiki.org/|**Zim Desktop Wiki**]]"
}
```

The json file should contain a single object with key-value pairs; the key is the string that will get replaced by the value. The keys shouldn't contain whitespace, but the values can. The values can also contain wiki formatting, though it isn't rendered before reload.

#### Troubleshooting

You can check the logs to confirm your replacements were successfully loaded. The following should show up:

```
INFO: Loaded n replacements from /your/replacements.json
```

If there's an error, n will be 0 and the above will be preceded by the encountered error.

```
ERROR: Failed to load json from bad path: Error text here
```

Some common errors and how to fix them:

* `[Errno 2] No such file or directory: 'bad path'`: check the path; aside from `~` and `~user` constructs you should use an absolute path (see [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) for more information)
* Check your json if any of these show up:
  * `Extra data: line n, column m, (char l)` (or `Expecting value: ...` etc): something's not json
  * `invalid json object`: couldn't be loaded as a Python `dict`
  * `json contains invalid keys`: non-string keys (how?)
  * `json contains invalid values`: non-string values
  * For more information, see the [Python json library docs](https://docs.python.org/3/library/json.html)

### System-wide alternatives

#### Linux

* [AutoKey](https://github.com/autokey/autokey) (GPL-3.0)

#### MacOS

* Settings > Keyboard > Text (built-in)

#### Windows

* [AutoHotkey](https://github.com/Lexikos/AutoHotkey_L) (GPL-2.0)
