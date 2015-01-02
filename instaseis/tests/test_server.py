#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test for the Instaseis server.

:copyright:
    Lion Krischer (krischer@geophysik.uni-muenchen.de), 2014
:license:
    GNU General Public License, Version 3
    (http://www.gnu.org/copyleft/gpl.html)
"""
from __future__ import absolute_import

import json

import instaseis
from .tornado_testing_fixtures import client_db_bwd_displ_only  # NOQA


def test_root_route(client_db_bwd_displ_only):  # NOQA
    """
    Shows very basic information and the version of the client.
    """
    client = client_db_bwd_displ_only
    request = client.fetch("/")
    assert request.code == 200
    result = json.loads(str(request.body.decode("utf8")))
    assert result == {
        "type": "Instaseis Remote Server", "version": instaseis.__version__}