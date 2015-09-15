#!flask/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 EDF SA
#
# This file is part of slurm-web.
#
# slurm-web is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# slurm-web is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with slurm-web.  If not, see <http://www.gnu.org/licenses/>.

import os
import ConfigParser

# path can be set by the env variable REST_CONF
path = os.getenv('RESTAPI_CONF', '/etc/slurm-web/restapi.conf')

default = {
    'cors': {
        'authorized_origins': 'http://localhost'
    },
    'racks': {
        'path': '/etc/slurm-web/racks.xml'
    },
    'cache': {
        'redis_url': 'redis://localhost:6379',
        'jobs_expiration': 10,
        'global_expiration': 86400
    }
}

settings = ConfigParser.ConfigParser(default)
settings.read(path)
