.. meta::
    :description: Each deployment contains a metadata file that contains details about the deployment version your code is running on.

.. _howto-deployment-metadata:

Deployment version metadata
#########################################

.. admonition:: Quick introduction to deployments
    :class: tip

    * Valohai deployments are primarily used for online inference
    * All deployments are served from a Kubernetes cluster
    * Each deployment can contain multiple versions, and each version can contain multiple endpoints
    * Valohai includes a ``valohai-metadata.json`` file in each deployment version

..

You can easily access the ``valohai-metadata.json`` file and read the details that you need for your execution. Inside your deployment code read the file and parse out the values that you're interested in.

.. note:: 

    The ``valohai-metadata.json`` file is read-only so it is not possible to customize the metadata for deployments.


.. code--block:: python

    with open('valohai-metadata.json', 'r') as f:
        metadata = json.load(f)

    print(f"Deployment ID: {metadata['deployment']['id']}")
    print(f"Deployment Version ID: {metadata['version']['id']}")
    print(f"Deployment version created: {metadata['version']['ctime']}")
    print(f"Model ID: {metadata['version']['endpoints'][0]['files'][0]['datum']['id']}")
    print(f"Model file created: {metadata['version']['endpoints'][0]['files'][0]['datum']['ctime']}")
    print(f"File was output from execution: {metadata['version']['endpoints'][0]['files'][0]['datum']['output_execution']}")

..

.. code-block:: json

    {
        "deployment": {
            "ctime": "2021-07-08T05:36:49.575910Z",
            "enabled": true,
            "id": "017a849e-5fa7-9a95-a13c-519fdca7dbdc",
            "name": "test",
            "owner": 123,
            "project": {
                "ctime": "2021-07-08T05:36:28.772504Z",
                "description": "",
                "enabled_endpoint_count": null,
                "execution_count": null,
                "id": "017a849e-0e64-8a79-c338-6eb6878f6c8c",
                "last_execution_ctime": null,
                "mtime": "2021-07-08T05:36:28.772529Z",
                "name": "deployment-metadata",
                "owner": {
                    "id": 123,
                    "username": "sample"
                },
                "queued_execution_count": null,
                "running_execution_count": null,
                "url": "https://app.valohai.com/api/v0/projects/017a849e-0e64-8a79-c338-6eb6878f6c8c/",
                "urls": {
                    "display": "https://app.valohai.com/p/sample/deployment-metadata/",
                    "display_repository": "https://app.valohai.com/p/sample/deployment-metadata/settings/repository/"
                }
            },
            "target": "0162621f-9db5-9889-6a6e-d3030117b9a8",
            "target_log_handler_type": "elasticsearch",
            "url": "https://app.valohai.com/api/v0/deployments/017a849e-5fa7-9a95-a13c-519fdca7dbdc/",
            "urls": {
                "display": "https://app.valohai.com/p/sample/deployment-metadata/deployment/017a849e-5fa7-9a95-a13c-519fdca7dbdc/"
            },
            "version_aliases": [],
            "versions": [
                {
                    "commit": {
                        "adhoc": true,
                        "commit_time": "2021-07-08T05:36:37.470388Z",
                        "description": "",
                        "has_config": true,
                        "identifier": "~6317ab30673a2a7e1fca502abae894304542128e4253c107c3827737e4cc205a",
                        "ref": "adhoc",
                        "urls": {
                            "display": "https://app.valohai.com/p/sample/deployment-metadata/commits/~6317ab30673a2a7e1fca502abae894304542128e4253c107c3827737e4cc205a/"
                        }
                    },
                    "ctime": "2021-07-08T05:37:11.431914Z",
                    "deployment": "017a849e-5fa7-9a95-a13c-519fdca7dbdc",
                    "enabled": false,
                    "id": "017a849e-b507-c5b2-f02d-77629e84bcd4",
                    "name": "20210708.0",
                    "url": "https://app.valohai.com/api/v0/deployment-versions/017a849e-b507-c5b2-f02d-77629e84bcd4/"
                },
                {
                    "commit": {
                        "adhoc": true,
                        "commit_time": "2021-07-08T05:39:51.833275Z",
                        "description": "",
                        "has_config": true,
                        "identifier": "~7cfbf760e76caa424a31420086c68b53dbffcd2bae29758b03e75860f9e828a9",
                        "ref": "adhoc",
                        "urls": {
                            "display": "https://app.valohai.com/p/sample/deployment-metadata/commits/~7cfbf760e76caa424a31420086c68b53dbffcd2bae29758b03e75860f9e828a9/"
                        }
                    },
                    "ctime": "2021-07-08T05:40:03.296897Z",
                    "deployment": "017a849e-5fa7-9a95-a13c-519fdca7dbdc",
                    "enabled": false,
                    "id": "017a84a1-5460-f531-b199-e5e361416d4c",
                    "name": "20210708.1",
                    "url": "https://app.valohai.com/api/v0/deployment-versions/017a84a1-5460-f531-b199-e5e361416d4c/"
                },
                {
                    "commit": {
                        "adhoc": true,
                        "commit_time": "2021-07-08T05:42:02.406358Z",
                        "description": "",
                        "has_config": true,
                        "identifier": "~f3225ec51c8265b0484fff2566b2e71e69d4634fb1ffeda0b836d0d3ce5f1acf",
                        "ref": "adhoc",
                        "urls": {
                            "display": "https://app.valohai.com/p/sample/deployment-metadata/commits/~f3225ec51c8265b0484fff2566b2e71e69d4634fb1ffeda0b836d0d3ce5f1acf/"
                        }
                    },
                    "ctime": "2021-07-08T05:42:11.696183Z",
                    "deployment": "017a849e-5fa7-9a95-a13c-519fdca7dbdc",
                    "enabled": true,
                    "id": "017a84a3-49ef-9466-73fb-f2b8555ffc9a",
                    "name": "20210708.2",
                    "url": "https://app.valohai.com/api/v0/deployment-versions/017a84a3-49ef-9466-73fb-f2b8555ffc9a/"
                },
                {
                    "commit": {
                        "adhoc": true,
                        "commit_time": "2021-07-08T05:52:09.304950Z",
                        "description": "",
                        "has_config": true,
                        "identifier": "~f3d310901f9db9a4ddef9beebc722282215be12ff1632d0597b8be9a77246bd7",
                        "ref": "adhoc",
                        "urls": {
                            "display": "https://app.valohai.com/p/sample/deployment-metadata/commits/~f3d310901f9db9a4ddef9beebc722282215be12ff1632d0597b8be9a77246bd7/"
                        }
                    },
                    "ctime": "2021-07-08T05:52:20.638419Z",
                    "deployment": "017a849e-5fa7-9a95-a13c-519fdca7dbdc",
                    "enabled": false,
                    "id": "017a84ac-949e-c580-c746-43c06121a092",
                    "name": "20210708.3",
                    "url": "https://app.valohai.com/api/v0/deployment-versions/017a84ac-949e-c580-c746-43c06121a092/"
                },
                {
                    "commit": {
                        "adhoc": true,
                        "commit_time": "2021-07-08T05:55:30.227325Z",
                        "description": "",
                        "has_config": true,
                        "identifier": "~ec89eff575ae08aee6bd6fdb207e04e814b309c226af058891f9b4c6d1416df1",
                        "ref": "adhoc",
                        "urls": {
                            "display": "https://app.valohai.com/p/sample/deployment-metadata/commits/~ec89eff575ae08aee6bd6fdb207e04e814b309c226af058891f9b4c6d1416df1/"
                        }
                    },
                    "ctime": "2021-07-08T05:55:39.659645Z",
                    "deployment": "017a849e-5fa7-9a95-a13c-519fdca7dbdc",
                    "enabled": true,
                    "id": "017a84af-9e0b-615c-8610-eb762d9c2a3c",
                    "name": "20210708.4",
                    "url": "https://app.valohai.com/api/v0/deployment-versions/017a84af-9e0b-615c-8610-eb762d9c2a3c/"
                }
            ]
        },
        "endpoint": {
            "cpu_request": 0.1,
            "enabled": true,
            "endpoint_url": "https://valohai.cloud/sample/deployment-metadata/test/VERSION/digits",
            "files": [
                {
                    "datum": {
                        "aliases": [],
                        "ctime": "2021-07-08T05:37:03.571241Z",
                        "file_ctime": null,
                        "file_mtime": null,
                        "id": "017a849e-9652-e750-d4af-ee173561bffd",
                        "md5": null,
                        "name": "test.txt",
                        "output_execution": null,
                        "project": {
                            "ctime": "2021-07-08T05:36:28.772504Z",
                            "description": "",
                            "enabled_endpoint_count": null,
                            "execution_count": null,
                            "id": "017a849e-0e64-8a79-c338-6eb6878f6c8c",
                            "last_execution_ctime": null,
                            "mtime": "2021-07-08T05:36:28.772529Z",
                            "name": "deployment-metadata",
                            "owner": {
                                "id": 123,
                                "username": "sample"
                            },
                            "queued_execution_count": null,
                            "running_execution_count": null,
                            "url": "https://app.valohai.com/api/v0/projects/017a849e-0e64-8a79-c338-6eb6878f6c8c/",
                            "urls": {
                                "display": "https://app.valohai.com/p/sample/deployment-metadata/",
                                "display_repository": "https://app.valohai.com/p/sample/deployment-metadata/settings/repository/"
                            }
                        },
                        "purged": false,
                        "sha1": null,
                        "sha256": null,
                        "size": 5,
                        "store": "015e516a-2a89-ad95-38b9-cae527cde9a8",
                        "tags": [],
                        "uri": null
                    },
                    "id": "017a84af-9e15-eabf-6467-1d5f9bd28f5c",
                    "name": "model"
                }
            ],
            "id": "017a84af-9e0e-e57b-1438-ae078807e080",
            "is_ready_to_deploy": false,
            "memory_limit": 0,
            "memory_request": 0,
            "name": "digits",
            "node_selector": "",
            "status": "BUILDING_IMAGE",
            "status_detail": null,
            "url": "https://app.valohai.com/api/v0/deployment-endpoints/017a84af-9e0e-e57b-1438-ae078807e080/",
            "version": "017a84af-9e0b-615c-8610-eb762d9c2a3c"
        },
        "meta": {
            "ctime": "2021-07-08T05:55:39.863204+00:00"
        },
        "project": {
            "ctime": "2021-07-08T05:36:28.772504Z",
            "default_environment": null,
            "default_store": null,
            "description": "",
            "enabled_endpoint_count": null,
            "environment_variables": {},
            "execution_count": null,
            "execution_summary": {
                "complete_count": 0,
                "count": 6,
                "created_count": 0,
                "error_count": 0,
                "queued_count": 6,
                "started_count": 0,
                "stopped_count": 0,
                "stopping_count": 0,
                "stopping_hard_count": 0
            },
            "id": "017a849e-0e64-8a79-c338-6eb6878f6c8c",
            "last_execution_ctime": null,
            "mtime": "2021-07-08T05:36:28.772529Z",
            "name": "deployment-metadata",
            "owner": {
                "id": 123,
                "username": "sample"
            },
            "queued_execution_count": null,
            "read_only": false,
            "repository": {
                "ref": "master, main",
                "url": ""
            },
            "running_execution_count": null,
            "tags": [],
            "upload_store_id": "015e516a-2a89-ad95-38b9-cae527cde9a8",
            "url": "https://app.valohai.com/api/v0/projects/017a849e-0e64-8a79-c338-6eb6878f6c8c/",
            "urls": {
                "display": "https://app.valohai.com/p/sample/deployment-metadata/",
                "display_repository": "https://app.valohai.com/p/sample/deployment-metadata/settings/repository/"
            }
        },
        "version": {
            "commit": {
                "adhoc": true,
                "commit_time": "2021-07-08T05:55:30.227325Z",
                "description": "",
                "has_config": true,
                "identifier": "~ec89eff575ae08aee6bd6fdb207e04e814b309c226af058891f9b4c6d1416df1",
                "ref": "adhoc",
                "urls": {
                    "display": "https://app.valohai.com/p/sample/deployment-metadata/commits/~ec89eff575ae08aee6bd6fdb207e04e814b309c226af058891f9b4c6d1416df1/"
                }
            },
            "creator": {
                "id": 123,
                "username": "sample"
            },
            "ctime": "2021-07-08T05:55:39.659645Z",
            "deployment": "017a849e-5fa7-9a95-a13c-519fdca7dbdc",
            "enabled": true,
            "endpoint_urls": {
                "digits": "https://valohai.cloud/sample/deployment-metadata/test/20210708.4/digits"
            },
            "endpoints": [
                {
                    "cpu_request": 0.1,
                    "enabled": true,
                    "endpoint_url": "https://valohai.cloud/sample/deployment-metadata/test/VERSION/digits",
                    "files": [
                        {
                            "datum": {
                                "ctime": "2021-07-08T05:37:03.571241Z",
                                "file_ctime": null,
                                "file_mtime": null,
                                "id": "017a849e-9652-e750-d4af-ee173561bffd",
                                "md5": null,
                                "name": "test.txt",
                                "output_execution": null,
                                "project": "017a849e-0e64-8a79-c338-6eb6878f6c8c",
                                "purged": false,
                                "sha1": null,
                                "sha256": null,
                                "size": 5,
                                "store": "015e516a-2a89-ad95-38b9-cae527cde9a8",
                                "tags": []
                            },
                            "id": "017a84af-9e15-eabf-6467-1d5f9bd28f5c",
                            "name": "model"
                        }
                    ],
                    "id": "017a84af-9e0e-e57b-1438-ae078807e080",
                    "is_ready_to_deploy": false,
                    "memory_limit": 0,
                    "memory_request": 0,
                    "name": "digits",
                    "node_selector": "",
                    "status": "BUILDING_IMAGE",
                    "status_detail": null,
                    "url": "https://app.valohai.com/api/v0/deployment-endpoints/017a84af-9e0e-e57b-1438-ae078807e080/",
                    "version": "017a84af-9e0b-615c-8610-eb762d9c2a3c"
                }
            ],
            "environment_variables": {},
            "id": "017a84af-9e0b-615c-8610-eb762d9c2a3c",
            "mtime": "2021-07-08T05:55:39.659665Z",
            "name": "20210708.4",
            "url": "https://app.valohai.com/api/v0/deployment-versions/017a84af-9e0b-615c-8610-eb762d9c2a3c/"
        }
    }

..
