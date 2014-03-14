import unittest
import tempfile
import mass
import time


class MassTests(unittest.TestCase):
    """Tests for mass Module."""

    def setUp(self):
        """Create temporary files to modify for each test."""
        self.dir = tempfile.TemporaryDirectory()
        self.files = []
        for i in range(5):
            with open(self.dir.name + '/{:02d}.txt'.format(i), 'w') as f:
                f.write('AAAAAAAA\nAAAAAAA\n')
                self.files.append(f.name)

    def test_modify(self):
        """Changes the output for every file."""
        mass.modify(self.dir.name, '/*.txt', lambda x: x.replace('A', 'B'))
        for fname in self.files:
            with open(fname) as f:
                for line in f:
                    self.assertRegex(line, 'B+\n')

    def test_concat(self):
        """Concatenates all files into a new output file."""
        mass.concat(self.dir.name, '/*.txt', self.dir.name + '/output.txt')
        with open(self.dir.name + '/output.txt') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 10)
            for line in lines:
                self.assertRegex(line, 'A+\n')

    def test_func(self):
        """Runs function against every line."""
        def x(line, lines):
            lines.append(line + 'B')
        lines = []
        mass.func(self.dir.name, '/*.txt', x, [lines])
        self.assertEqual(len(lines), 10)
        for line in lines:
            self.assertRegex(line, 'A+\nB')
        for fname in self.files:
            with open(fname) as f:
                for line in f:
                    self.assertRegex(line, 'A+\n')

if __name__ == '__main__':
    unittest.main()
