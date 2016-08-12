# coding=utf-8

import json
import requests
import unittest
from requests.auth import HTTPBasicAuth


class JenkinsGetTestCase(unittest.TestCase):
    def setUp(self):
        self.r = requests.get('http://192.168.217.130:8080/jenkins/api/json?tree=jobs[name]')

    def test_getAllJobsName(self):
        result = self.r.text
        json_result = json.loads(result)
        print json_result

        self.assertEqual(json_result['jobs'][0]['name'], 'check_python_version')

    def test_getAllJobsNameSimple(self):
        json_result = self.r.json()
        self.assertEqual(json_result['jobs'][0]['name'], 'check_python_version')

    # 测试开启鉴权的接口-禁用某个job

if __name__ == '__main__':
    unittest.main()
