########
# Copyright (c) 2015 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

# TODO make all the command docstrings consistent
"""
Handles all commands that start with 'cfy install'
"""

from cloudify_cli.commands import blueprints
from cloudify_cli.commands import deployments


def install(blueprint_path, blueprint_id, archive_location, blueprint_filename,
            deployment_id, inputs, workflow, parameters,
            allow_custom_parameters, timeout, include_logs):

    # the following conditions are a simple patch. Not the final and real deal:
    if archive_location is None and blueprint_filename is None:
        blueprints.upload(blueprint_path, blueprint_id)
        pass
    else:
        blueprints.publish_archive(archive_location, blueprint_filename,
                                   blueprint_id)
        pass

    deployments.create(blueprint_id, deployment_id, inputs)
    # TODO commit this wednesday morning!!!



