import os
import shutil
import unittest
from helpers import (
    replace_keys_with_mappings,
)

class TestReplaceKeysWithMappingsReports(unittest.TestCase):
    def setUp(self):
        self.results_dir = "test_results_dir"

    def tearDown(self):
        if os.path.exists(self.results_dir):
            shutil.rmtree(self.results_dir)

    def test_anchoreEnterpriseReports_enabled_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.enabled": True, # deprecated
        }
        expected_result = {}
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseReports_replicaCount_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.replicaCount": 2,
        }
        expected_result = {
            'reports': {
                'replicaCount': 2
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)


    def test_anchoreEnterpriseReports_resources_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.resources.limits.cpu": 1,
            "anchoreEnterpriseReports.resources.limits.memory": "4G",
            "anchoreEnterpriseReports.resources.requests.cpu": 1,
            "anchoreEnterpriseReports.resources.requests.memory": "1G"
        }
        expected_result = {
            'reports': {
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


    def test_anchoreEnterpriseReports_labels_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.labels.myLabel": "myValue",
            "anchoreEnterpriseReports.labels.myOtherLabel": "myOtherValue",
            "anchoreEnterpriseReports.labels.anotherLabel.with.a.dot": "qux"
        }
        expected_result = {
            'reports': {
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

    def test_anchoreEnterpriseReports_annotations_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.annotations.foo": "bar",
            "anchoreEnterpriseReports.annotations.bar": "baz",
            "anchoreEnterpriseReports.annotations.anotherLabel.with.a.dot": "qux"
        }
        expected_result = {
            'reports': {
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

    def test_anchoreEnterpriseReports_deploymentAnnotations_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.deploymentAnnotations.foo": "bar",
            "anchoreEnterpriseReports.deploymentAnnotations.bar": "baz",
            "anchoreEnterpriseReports.deploymentAnnotations.anotherLabel.with.a.dot": "qux"
        }
        expected_result = {
            'reports': {
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

    def test_anchoreEnterpriseReports_nodeSelector_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.nodeSelector.name": "foo",
            "anchoreEnterpriseReports.nodeSelector.value": "bar",
            "anchoreEnterpriseReports.nodeSelector.anotherLabel.with.a.dot": "baz"
        }
        expected_result = {
            'reports': {
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

    def test_anchoreEnterpriseReports_tolerations_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.tolerations": [
                {
                    "name": "foo",
                    "value": "bar"
                }
            ]
        }
        expected_result = {
            'reports': {
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

    def test_anchoreEnterpriseReports_affinity_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.affinity.name": "foo",
            "anchoreEnterpriseReports.affinity.value": "bar",
            "anchoreEnterpriseReports.affinity.anotherLabel.with.a.dot": "baz"
        }
        expected_result = {
            'reports': {
                'affinity':{
                    'name': 'foo',
                    'value': 'bar',
                    'anotherLabel.with.a.dot': 'baz'
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseReports_extraEnv_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.extraEnv": []
        }
        expected_result = {
            'reports': {
                'extraEnv': []
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseReports_serviceAccountName_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.serviceAccountName": ""
        }
        expected_result = {
            'reports': {
                'serviceAccountName': ""
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)


    def test_anchoreEnterpriseReports_service_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.service.name": "Null",
            "anchoreEnterpriseReports.service.type": "ClusterIP",
            "anchoreEnterpriseReports.service.apiPort": 8558,
            "anchoreEnterpriseReports.service.workerPort": 8778, # deprecated
            "anchoreEnterpriseReports.service.annotations": {},
            "anchoreEnterpriseReports.service.labels.foobar": "baz",
            "anchoreEnterpriseReports.service.labels.with.a.dot": "qux"
        }
        expected_result = {
            'reports': {
                'service': {
                    "name": "Null",
                    "type": "ClusterIP",
                    "port": 8558,
                    "annotations": {},
                    "labels": {
                        "foobar": "baz",
                        "with.a.dot": "qux"
                    }
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseReports_enableGraphiql_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.enableGraphiql": True
        }
        expected_result = {
            'anchoreConfig': {
                'reports': {
                    'enable_graphiql': True
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseReports_enableDataIngress_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.enableDataIngress": True
        }
        expected_result = {
            'anchoreConfig': {
                'reports_worker': {
                    'enable_data_ingress': True
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseReports_enableDataEgress_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.enableDataEgress": False
        }
        expected_result = {
            'anchoreConfig': {
                'reports_worker': {
                    'enable_data_egress': False
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseReports_dataEgressWindow_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.dataEgressWindow": 1
        }
        expected_result = {
            'anchoreConfig': {
                'reports_worker': {
                    'data_egress_window': 1
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseReports_dataRefreshMaxWorkers_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.dataRefreshMaxWorkers": 1
        }
        expected_result = {
            'anchoreConfig': {
                'reports_worker': {
                    'data_refresh_max_workers': 1
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseReports_dataLoadMaxWorkers_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.dataLoadMaxWorkers": 1
        }
        expected_result = {
            'anchoreConfig': {
                'reports_worker': {
                    'data_load_max_workers': 1
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)

    def test_anchoreEnterpriseReports_cycleTimers_value(self):
        dot_string_dict = {
            "anchoreEnterpriseReports.cycleTimers.reports_data_load": 600,
            "anchoreEnterpriseReports.cycleTimers.reports_data_refresh": 7200,
            "anchoreEnterpriseReports.cycleTimers.reports_metrics": 3600,
            "anchoreEnterpriseReports.cycleTimers.reports_data_egress": 600
        }
        expected_result = {
            'anchoreConfig': {
                'reports_worker': {
                    'cycle_timers': {
                        'reports_data_load': 600,
                        'reports_data_refresh': 7200,
                        'reports_metrics': 3600,
                        'reports_data_egress': 600
                    }
                }
            }
        }
        result = replace_keys_with_mappings(dot_string_dict, self.results_dir)
        self.assertEqual(result[0], expected_result)