'''easiest working solution to include the import path from calc without __init__.py as the project is structured in different directories'''
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

import unittest
from src import calc
import io

class testCalc(unittest.TestCase):
    
    def test_add(self):
        
        self.assertEqual(calc.add(10, 5,), 15)
        self.assertEqual(calc.add(-1, 1,), 0)
        self.assertEqual(calc.add(-1, -1,), -2)
        
    def test_substract(self):
        
        self.assertEqual(calc.substract(10, 5,), 5)
        self.assertEqual(calc.substract(-1, 1,), -2)
        self.assertEqual(calc.substract(-1, -1,), 0)
        
    def test_multiply(self):
        
        self.assertEqual(calc.multiply(10, 5,), 50)
        self.assertEqual(calc.multiply(-1, 1,), -1)
        self.assertEqual(calc.multiply(-1, -1,), 1)
        
    def test_divide(self):
        
        self.assertEqual(calc.divide(10, 5,), 2)
        self.assertEqual(calc.divide(-1, 1,), -1)
        self.assertEqual(calc.divide(-1, -1,), 1)
        

        
if __name__ == '__main__':
    out = io.BytesIO()
    print(out)
    with open('TEST-report.xml', 'wb') as report:
        report.write(out.getvalue())
    print(report)

    unittest.main()