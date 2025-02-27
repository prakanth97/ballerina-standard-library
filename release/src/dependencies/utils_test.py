from sys import modules
import unittest

import utils

IO_MODULE = "module-ballerina-io"
JAVA_ARRAYS_MODULE = "module-ballerina-jballerina.java.arrays"

class TestDashboardCreation(unittest.TestCase):
    def test_get_module_short_name(self):
        expected = "java.arrays"
        actual = utils.get_module_short_name(JAVA_ARRAYS_MODULE)
        self.assertEqual(expected, actual)

        expected = "io"
        actual = utils.get_module_short_name(IO_MODULE)
        self.assertEqual(expected, actual)


    def test_get_repo_link(self):
        expected = "[io](https://github.com/ballerina-platform/module-ballerina-io)"
        actual = utils.get_repo_link(IO_MODULE)
        self.assertEqual(expected, actual)


    def test_get_release_badge(self):
        expected = "[![GitHub Release](https://img.shields.io/github/v/release/ballerina-platform/module-ballerina-io?sort=semver&color=30c955&label=)](https://github.com/ballerina-platform/module-ballerina-io/releases)"
        actual = utils.get_release_badge(IO_MODULE)
        self.assertEqual(expected, actual)

    def test_get_build_status_badge(self):
        expected = "[![Build](https://img.shields.io/github/workflow/status/ballerina-platform/module-ballerina-io/Build?label=)](https://github.com/ballerina-platform/module-ballerina-io/actions/workflows/build-timestamped-master.yml)"
        actual = utils.get_build_status_badge(IO_MODULE)
        self.assertEqual(expected, actual)


    def test_get_trivy_badge(self):
        expected = "[![Trivy](https://img.shields.io/github/workflow/status/ballerina-platform/module-ballerina-io/Trivy?label=)](https://github.com/ballerina-platform/module-ballerina-io/actions/workflows/trivy-scan.yml)"
        actual = utils.get_trivy_badge(IO_MODULE)
        self.assertEqual(expected, actual)


    def test_get_codecov_badge(self):
        expected = "[![CodeCov](https://codecov.io/gh/ballerina-platform/module-ballerina-io/branch/master/graph/badge.svg)](https://codecov.io/gh/ballerina-platform/module-ballerina-io)"
        actual = utils.get_codecov_badge(IO_MODULE, "master")
        self.assertEqual(expected, actual)


    def test_get_bugs_badge(self):
        expected = "[![Bugs](https://img.shields.io/github/issues-search/ballerina-platform/ballerina-standard-library?query=is%3Aopen+label%3Amodule%2Fjava.arrays+label%3AType%2FBug&label=&color=30c955)](https://github.com/ballerina-platform/ballerina-standard-library/issues?q=is%3Aopen+label%3Amodule%2Fjava.arrays+label%3AType%2FBug)"
        actual = utils.get_bugs_badge(JAVA_ARRAYS_MODULE)
        self.assertEqual(expected, actual)


    def test_get_pull_requests_badge(self):
        expected = "[![GitHub Pull Requests](https://img.shields.io/github/issues-pr-raw/ballerina-platform/module-ballerina-io.svg?label=)](https://github.com/ballerina-platform/module-ballerina-io/pulls)"
        actual = utils.get_pull_requests_badge(IO_MODULE)
        self.assertEqual(expected, actual)


    def test_get_load_tests_badge(self):
        expected = "[![Load Tests](https://img.shields.io/github/workflow/status/ballerina-platform/module-ballerina-io/Process%20load%20test%20results?label=)](https://github.com/ballerina-platform/module-ballerina-io/actions/workflows/process-load-test-result.yml)"
        actual = utils.get_load_tests_badge(IO_MODULE)
        self.assertEqual(expected, actual)
        expected = "[![Load Tests](https://img.shields.io/badge/-N%2FA-yellow)](https://github.com/ballerina-platform/module-ballerina-jballerina.java.arrays/actions/workflows/process-load-test-result.yml)"
        actual = utils.get_load_tests_badge(JAVA_ARRAYS_MODULE)
        self.assertEqual(expected, actual)

    def test_get_row_without_level(self):
        module = { "name": JAVA_ARRAYS_MODULE, "default_branch": "master"}
        expected = "||[java.arrays](https://github.com/ballerina-platform/module-ballerina-jballerina.java.arrays)|[![GitHub Release](https://img.shields.io/github/v/release/ballerina-platform/module-ballerina-jballerina.java.arrays?sort=semver&color=30c955&label=)](https://github.com/ballerina-platform/module-ballerina-jballerina.java.arrays/releases)|[![Build](https://img.shields.io/github/workflow/status/ballerina-platform/module-ballerina-jballerina.java.arrays/Build?label=)](https://github.com/ballerina-platform/module-ballerina-jballerina.java.arrays/actions/workflows/build-timestamped-master.yml)|[![Trivy](https://img.shields.io/github/workflow/status/ballerina-platform/module-ballerina-jballerina.java.arrays/Trivy?label=)](https://github.com/ballerina-platform/module-ballerina-jballerina.java.arrays/actions/workflows/trivy-scan.yml)|[![CodeCov](https://codecov.io/gh/ballerina-platform/module-ballerina-jballerina.java.arrays/branch/master/graph/badge.svg)](https://codecov.io/gh/ballerina-platform/module-ballerina-jballerina.java.arrays)|[![Bugs](https://img.shields.io/github/issues-search/ballerina-platform/ballerina-standard-library?query=is%3Aopen+label%3Amodule%2Fjava.arrays+label%3AType%2FBug&label=&color=30c955)](https://github.com/ballerina-platform/ballerina-standard-library/issues?q=is%3Aopen+label%3Amodule%2Fjava.arrays+label%3AType%2FBug)|[![GitHub Pull Requests](https://img.shields.io/github/issues-pr-raw/ballerina-platform/module-ballerina-jballerina.java.arrays.svg?label=)](https://github.com/ballerina-platform/module-ballerina-jballerina.java.arrays/pulls)|[![Load Tests](https://img.shields.io/badge/-N%2FA-yellow)](https://github.com/ballerina-platform/module-ballerina-jballerina.java.arrays/actions/workflows/process-load-test-result.yml)|\n"
        actual = utils.get_dashboard_row(module, '')
        self.assertEqual(expected, actual)
