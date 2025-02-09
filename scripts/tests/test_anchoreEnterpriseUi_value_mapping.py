import os
import shutil
import unittest
from helpers import (
    replace_keys_with_mappings,
)

class TestReplaceKeysWithMappingsEnterpriseUi(unittest.TestCase):
    def setUp(self):
        self.results_dir = "test_results_dir"

    def tearDown(self):
        if os.path.exists(self.results_dir):
            shutil.rmtree(self.results_dir)

    def test_anchoreEnterpriseUi_enabled_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.enabled": True, # deprecated
        }
        expected_result = {}
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_image_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.image": "docker.io/anchore/enterprise-ui:v5.0.0",
            "anchoreEnterpriseUi.imagePullPolicy": "IfNotPresent"
        }
        expected_result = {
            'ui': {
                'image': "docker.io/anchore/enterprise-ui:v5.0.0",
                'imagePullPolicy': "IfNotPresent"
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_replicaCount_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.replicaCount": 2,
        }
        expected_result = {
            'ui': {
                'replicaCount': 2
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)


    def test_anchoreEnterpriseUi_resources_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.resources.limits.cpu": 1,
            "anchoreEnterpriseUi.resources.limits.memory": "4G",
            "anchoreEnterpriseUi.resources.requests.cpu": 1,
            "anchoreEnterpriseUi.resources.requests.memory": "1G"
        }
        expected_result = {
            'ui': {
                'resources': {
                    'limits': {
                        'cpu': 1,
                        'memory': '4G'
                    },
                    'requests': {
                        'cpu': 1,
                        'memory': '1G'
                    }
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)


    def test_anchoreEnterpriseUi_labels_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.labels.myLabel": "myValue",
            "anchoreEnterpriseUi.labels.myOtherLabel": "myOtherValue",
            "anchoreEnterpriseUi.labels.anotherLabel.with.a.dot": "qux"
        }
        expected_result = {
            'ui': {
                'labels':
                    {
                        'myLabel': 'myValue',
                        'myOtherLabel': 'myOtherValue',
                        'anotherLabel.with.a.dot': 'qux'
                    }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_annotations_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.annotations.foo": "bar",
            "anchoreEnterpriseUi.annotations.bar": "baz",
            "anchoreEnterpriseUi.annotations.anotherLabel.with.a.dot": "qux"
        }
        expected_result = {
            'ui': {
                'annotations':
                    {
                        'foo': 'bar',
                        'bar': 'baz',
                        'anotherLabel.with.a.dot': 'qux'
                    }

            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_deploymentAnnotations_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.deploymentAnnotations.foo": "bar",
            "anchoreEnterpriseUi.deploymentAnnotations.bar": "baz",
            "anchoreEnterpriseUi.deploymentAnnotations.anotherLabel.with.a.dot": "qux"
        }
        expected_result = {
            'ui': {
                'deploymentAnnotations':
                    {
                        'foo': 'bar',
                        'bar': 'baz',
                        'anotherLabel.with.a.dot': 'qux'
                    }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_nodeSelector_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.nodeSelector.name": "foo",
            "anchoreEnterpriseUi.nodeSelector.value": "bar",
            "anchoreEnterpriseUi.nodeSelector.anotherLabel.with.a.dot": "baz"
        }
        expected_result = {
            'ui': {
                'nodeSelector':
                    {
                        'name': 'foo',
                        'value': 'bar',
                        'anotherLabel.with.a.dot': 'baz'
                    }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_tolerations_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.tolerations": [
                {
                    "name": "foo",
                    "value": "bar"
                }
            ]
        }
        expected_result = {
            'ui': {
                'tolerations': [
                    {
                        'name': 'foo',
                        'value': 'bar'
                    }
                ]
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_affinity_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.affinity.name": "foo",
            "anchoreEnterpriseUi.affinity.value": "bar",
            "anchoreEnterpriseUi.affinity.anotherLabel.with.a.dot": "baz"
        }
        expected_result = {
            'ui': {
                'affinity':{
                    'name': 'foo',
                    'value': 'bar',
                    'anotherLabel.with.a.dot': 'baz'
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_extraEnv_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.extraEnv": [
                {
                    "name": "foo",
                    "value": "bar"
                },
                {
                    "a.bad.one.but.bring.over.anyways": False
                }
            ]
        }
        expected_result = {
            'ui': {
                'extraEnv': [
                    {
                        "name": "foo",
                        "value": "bar"
                    },
                    {
                        "a.bad.one.but.bring.over.anyways": False
                    }
                ]
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_serviceAccountName_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.serviceAccountName": "Null"
        }
        expected_result = {
            'ui': {
                'serviceAccountName': "Null"
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)


    def test_anchoreEnterpriseUi_service_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.service.name": "Null",
            "anchoreEnterpriseUi.service.type": "ClusterIP",
            "anchoreEnterpriseUi.service.port": 80,
            "anchoreEnterpriseUi.service.annotations.foo": "bar",
            "anchoreEnterpriseUi.service.annotations.baz": "qux",
            "anchoreEnterpriseUi.service.annotations.with.a.dot": "quux",
            "anchoreEnterpriseUi.service.labels": {},
            "anchoreEnterpriseUi.service.sessionAffinity": "ClientIP"
        }
        expected_result = {
            'ui': {
                'service': {
                    "name": "Null",
                    "type": "ClusterIP",
                    "port": 80,
                    "annotations": {
                        "foo": "bar",
                        "baz": "qux",
                        "with.a.dot": "quux"
                    },
                    "labels": {},
                    "sessionAffinity": "ClientIP"
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_db_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.dbUser": "anchoreengineui",
            "anchoreEnterpriseUi.dbPass": "anchore-postgres,123ui"
        }
        expected_result = {
            'ui': {
                'dbUser': "anchoreengineui",
                'dbPass': "anchore-postgres,123ui"
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_appDBConfig_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.appDBConfig.native": True,
            "anchoreEnterpriseUi.appDBConfig.pool.max": 10,
            "anchoreEnterpriseUi.appDBConfig.pool.min": 0,
            "anchoreEnterpriseUi.appDBConfig.pool.acquire": 30000,
            "anchoreEnterpriseUi.appDBConfig.pool.idle": 10000
        }
        expected_result = {
            'anchoreConfig': {
                'ui': {
                    'appdb_config': {
                        'native': True,
                        'pool': {
                            'max': 10,
                            'min': 0,
                            'acquire': 30000,
                            'idle': 10000
                        }
                    }
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_ldapsRootCaCertName_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.ldapsRootCaCertName": "Null"
        }
        expected_result = {
            'ui': {
                'ldapsRootCaCertName': "Null"
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_logLevel_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.logLevel": "http"
        }
        expected_result = {
            'anchoreConfig': {
                'ui': {
                    'log_level': "http"
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_enableProxy_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.enableProxy": False
        }
        expected_result = {
            'anchoreConfig': {
                'ui': {
                    'enable_proxy': False
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_enableSsl_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.enableSsl": False
        }
        expected_result = {
            'anchoreConfig': {
                'ui': {
                    'enable_ssl': False
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_enableSharedLogin_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.enableSharedLogin": True
        }
        expected_result = {
            'anchoreConfig': {
                'ui': {
                    'enable_shared_login': True
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_redisFlushdb_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.redisFlushdb": True
        }
        expected_result = {
            'anchoreConfig': {
                'ui': {
                    'redis_flushdb': True
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_forceWebsocket_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.forceWebsocket": False
        }
        expected_result = {
            'anchoreConfig': {
                'ui': {
                    'force_websocket': False
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_authenticationLock_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.authenticationLock.count": 5,
            "anchoreEnterpriseUi.authenticationLock.expires": 300
        }
        expected_result = {
            'anchoreConfig': {
                'ui': {
                    'authentication_lock': {
                        'count': 5,
                        'expires': 300
                    }
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_customLinks_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.customLinks.title": "Custom External Links",
            "anchoreEnterpriseUi.customLinks.links": [
                {
                    "title": "Example Link 1",
                    "uri": "https://example.com"
                },
                {
                    "title": "Example Link 2",
                    "uri": "https://example.com"
                }
            ]
        }
        expected_result = {
            'anchoreConfig': {
                'ui': {
                    'custom_links': {
                        'title': "Custom External Links",
                        'links': [
                            {
                                'title': "Example Link 1",
                                'uri': "https://example.com"
                            },
                            {
                                'title': "Example Link 2",
                                'uri': "https://example.com"
                            }
                        ]
                    }
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_enableAddRepositories_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.enableAddRepositories.admin": True,
            "anchoreEnterpriseUi.enableAddRepositories.standard": True
        }
        expected_result = {
            'anchoreConfig': {
                'ui': {
                    'enable_add_repositories': {
                        'admin': True,
                        'standard': True
                    }
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseUi_enrichInventoryView_value(self):
        dot_string_dict = {
            "anchoreEnterpriseUi.enrichInventoryView": True
        }
        expected_result = {
            'anchoreConfig': {
                'ui': {
                    'enrich_inventory_view': True
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_uiRedis_auth_password_value(self):
        dot_string_dict = {
            "ui-redis.auth.password": "anchore-redis,123"
        }
        expected_result = {
                'ui-redis': {
                    'auth': {
                        'password': "anchore-redis,123"
                    }
                }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_uiRedis_architecture_value(self):
        dot_string_dict = {
            "ui-redis.architecture": "standalone"
        }
        expected_result = {
                'ui-redis': {
                    'architecture': "standalone"
                }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_uiRedis_master_persistence_enabled_value(self):
        dot_string_dict = {
            "ui-redis.master.persistence.enabled": False
        }
        expected_result = {
                'ui-redis': {
                    'master': {
                        'persistence': {
                            'enabled': False
                        }
                    }
                }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_uiRedis_enabled_value(self):
        dot_string_dict = {
            "ui-redis.enabled": False
        }
        expected_result = {
                'ui-redis': {
                    'chartEnabled': False
                }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_uiRedis_externalEndpoint_value(self):
        dot_string_dict = {
            "ui-redis.externalEndpoint": "my-redis-place.someplace"
        }
        expected_result = {
                'ui-redis': {
                    'externalEndpoint': "my-redis-place.someplace"
                }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)