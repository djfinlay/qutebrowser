# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2014-2016 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""Template configuration related to jinja2."""

from jinja2 import sandbox, exceptions, DictLoader

from qutebrowser.config import config
from qutebrowser.utils import log
from qutebrowser.browser.webkit import webview


class TabData():
    def __init__(self, title=0, index=None):
        self.title = title
        self.index = index


def get_and_render(sect, opt, **kwargs):
    """Helper for getting and rendering a config value. """
    return render(config.get(sect, opt), **kwargs)


def render(value, **kwargs):
    init()
    """Render a template string and pass the given arguments to it."""
    try:
        return _env.from_string(value).render(**kwargs)
    except exceptions.UndefinedError:
        log.misc.exception("UndefinedError while rendering " + value)
        raise

_inited = False


# TODO: FIX THIS
def init():
    global _inited
    global _env
    if not _inited:
        _env = sandbox.SandboxedEnvironment(loader=DictLoader(config.section('templates')))
        _inited = True
# TODO: Expose LoadStatus
# TODO: Maybe DictLoader?
