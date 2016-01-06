########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
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
# * See the License for the specific language governing permissions and
#    * limitations under the License.

# flake8: noqa

import argparse

from cloudify_cli import commands as cfy
from cloudify_cli.config import completion_utils
from cloudify_cli.config import argument_utils
from cloudify_cli.constants import DEFAULT_REST_PORT

FORMAT_INPUT_AS_YAML_OR_DICT = 'formatted as YAML or as "key1=value1;key2=value2"'


def manager_blueprint_path_argument(hlp):
    return {
        'metavar': 'BLUEPRINT_FILE',
        'dest': 'blueprint_path',
        'type': argparse.FileType(),
        'required': True,
        'help': hlp,
        'completer': completion_utils.yaml_files_completer
    }


def local_blueprint_path_argument(hlp):
    return argument_utils.remove_completer(
        argument_utils.remove_metavar(
            argument_utils.remove_type(manager_blueprint_path_argument(hlp))
        )
    )


def blueprint_id_argument():
    return {
        'help': 'The id of the blueprint',
        'dest': 'blueprint_id',
        'required': True,
        'completer': completion_utils.objects_args_completer_maker('blueprints')
    }


def archive_location_argument():
    return {
        'dest': 'archive_location',
        'required': True,
        'help': "Path or URL to the application's blueprint archive file",
        'completer': completion_utils.archive_files_completer
    }


def blueprint_filename_argument():
    return {
        'dest': 'blueprint_filename',
        'help': "Name of the archive's main blueprint file",
    }


def deployment_id_argument(hlp):
    return {
        'dest': 'deployment_id',
        'help': hlp,
        'completer': completion_utils.objects_args_completer_maker('deployments')
    }


def inputs_argument(hlp):
    return {
        'dest': 'inputs',
        'default': 'inputs.yaml',
        'help': hlp
    }


def execution_id_argument(hlp):
    return {
        'dest': 'execution_id',
        'required': True,
        'help': hlp,
        'completer': completion_utils.objects_args_completer_maker('executions')
    }


def workflow_id_argument(hlp):
    return {
        'metavar': 'WORKFLOW',
        'dest': 'workflow_id',
        'required': True,
        'help': hlp,
        'completer': completion_utils.workflow_id_completer
    }


def parameters_argument():
    return {
        'dest': 'parameters',
        'default': {},
        'help': 'Parameters for the workflow execution ({0})'
        .format(FORMAT_INPUT_AS_YAML_OR_DICT)
    }


def allow_custom_parameters_argument():
    return {
        'dest': 'allow_custom_parameters',
        'action': 'store_true',
        'help': 'Allow the passing of custom parameters ('
                "parameters which were not defined in the workflow's schema "
                'in the blueprint) to the execution'
    }


def force_argument(hlp):
    return {
        'dest': 'force',
        'action': 'store_true',
        'default': False,
        'help': hlp
    }


def timeout_argument():
    return {
        'dest': 'timeout',
        'type': int,
        'default': 900,
        'help': 'Operation timeout in seconds (The execution itself will keep '
                'going, it is the CLI that will stop waiting for it to '
                'terminate)'
    }


def include_logs_argument():
    return {
        'dest': 'include_logs',
        'action': 'store_true',
        'help': 'Include logs in returned events'
    }


def install_plugins_argument():
    return {
        'dest': 'install_plugins',
        'action': 'store_true',
        'default': False,
        'help': 'Install necessary plugins of the given blueprint.'
    }


def task_retries_argument(default_value):
    return {
        'dest': 'task_retries',
        'default': default_value,
        'type': int,
        'help': 'How many times should a task be retried in case it fails'
    }


def task_retry_interval_argument(default_value):
    return {
        'dest': 'task_retry_interval',
        'default': default_value,
        'type': int,
        'help': 'How many seconds to wait before each task is retried'
    }


def task_thread_pool_size_argument():
    return {
        'dest': 'task_thread_pool_size',
        'default': 1,
        'type': int,
        'help': 'The size of the thread pool size to execute tasks in'
    }


def plugin_id_argument(hlp):
    return {
        'help': hlp,
        'dest': 'plugin_id',
        'required': True,
        'completer': completion_utils.objects_args_completer_maker('plugins')
    }


def snapshot_id_argument(hlp):
    return {
        'help': hlp,
        'dest': 'snapshot_id',
        'required': True,
        'completer': completion_utils.objects_args_completer_maker('snapshots')
    }


def parser_config():
    return {
        'description': 'Manages Cloudify in different Cloud Environments',
        'arguments': {
            '--version': {
                'help': 'show version information and exit',
                'action': cfy.version
            }
        },
        'commands': {
            'install': {
                'help': '',  # TODO add help text
                'arguments': {
                    # TODO make {blueprint-path, blueprint-id} and
                    # TODO {archive-location, blueprint-filename}
                    # TODO mutually exclusive groups?
                    '-p,--blueprint-path': argument_utils.make_optional(
                            argument_utils.set_default(
                                    manager_blueprint_path_argument(
                                            hlp="Path to the application's"
                                                "blueprint file"
                                    ), 'blueprint.yaml'
                            )
                    ),
                    '-b,--blueprint-id': argument_utils.remove_completer(
                            argument_utils.make_optional(blueprint_id_argument(
                            ))
                    ),
                    '--archive-location': argument_utils.make_optional( # TODO this originally also had `-l`, but I removed it as it conflicted with the `-l` of `include logs`
                            archive_location_argument()),
                    '-n,--blueprint-filename': blueprint_filename_argument(),
                    '-d,--deployment-id': deployment_id_argument(
                            hlp='The id of the deployed blueprint'
                    ),
                    '-i,--inputs': inputs_argument(
                        hlp='Inputs file/string for the deployment creation'
                            '({0})'.format(FORMAT_INPUT_AS_YAML_OR_DICT)
                    ),
                    '-w,--workflow': argument_utils.set_default(
                            argument_utils.make_optional(workflow_id_argument(
                                    hlp='The workflow to start (by default: '
                                        '`install`')),
                            'install'),
                    '--parameters': parameters_argument(),  # TODO this originally also had `-p`, but I removed it as it conflicted with the `-p` of `blueprint-path`
                    '--allow-custom-parameters':
                        allow_custom_parameters_argument(),
                    '--timeout': timeout_argument(),
                    '-l,--include-logs': include_logs_argument()
                },
                'handler': cfy.install
            },
            'uninstall': {
                'help': '',  # TODO add help text
                'arguments': {
                    '-b,--blueprint-id':
                        argument_utils.make_optional(blueprint_id_argument()),
                    '-d,--deployment-id': deployment_id_argument(
                            hlp='The id of the deployed blueprint'),
                    '-w,--workflow': argument_utils.set_default(
                            argument_utils.make_optional(workflow_id_argument(
                                    hlp='The workflow to start (by default: '
                                        '`uninstall`')),
                            'uninstall'),
                    '--parameters': parameters_argument(),  # TODO this originally also had `-p`, but I removed it as it conflicted with the `-p` of `blueprint-path` IN INSTALL
                    '--allow-custom-parameters':
                        allow_custom_parameters_argument(),
                    '--timeout': timeout_argument(),
                    '-l,--include-logs': include_logs_argument()
                    # TODO decide if --ignore-live-nodes from `cfy deployments delete` should be an argument.

                },
                'handler': cfy.uninstall
            },

            'plugins': {
                'help': "Manages Cloudify's plugins",
                'sub_commands': {
                    'upload': {
                        'arguments': {
                            '-p,--plugin-path': {
                                'metavar': 'PLUGIN_FILE',
                                'dest': 'plugin_path',
                                'type': argparse.FileType(),
                                'required': True,
                                'help': 'Path to the plugin file',
                                'completer': completion_utils.yaml_files_completer
                            }
                        },
                        'help': 'command for uploading a plugin to the management server',
                        'handler': cfy.plugins.upload
                    },
                    'get': {
                        'arguments': {
                            '-p,--plugin-id': plugin_id_argument(
                                hlp='The plugin id')
                        },
                        'help': 'Command for listing all modules according to their plugin id',
                        'handler': cfy.plugins.get
                    },
                    'download': {
                        'arguments': {
                            '-p,--plugin-id': plugin_id_argument(
                                hlp='The plugin id'),
                            '-o,--output': {
                                'help': 'The output file path of the plugin to be downloaded',
                                'dest': 'output',

                            }
                        },
                        'help': 'Command for downloading a plugin from the management server',
                        'handler': cfy.plugins.download
                    },
                    'list': {
                        'help': 'Command for listing all plugins on the '
                                'Manager',
                        'handler': cfy.plugins.ls
                    },
                    'delete': {
                        'arguments': {
                            '-p,--plugin-id': plugin_id_argument(
                                hlp='The plugin id')
                        },
                        'help': 'Command for deleting a plugin',
                        'handler': cfy.plugins.delete
                    }
                }
            },
            'blueprints': {
                'help': "Manages Cloudify's Blueprints",
                'sub_commands': {
                    'upload': {
                        'arguments': {
                            '-p,--blueprint-path':
                                manager_blueprint_path_argument(
                                        hlp="Path to the application's "
                                            "blueprint file"
                                ),
                            '-b,--blueprint-id': argument_utils.remove_completer(blueprint_id_argument())
                        },
                        'help': 'command for uploading a blueprint to the management server',
                        'handler': cfy.blueprints.upload
                    },
                    'publish-archive': {
                        'arguments': {
                            '-l,--archive-location': archive_location_argument(),
                            '-n,--blueprint-filename': blueprint_filename_argument(),
                            '-b,--blueprint-id': argument_utils.remove_completer(blueprint_id_argument())
                        },
                        'help': 'command for publishing a blueprint '
                                'archive from a path or URL to the '
                                'management server',
                        'handler': cfy.blueprints.publish_archive
                    },
                    'download': {
                        'arguments': {
                            '-b,--blueprint-id': blueprint_id_argument(),
                            '-o,--output': {
                                'help': 'The output file path of the blueprint to be downloaded',
                                'dest': 'output',

                            }
                        },
                        'help': 'command for downloading a blueprint from the management server',
                        'handler': cfy.blueprints.download
                    },
                    'list': {
                        'help': 'command for listing all blueprints on the '
                                'Manager',
                        'handler': cfy.blueprints.ls
                    },
                    'delete': {
                        'arguments': {
                            '-b,--blueprint-id': blueprint_id_argument()
                        },
                        'help': 'command for deleting a blueprint',
                        'handler': cfy.blueprints.delete
                    },
                    'validate': {
                        'arguments': {
                            '-p,--blueprint-path':
                                manager_blueprint_path_argument(
                                        hlp="Path to the application's "
                                            "blueprint file"
                                ),
                        },
                        'help': 'command for validating a blueprint',
                        'handler': cfy.blueprints.validate
                    },
                    'get': {
                        'arguments': {
                            '-b,--blueprint-id': blueprint_id_argument()
                        },
                        'help': 'command for getting a blueprint by its id',
                        'handler': cfy.blueprints.get
                    },
                    'inputs': {
                        'arguments': {
                            '-b,--blueprint-id': blueprint_id_argument()
                        },
                        'help': 'command for listing all available blueprint inputs',
                        'handler': cfy.blueprints.inputs
                    }
                }
            },
            'snapshots': {
                'help': "Manages Cloudify's Snapshots",
                'sub_commands': {
                    'create': {
                        'arguments': {
                            '-s,--snapshot-id': argument_utils.remove_completer(
                                snapshot_id_argument(
                                    hlp='A unique id that will be assigned to the created snapshot'
                                )
                            ),
                            '--include-metrics': {
                                'dest': 'include_metrics',
                                'action': 'store_true',
                                'default': False,
                                'help': 'Include metrics data'
                                        'in the snapshot'
                            },
                            '--exclude-credentials': {
                                'dest': 'exclude_credentials',
                                'action': 'store_true',
                                'default': False,
                                'help': 'Do not store credentials in snapshot'
                            }
                        },
                        'help': 'Create a new snapshot',
                        'handler': cfy.snapshots.create
                    },
                    'upload': {
                        'arguments': {
                            '-p,--snapshot-path': {
                                'metavar': 'SNAPSHOT_FILE',
                                'dest': 'snapshot_path',
                                'type': argparse.FileType(),
                                'required': True,
                                'help': "Path to the manager's snapshot file",
                                'completer': completion_utils.yaml_files_completer
                            },
                            '-s,--snapshot-id': argument_utils.remove_completer(snapshot_id_argument('The id of the snapshot'))
                        },
                        'help': 'Upload a snapshot to the management server',
                        'handler': cfy.snapshots.upload
                    },
                    'download': {
                        'arguments': {
                            '-s,--snapshot-id': snapshot_id_argument('The id of the snapshot'),
                            '-o,--output': {
                                'help': 'The output file path of the snapshot to be downloaded',
                                'dest': 'output',

                            }
                        },
                        'help': 'Download a snapshot from the management server',
                        'handler': cfy.snapshots.download
                    },
                    'list': {
                        'help': 'List all snapshots on the manager',
                        'handler': cfy.snapshots.ls
                    },
                    'delete': {
                        'arguments': {
                            '-s,--snapshot-id': snapshot_id_argument('The id of the snapshot')
                        },
                        'help': 'Delete a snapshot from the manager',
                        'handler': cfy.snapshots.delete
                    },
                    'restore': {
                        'arguments': {
                            '-s,--snapshot-id': snapshot_id_argument('The id of the snapshot'),
                            '--without-deployments-envs': {
                                'dest': 'without_deployments_envs',
                                'action': 'store_true',
                                'default': False,
                                'help': 'Restore snapshot without deployment environments'
                            },
                            '-f,--force':
                                force_argument(
                                        hlp='Force restoring the snapshot on '
                                            'a dirty manager')
                        },
                        'help': 'Restore manager state to a specific snapshot',
                        'handler': cfy.snapshots.restore
                    }
                }
            },
            'agents': {
                'help': "Manages Cloudify's Agents",
                'sub_commands': {
                    'install': {
                        'arguments': {
                            '-d,--deployment-id': deployment_id_argument(
                                hlp='The id of the deployment to install '
                                    'agents for. If omitted, this will '
                                    'install agents for all deployments'
                            ),
                            '-l,--include-logs': include_logs_argument()
                        },
                        'help':'command for installing agents on deployments',
                        'handler': cfy.agents.install
                    }
                }
            },
            'deployments': {
                'help': "Manages and Executes Cloudify's Deployments",
                'sub_commands': {
                    'create': {
                        'arguments': {
                            '-d,--deployment-id': argument_utils.remove_completer(
                                deployment_id_argument(
                                    hlp='A unique id that will be assigned to '
                                        'the created deployment'
                                )
                            ),
                            '-b,--blueprint-id': blueprint_id_argument(),
                            '-i,--inputs': inputs_argument(
                                hlp='Inputs file/string for the deployment'
                                    'creation ({0})'
                                    .format(FORMAT_INPUT_AS_YAML_OR_DICT))
                        },
                        'help': 'command for creating a deployment of a blueprint',
                        'handler': cfy.deployments.create
                    },
                    'delete': {
                        'arguments': {
                            '-d,--deployment-id': deployment_id_argument(
                                hlp='The id of the deployment to delete'),
                            '-f,--ignore-live-nodes': {
                                'dest': 'ignore_live_nodes',
                                'action': 'store_true',
                                'default': False,
                                'help': 'Delete the deployment even '
                                        'if there are existing live nodes for it'
                            }
                        },
                        'help': 'command for deleting a deployment',
                        'handler': cfy.deployments.delete
                    },
                    'list': {
                        'arguments': {
                            '-b,--blueprint-id': argument_utils.make_optional(
                                blueprint_id_argument()
                            )
                        },
                        'help': 'command for listing all deployments or all deployments'
                                ' of a blueprint',
                        'handler': cfy.deployments.ls
                    },
                    'outputs': {
                        'arguments': {
                            '-d,--deployment-id': deployment_id_argument(
                                hlp='The id of the deployment to get outputs '
                                    'for'
                            )
                        },
                        'help': 'command for getting a specific deployment outputs',
                        'handler': cfy.deployments.outputs
                    }
                }
            },
            'events': {
                'help': "Manages Cloudify's events",
                'sub_commands': {
                    'list': {
                        'arguments': {
                            '-l,--include-logs': include_logs_argument(),
                            '-e,--execution-id': execution_id_argument(
                                hlp='The id of the execution to list events for'
                            ),
                            '--tail': {
                                'dest': 'tail',
                                'action': 'store_true',
                                'default': False,
                                'help': 'tail the events of the specified execution until it ends'
                            }
                        },
                        'help': 'Displays Events for different executions',
                        'handler': cfy.events.ls
                    }
                }
            },
            'executions': {
                'help': "Manages Cloudify's Executions",
                'sub_commands': {
                    'get': {
                        'arguments': {
                            '-e,--execution-id': execution_id_argument(
                                hlp='The id of the execution to get'
                            )
                        },
                        'help': 'command for getting an execution by its id',
                        'handler': cfy.executions.get
                    },
                    'list': {
                        'arguments': {
                            '-d,--deployment-id': deployment_id_argument(
                                hlp="Filter executions for a given deployment "
                                    "by the deployment's id"
                            ),
                            '--system-workflows': {
                                'dest': 'include_system_workflows',
                                'action': 'store_true',
                                'default': False,
                                'help': 'Include executions of system workflows.'
                            },
                        },
                        'help': 'command for listing all executions of a deployment',
                        'handler': cfy.executions.ls
                    },
                    'start': {
                        'arguments': {
                            '-w,--workflow': workflow_id_argument(
                                hlp='The workflow to start'),
                            '-p,--parameters': parameters_argument(),
                            '--allow-custom-parameters':
                                allow_custom_parameters_argument(),
                            '--timeout': timeout_argument(),
                            '-f,--force':
                                force_argument(
                                        hlp='Whether the workflow should '
                                            'execute even if there is an '
                                            'ongoing execution for the'
                                            'provided deployment'
                                ),
                            '-l,--include-logs': include_logs_argument(),
                            '-d,--deployment-id': deployment_id_argument(
                                hlp='The deployment id')
                        },
                        'help': 'Command for starting a workflow execution on a deployment',
                        'handler': cfy.executions.start
                    },
                    'cancel': {
                        'arguments': {
                            '-e,--execution-id': execution_id_argument(
                                hlp='The id of the execution to cancel'
                            ),
                            '-f,--force': force_argument(
                                    hlp='Terminate the execution abruptly, '
                                        'rather than request an orderly '
                                        'termination')
                        },
                        'help': 'Cancel an execution by its id',
                        'handler': cfy.executions.cancel
                    }
                }
            },
            'nodes': {
                'help': 'Manage nodes',
                'sub_commands': {
                    'get': {
                        'arguments': {
                            '--node-id': {
                                'dest': 'node_id',
                                'required': True,
                                'help': 'The ID of the node to get'
                            },
                            '-d,--deployment-id': argument_utils.make_required(
                                    deployment_id_argument(
                                            hlp='Filter nodes for a given '
                                                'deployment according to the '
                                                'deployment ID'))
                        },
                        'help': 'command for getting a node by its ID',
                        'handler': cfy.nodes.get
                    },
                    'list': {
                        'arguments': {
                            '-d,--deployment-id': deployment_id_argument(
                                    hlp='Filter nodes for a given deployment '
                                        'according to the deployment ID')
                        },
                        'help': 'Command for getting all nodes',
                        'handler': cfy.nodes.ls
                    }
                }
            },
            'node-instances': {
                'help': 'Manage node instances',
                'sub_commands': {
                    'get': {
                        'arguments': {
                            '--node-instance-id': {
                                'dest': 'node_instance_id',
                                'required': True,
                                'help': 'The ID of the node instance to get'
                            }
                        },
                        'help': 'Command for getting a node instance according to it\'s ID',
                        'handler': cfy.node_instances.get
                    },
                    'list': {
                        'arguments': {
                            '-d,--deployment-id': deployment_id_argument(
                                    hlp='Filter node instances for a given '
                                        'deployment according to the '
                                        'deployment ID'),
                            '--node-name': {
                                'dest': 'node_name',
                                'help': 'Filter node instances according to the node name'
                            }
                        },
                        'help': 'Command for getting node instances',
                        'handler': cfy.node_instances.ls
                    }
                }
            },
            'workflows': {
                'help': 'Manages Deployment Workflows',
                'sub_commands': {
                    'get': {
                        'arguments': {
                            '-d,--deployment-id': deployment_id_argument(
                                hlp='The id of the deployment for whic  h the '
                                    'workflow belongs'
                            ),
                            '-w,--workflow': workflow_id_argument(
                                hlp='The id of the workflow to get'
                            )
                        },
                        'help': 'command for getting a workflow by its name and deployment',
                        'handler': cfy.workflows.get
                    },
                    'list': {
                        'arguments': {
                            '-d,--deployment-id': deployment_id_argument(
                                hlp='The id of the deployment whose workflows '
                                    'to list'
                            )
                        },
                        'help': 'command for listing workflows for a deployment',
                        'handler': cfy.workflows.ls
                    }
                }
            },
            'local': {
                'help': 'Execute workflows locally',
                'sub_commands': {
                    'install': {
                        'help': '',  # TODO add help text
                        'arguments': {
                            '-p,--blueprint-path':
                                argument_utils.make_optional(
                                        argument_utils.set_default(
                                            local_blueprint_path_argument(
                                                hlp="Path to the application's"
                                                    "blueprint file"
                                            ), 'blueprint.yaml'
                                        )
                                ),
                            '-i,--inputs': inputs_argument(
                                    hlp='Inputs file/string for the '
                                        'deployment creation({0})'.
                                        format(FORMAT_INPUT_AS_YAML_OR_DICT)),
                            '--install-plugins': install_plugins_argument(),
                            '-w,--workflow': argument_utils.set_default(
                                    argument_utils.make_optional(
                                            workflow_id_argument(
                                                    hlp='The workflow to start'
                                                        ' (by default: '
                                                        '`install`')),
                                    'install'),
                            '--parameters': parameters_argument(),  # TODO this originally also had `-p`, but I removed it as it conflicted with the `-p` of `blueprint-path`
                            '--allow-custom-parameters':
                                allow_custom_parameters_argument(),
                            '--task-retries': task_retries_argument(0),
                            '--task-retry-interval':
                                task_retry_interval_argument(1),
                            '--task-thread-pool-size':
                                task_thread_pool_size_argument()
                        },
                        'handler': cfy.local.install
                    },
                    'init': {
                        'help': 'Init a local workflow execution environment '
                                'in the current working directory',
                        'arguments': {
                            '-p,--blueprint-path':
                                local_blueprint_path_argument(
                                        hlp='Path to a blueprint'
                                ),
                            '-i,--inputs': inputs_argument(
                                    hlp='Inputs file/string for the local '
                                        'workflow creation ({0})'
                                        .format(FORMAT_INPUT_AS_YAML_OR_DICT)
                                ),
                            '--install-plugins': install_plugins_argument(),
                        },
                        'handler': cfy.local.init
                    },
                    'install-plugins': {
                        'help': 'Installs the necessary plugins for a given blueprint',
                        'arguments': {
                            '-p,--blueprint-path':
                                local_blueprint_path_argument(
                                        hlp='Path to a blueprint'
                                ),
                        },
                        'handler': cfy.local.install_plugins
                    },
                    'create-requirements': {
                        'help': 'Creates a PIP compliant requirements file for the given blueprint',
                        'arguments': {
                            '-p,--blueprint-path':
                                local_blueprint_path_argument(
                                        hlp='Path to a blueprint'
                                ),
                            '-o,--output': {
                                'metavar': 'REQUIREMENTS_OUTPUT',
                                'dest': 'output',
                                'help': 'Path to a file that will hold the '
                                        'requirements of the blueprint'
                            }
                        },
                        'handler': cfy.local.create_requirements
                    },
                    'execute': {
                        'help': 'Execute a workflow locally',
                        'arguments': {
                            '-w,--workflow':
                                argument_utils.remove_completer(
                                    workflow_id_argument(
                                        hlp='The workflow to execute locally'))
                            ,
                            '-p,--parameters': parameters_argument(),
                            '--allow-custom-parameters':
                                allow_custom_parameters_argument(),
                            '--task-retries': task_retries_argument(0),
                            '--task-retry-interval':
                                task_retry_interval_argument(1),
                            '--task-thread-pool-size':
                                task_thread_pool_size_argument()
                        },
                        'handler': cfy.local.execute
                    },
                    'outputs': {
                        'help': 'Display outputs',
                        'arguments': {},
                        'handler': cfy.local.outputs
                    },
                    'instances': {
                        'help': 'Display node instances',
                        'arguments': {
                            '--node-id': {
                                'dest': 'node_id',
                                'help': 'Only display node instances of this node id'
                            }
                        },
                        'handler': cfy.local.instances
                    }
                }
            },
            'status': {
                'help': "Show a management server's status",
                'handler': cfy.status
            },
            'dev': {
                'help': 'Executes fabric tasks on the management machine',
                'arguments': {
                    '-t,--task': {
                        'dest': 'task',
                        'help': 'name of fabric task to run',
                        'completer': completion_utils.dev_task_name_completer
                    },
                    '-a,--args': {
                        'nargs': argparse.REMAINDER,
                        'dest': 'args',
                        'help': 'arguments for the fabric task'
                    },
                    '-p,--tasks-file': {
                        'dest': 'tasks_file',
                        'help': 'Path to a tasks file',
                    }
                },
                'handler': cfy.dev
            },
            'ssh': {
                'help': 'SSH to management server',
                'arguments': {
                    '-c,--command': {
                        'dest': 'ssh_command',
                        'metavar': 'COMMAND',
                        'help': 'Execute command over SSH'
                    },
                    '-p,--plain': {
                        'dest': 'ssh_plain_mode',
                        'action': 'store_true',
                        'help': 'Leave authentication to user'
                    }
                },
                'handler': cfy.ssh
            },
            'bootstrap': {
                'help': 'Bootstrap a Cloudify management environment',
                'arguments': {
                    '-p,--blueprint-path':
                        local_blueprint_path_argument(
                                hlp='Path to a blueprint'
                        ),
                    '-i,--inputs': inputs_argument(
                        hlp='Inputs file/string for a manager blueprint ({0})'
                            .format(FORMAT_INPUT_AS_YAML_OR_DICT)
                    ),
                    '--keep-up-on-failure': {
                        'dest': 'keep_up',
                        'action': 'store_true',
                        'help': 'If the bootstrap fails,'
                                ' the management server will remain running'
                    },
                    '--skip-validations': {
                        'dest': 'skip_validations',
                        'action': 'store_true',
                        'help': 'Run bootstrap without,'
                                ' validating resources prior to bootstrapping the manager'
                    },
                    '--validate-only': {
                        'dest': 'validate_only',
                        'action': 'store_true',
                        'help': 'Run validations without'
                                ' actually performing the bootstrap process.'
                    },
                    '--install-plugins': install_plugins_argument(),
                    '--task-retries': task_retries_argument(5),
                    '--task-retry-interval': task_retry_interval_argument(30),
                    '--task-thread-pool-size':
                        task_thread_pool_size_argument()
                },
                'handler': cfy.bootstrap
            },
            'teardown': {
                'help': 'Teardown Cloudify',
                'arguments': {
                    '--ignore-deployments': {
                        'dest': 'ignore_deployments',
                        'action': 'store_true',
                        'help': 'Perform teardown even if deployments'
                                'exist on the manager'
                    },
                    '-f,--force': force_argument(
                            hlp='Confirmation for the teardown request')
                },
                'handler': cfy.teardown
            },
            'recover': {
                'help': 'Performs recovery of the management machine '
                        'and all its contained nodes.',
                'arguments': {
                    '-f,--force': force_argument(
                            hlp='Confirmation for the recovery request'
                    ),
                    '--task-retries': task_retries_argument(5),
                    '--task-retry-interval': task_retry_interval_argument(30),
                    '--task-thread-pool-size':
                        task_thread_pool_size_argument(),
                    '-s,--snapshot-path': {
                        'dest': 'snapshot_path',
                        'type': argparse.FileType(),
                        'help': 'Path to the snapshot that will be restored'
                    }
                },
                'handler': cfy.recover
            },
            'use': {
                'help': 'Use/switch to the specified management server',
                'arguments': {
                    '-t,--management-ip': {
                        'help': 'The cloudify management server ip address',
                        'dest': 'management_ip',
                        'required': True
                    },
                    '--port': {
                        'help': 'Specify the rest server port',
                        'default': DEFAULT_REST_PORT,
                        'type': int,
                        'dest': 'rest_port'
                    }
                },
                'handler': cfy.use
            },
            'init': {
                'help': 'Initialize cfy work environment',
                'arguments': {
                    '-r,--reset-config': {
                        'dest': 'reset_config',
                        'action': 'store_true',
                        'help': 'Overwriting existing configuration is allowed'
                    },
                },
                'handler': cfy.init
            }
        }
    }
