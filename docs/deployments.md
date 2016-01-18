### Deployments
> **Manage Cloudify's Deployments**

* **create** - Create a deployment from a blueprint

| Option               | Description                                                                          |
| -------------------- | ------------------------------------------------------------------------------------ |
| `-d,--deployment-id` | A unique id that will be assigned to the created deployment                          |
| `-b,--blueprint-id`  | The blueprint's id                                                                   |
| `-i,--inputs`        | Inputs for the deployment creation, formatted as YAML or as "key1=value1;key2=value2 |

* **delete** - Delete a deployment from the manager

| Option                   | Description                                                        |
| ------------------------ | ------------------------------------------------------------------ |
| `-d,--deployment-id`     | The id of the deployment to delete                                 |
| `-b,--blueprint-id`      | The blueprint's id                                                 |
| `-f,--ignore-live-nodes` | Delete the deployment even if there are existing live nodes for it |

* **list** - List the all deployments on the manager, or all deployments of a specific blueprint

| Option                   | Description         |
| ------------------------ | ------------------- |
| `-b,--blueprint-id`      | The blueprint's id  |

* **outputs** - Get outputs for a specific deployment

| Option                   | Description         |
| ------------------------ | ------------------- |
| `-d,--deployment-id`     | The blueprint's id  |
