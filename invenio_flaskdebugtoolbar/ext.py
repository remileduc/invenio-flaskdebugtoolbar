# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Invenio module that integrates the flask debug toolbar."""

from __future__ import absolute_import, print_function

from flask_debugtoolbar import DebugToolbarExtension

from . import config


class InvenioFlaskDebugToolbar(object):
    """Invenio-FlaskDebugToolbar extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        DebugToolbarExtension(app)
        app.extensions['invenio-flaskdebugtoolbar'] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        if 'BASE_TEMPLATE' in app.config:
            app.config.setdefault(
                'DEBUG_TB_BASE_TEMPLATE',
                app.config['BASE_TEMPLATE'],
            )
        if config.DEBUG_TB_ENABLED is None:
            app.config.setdefault('DEBUG_TB_ENABLED', app.debug)
        for k in dir(config):
            if k.startswith('DEBUG_TB_'):
                app.config.setdefault(k, getattr(config, k))
