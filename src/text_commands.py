#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin

import subprocess


def plugin_loaded():
    '''
        Sublime 3 calls this once the plugin API is ready.
    '''

    s = sublime.load_settings('base64.sublime-settings')

    base64_readme_shown = s.get('base64.readme_shown', False)
    if not base64_readme_shown:
        s.set('base64.readme_shown', True)
        sublime.save_settings('base64.sublime-settings')
        sublime.set_timeout_async(lambda: sublime.active_window().run_command('base64_readme'), 5000)


def base64(view, data, opts_in):
    '''
        base64 calls the base64 binary to process the data and returns the result.
    '''

    window = view.window()
    s = sublime.load_settings('base64.sublime-settings')
    base64_command = s.get('base64.command', 'base64')
    opts = [base64_command]
    opts += opts_in
    try:
        base64_process = subprocess.Popen(opts,
                                          universal_newlines=False,
                                          stdin=subprocess.PIPE,
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE)
        result, error = base64_process.communicate(input=data.encode())
        if error:
            panel(window, error.decode())
        if base64_process.returncode:
            return None
        return result.decode().strip('\n')
    except IOError as e:
        panel(window, 'Error: %s' % e)
        return None
    except OSError as e:
        panel(window, 'Error: %s' % e)
        return None


def panel(window, message):
    '''
        Panel displays base64's stderr at the bottom of the window.
    '''

    p = window.create_output_panel('base64_message')
    p.run_command('base64_message', {'message': message})
    p.show(p.size())
    window.run_command('show_panel', {'panel': 'output.base64_message'})


class Base64ReadmeCommand(sublime_plugin.TextCommand):
    '''
        Readme
    '''

    def run(self, edit):
        v = self.view.window().new_file()
        v.set_name('Base64: Readme')
        v.settings().set('gutter', False)
        v.insert(edit, 0, sublime.load_resource('Packages/Base64/README.md'))
        # v.set_syntax_file('Packages/Markdown/Markdown.sublime-syntax')
        v.set_read_only(True)
        v.set_scratch(True)


class Base64ChangelogCommand(sublime_plugin.TextCommand):
    '''
        Changelog
    '''

    def run(self, edit):
        v = self.view.window().new_file()
        v.set_name('Base64: Changelog')
        v.settings().set('gutter', False)
        v.insert(edit, 0, sublime.load_resource('Packages/Base64/CHANGELOG.md'))
        # v.set_syntax_file('Packages/Markdown/Markdown.sublime-syntax')
        v.set_read_only(True)
        v.set_scratch(True)


class Base64MessageCommand(sublime_plugin.TextCommand):
    '''
        A helper command for panel.
    '''

    def run(self, edit, message):
        v = self.view
        v.insert(edit, v.size(), message)


class Base64EncodeCommand(sublime_plugin.TextCommand):
    '''
        Encodes plaintext to a Base64 format.
    '''

    def run(self, edit):
        opts = []
        v = self.view
        for selection in v.sel():
            data = base64(v, v.substr(selection), opts)
            if data:
                # v.replace(edit, doc, data)
                v.replace(edit, selection, data)


class Base64DecodeCommand(sublime_plugin.TextCommand):
    '''
        Decodes a Base64 format message.
    '''

    def run(self, edit):
        opts = ['--decode']
        v = self.view
        for selection in v.sel():
            data = base64(v, v.substr(selection), opts)
            if data:
                # v.replace(edit, doc, data)
                v.replace(edit, selection, data)
