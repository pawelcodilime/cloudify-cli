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

"""
Handles 'cfy install'
"""

import os

from cloudify_cli.commands import blueprints
from cloudify_cli.commands import deployments
from cloudify_cli.commands import executions
from cloudify_cli.constants import DEFAULT_BLUEPRINT_FILE_NAME


def install(blueprint_path, blueprint_id, archive_location, blueprint_filename,
            deployment_id, inputs, workflow_id, parameters,
            allow_custom_parameters, timeout, include_logs):

    # We use the `archive_location` argument to distinguish between using
    # `install` in 'upload blueprint' mode, and using `install` in 'publish
    # archive' mode.
    if archive_location:
        # If blueprint-id wasn't supplied, assign it to the name of the archive
        if blueprint_id is None:

            filename, ext = os.path.splitext(
                    os.path.basename(archive_location))
            blueprint_id = filename

        blueprints.publish_archive(archive_location, blueprint_filename,
                                   blueprint_id)
    else:
        # If blueprint-id wasn't supplied, assign it to the name of
        # folder containing the application's blueprint file.
        if blueprint_id is None:

            blueprint_id = os.path.basename(
                    os.path.dirname(
                            os.path.abspath(
                                    blueprint_path.name)))

        blueprints.upload(blueprint_path, blueprint_id)

    # If deployment-id wasn't supplied, assign it to
    # the same name as the blueprint id.
    if deployment_id is None:
        deployment_id = blueprint_id

    deployments.create(blueprint_id, deployment_id, inputs)

    # although the `install` command does not need the `force` argument,
    # we *are* using the `executions start` handler as a part of it.
    # as a result, we need to provide it with a `force` argument, which is
    # defined below.
    force = False

    executions.start(workflow_id, deployment_id, timeout, force,
                     allow_custom_parameters, include_logs, parameters)
