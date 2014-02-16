import unittest
import tempfile
import massmodify
import time


class MassmodifyTests(unittest.TestCase):
    """Tests for massmodify Module."""

    def setUp(self):
        """Create temporary files to modify for each test."""
        self.dir = tempfile.TemporaryDirectory()
        self.files = []
        for i in range(5):
            with open(self.dir.name + '/{:02d}.txt'.format(i), 'w') as f:
                f.write('AAAAAAAA\nAAAAAAA\n')
                self.files.append(f.name)

    def test_modify(self):
        """Test the modify function changes the output for every file."""
        massmodify.modify(self.dir.name, '/*.txt',
                          lambda x: x.replace('A', 'B'))
        for fname in self.files:
            with open(fname) as f:
                for line in f:
                    self.assertNotIn('A', line)

if __name__ == '__main__':
    unittest.main()
