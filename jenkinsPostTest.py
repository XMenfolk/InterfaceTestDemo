# coding=utf-8

import unittest
import requests
import json
from requests.auth import HTTPBasicAuth


class JenkinsPostTest(unittest.TestCase):
    def setUp(self):
        # 构建job的url
        self.build_job_url = 'http://192.168.217.130:8080/jenkins/job/check_python_version/build'
        # 禁用job的url
        self.disable_job_url = 'http://192.168.217.130:8080/jenkins/job/check_python_version/disable'
        # 获取job状态等信息的rul
        self.job_url = 'http://192.168.217.130:8080/jenkins/job/check_python_version/api/json'

    # 测试构建某一job接口
    def test_buildJob(self):
        r = requests.post(self.build_job_url, data=None, auth=('admin', 'admin'))
        print r.status_code
        self.assertEqual(r.status_code, 201)

    # 测试禁用某一job接口
    def test_disableJob(self):
        # 确认job状态是否可执行，'buildable':'true'
        status = self.get_JobInfo()
        self.assertTrue(status)

        # 禁用job，断言禁用job是否成功
        r = requests.post(self.disable_job_url, data=None, auth=('admin', 'admin'))
        self.assertEqual(r.status_code, 200)

        # 获取当前job状态
        status = self.get_JobInfo()
        self.assertFalse(status)
        print status

    # 获取当前job信息
    def get_JobInfo(self):
        job_info = requests.get(self.job_url, auth=('admin', 'admin')).json()
        return job_info['buildable']