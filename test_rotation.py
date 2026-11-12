import unittest

from rotation import Shift, simulate


class RotationTests(unittest.TestCase):
    shifts = [Shift(0, 60, "Alex", "Sam"), Shift(60, 120, "Sam", "Jo")]

    def test_ack_at_deadline_suppresses_escalation(self):
        self.assertEqual(simulate(self.shifts, 55, 5, 60),
                         [(55, "page", "Alex"), (60, "acknowledge", "Alex")])

    def test_late_ack_uses_incident_shift(self):
        self.assertEqual(simulate(self.shifts, 59, 5, 65),
                         [(59, "page", "Alex"), (64, "escalate", "Sam"),
                          (65, "acknowledge", "Sam")])

    def test_new_incident_at_handoff_uses_next_shift(self):
        self.assertEqual(simulate(self.shifts, 60, 5)[0], (60, "page", "Sam"))

    def test_missing_coverage_is_explicit(self):
        with self.assertRaisesRegex(ValueError, "no on-call coverage"):
            simulate(self.shifts, 120, 5)

    def test_overlapping_shifts_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            simulate(self.shifts + [Shift(59, 61, "Pat", "Lee")], 59, 5)


if __name__ == "__main__":
    unittest.main()
