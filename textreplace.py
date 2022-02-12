from json import load

from zim.plugins import PluginClass
from zim.gui.pageview import PageViewExtension

import logging
logger = logging.getLogger('zim.plugins.textreplacer')


class TextReplacerPlugin(PluginClass):
    plugin_info = {
            'name': _('Text Replacer'),  # T: plugin name
            'description': _('''\
Text replacer allows you to define shortcuts for strings,
similar to the built-in symbol replacement.

With thanks to HorseLuvver and gandrille.
'''),  # T: plugin description
            'author': 'introt <introt@koti.fimnet.fi>'
            }

    plugin_preferences = (
            ('json_path', 'string', _('Path to text replacements dictionary json file'), ''),  # T: plugin preference
        )


class TextReplacerPageViewExtension(PageViewExtension):
    def __init__(self, plugin, pageview):
        PageViewExtension.__init__(self, plugin, pageview)
        self.replacements = {}
        path = self.plugin.preferences['json_path']
        try:
            with open(path, 'r') as f:
                json = load(f)
            assert type(json) == dict, 'invalid json object'
            assert all(type(key) == str for key in json.keys()), 'json contains invalid keys'
            assert all(type(val) == str for val in json.values()), 'json contains invalid values'
            self.replacements = json
            self.connectto(pageview.textview, 'end-of-word', self.on_end_of_word)
        except Exception as e:
            logger.error('Failed to load json from %s: %s', path, e)
        finally:
            logger.info('Loaded %s replacements from %s', len(self.replacements.keys()), path)

    def on_end_of_word(self, textview, start, end, word, char, editmode):
        buffer = textview.get_buffer()
        if word in self.replacements.keys():
            with buffer.tmp_cursor(start):
                buffer.delete(start, end)
                buffer.insert_at_cursor(self.replacements[word])
            buffer.set_modified(True)
            textview.stop_emission('end_of_word')
