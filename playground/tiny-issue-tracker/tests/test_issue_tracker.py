import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from issue_tracker import IssueTracker


class IssueTrackerTest(unittest.TestCase):
    def test_create_strips_title_and_assigns_ids(self):
        tracker = IssueTracker()

        first = tracker.create("  Fix login  ")
        second = tracker.create("Add export")

        self.assertEqual(first.id, 1)
        self.assertEqual(second.id, 2)
        self.assertEqual(first.title, "Fix login")
        self.assertEqual(first.status, "open")

    def test_search_is_case_insensitive(self):
        tracker = IssueTracker()
        tracker.create("Fix Login")
        tracker.create("Add CSV export")

        matches = tracker.search("login")

        self.assertEqual([issue.title for issue in matches], ["Fix Login"])

    def test_next_issue_uses_priority_order(self):
        tracker = IssueTracker()
        tracker.create("Nice polish", priority="low")
        tracker.create("Production outage", priority="critical")
        tracker.create("Small bug", priority="high")

        self.assertEqual(tracker.next_issue().title, "Production outage")

    def test_closed_issues_are_not_next(self):
        tracker = IssueTracker()
        outage = tracker.create("Production outage", priority="critical")
        tracker.create("Small bug", priority="high")

        tracker.close(outage.id)

        self.assertEqual(tracker.next_issue().title, "Small bug")


if __name__ == "__main__":
    unittest.main()
