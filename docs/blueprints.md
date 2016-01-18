### Blueprints
> **Manage Cloudify's Blueprints**
* **upload** - Upload a blueprint to the Manager

| Option                | Description                              | Required |
| --------------------- | ---------------------------------------- | :------: |
| `-p,--blueprint-path` | Path to the application's blueprint file | True     |
| `-b,--blueprint-id`   | The id of the blueprint                  | True     |

* **publish-archive** - Publish a blueprint archive from a path or a URL to the Manager

| Option                    | Description                                             | Required | Default Value  |
| ------------------------- | ------------------------------------------------------- | :------: | -------------- |
| `-l,--archive-location`   | Path or URL to the application's blueprint archive file | True     |                |
| `-n,--blueprint-filename` | The name of the archive's main blueprint file           | False    | blueprint.yaml |
| `-b,--blueprint-id`       | The id of the blueprint                                 | True     |                |

* **download** - Download a blueprint from the Manager

| Option              | Description                                            | Required | Default Value  |
| ------------------- | ------------------------------------------------------ | :------: | -------------- |
| `-o,--output`       | The output file path of the blueprint to be downloaded | False    | The name of the download file, <br>placed in the current working directory
| `-b,--blueprint-id` | The id of the blueprint                                | True     |                |

* **list** - List all blueprints on the Manager

* **delete** - Delete a blueprint from the manager

| Option              | Description             | Required |
| ------------------- | ----------------------- | :------: |
| `-b,--blueprint-id` | The id of the blueprint | True     |

* **validate** - Validate a blueprint

| Option                | Description                              |
| --------------------- | ---------------------------------------- |
| `-p,--blueprint-path` | Path to the application's blueprint file |

* **get** - Get a blueprint by its id

| Option              | Description             | Required |
| ------------------- | ----------------------- | :------: |
| `-b,--blueprint-id` | The id of the blueprint | True     |

* **inputs** - List a blueprint's inputs

| Option              | Description             | Required |
| ------------------- | ----------------------- | :------: |
| `-b,--blueprint-id` | The id of the blueprint | True     |