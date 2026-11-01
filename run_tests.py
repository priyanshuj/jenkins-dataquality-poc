import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape


class JUnitTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_cases = []


class JUnitTestRunner(unittest.TextTestRunner):
    resultclass = JUnitTestResult


class ReportingResult(JUnitTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        self.test_cases.append((test, "success", ""))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.test_cases.append((test, "failure", self._exc_info_to_string(err, test)))

    def addError(self, test, err):
        super().addError(test, err)
        self.test_cases.append((test, "error", self._exc_info_to_string(err, test)))


class ReportingRunner(unittest.TextTestRunner):
    resultclass = ReportingResult


suite = unittest.defaultTestLoader.discover(".", pattern="test_*.py")
result = ReportingRunner(verbosity=2).run(suite)

report_dir = Path("test-reports")
report_dir.mkdir(exist_ok=True)

root = ET.Element("testsuite", {
    "name": "DataQualityUnitTests",
    "tests": str(result.testsRun),
    "failures": str(len(result.failures)),
    "errors": str(len(result.errors)),
    "skipped": str(len(result.skipped)),
})

for test, status, details in result.test_cases:
    case = ET.SubElement(root, "testcase", {
        "classname": test.__class__.__module__ + "." + test.__class__.__name__,
        "name": test._testMethodName,
    })
    if status in ("failure", "error"):
        tag = "failure" if status == "failure" else "error"
        ET.SubElement(case, tag, {"message": status}).text = details

ET.ElementTree(root).write(
    report_dir / "junit.xml",
    encoding="utf-8",
    xml_declaration=True,
)

sys.exit(not result.wasSuccessful())
