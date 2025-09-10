#!/usr/bin/env python3
"""
Test runner script for the Car Rental Project

This script runs all unit tests in the project using Python's built-in unittest module.
It provides detailed test results and coverage information.

Usage:
    python run_tests.py
    python run_tests.py -v  # Verbose output
    python run_tests.py --pattern "test_car*"  # Run specific test pattern
"""

import unittest
import sys
import os
import argparse
from io import StringIO

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)


def discover_and_run_tests(test_dir='tests', pattern='test_*.py', verbosity=2):
    """
    Discover and run all tests in the specified directory
    
    Args:
        test_dir (str): Directory containing test files
        pattern (str): Pattern to match test files
        verbosity (int): Test output verbosity level (0-2)
    
    Returns:
        bool: True if all tests passed, False otherwise
    """
    # Discover tests
    loader = unittest.TestLoader()
    start_dir = os.path.join(project_root, test_dir)
    
    if not os.path.exists(start_dir):
        print(f"Error: Test directory '{start_dir}' does not exist")
        return False
    
    suite = loader.discover(start_dir, pattern=pattern, top_level_dir=project_root)
    
    # Count total tests
    def count_tests(test_suite):
        count = 0
        for test in test_suite:
            if isinstance(test, unittest.TestSuite):
                count += count_tests(test)
            else:
                count += 1
        return count
    
    total_tests = count_tests(suite)
    print(f"Discovered {total_tests} tests")
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=verbosity, stream=sys.stdout)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped) if hasattr(result, 'skipped') else 0}")
    
    if result.failures:
        print(f"\nFAILED TESTS:")
        for test, trace in result.failures:
            print(f"  - {test}")
    
    if result.errors:
        print(f"\nERROR TESTS:")
        for test, trace in result.errors:
            print(f"  - {test}")
    
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100) if result.testsRun > 0 else 0
    print(f"\nSuccess Rate: {success_rate:.1f}%")
    
    return len(result.failures) == 0 and len(result.errors) == 0


def run_specific_test_file(test_file, verbosity=2):
    """
    Run tests from a specific test file
    
    Args:
        test_file (str): Path to the test file
        verbosity (int): Test output verbosity level
    
    Returns:
        bool: True if all tests passed, False otherwise
    """
    if not os.path.exists(test_file):
        print(f"Error: Test file '{test_file}' does not exist")
        return False
    
    # Load and run the specific test file
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(test_file), pattern=os.path.basename(test_file))
    
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    
    return len(result.failures) == 0 and len(result.errors) == 0


def main():
    """Main function to parse arguments and run tests"""
    parser = argparse.ArgumentParser(description='Run unit tests for Car Rental Project')
    parser.add_argument('-v', '--verbose', action='store_true', 
                       help='Increase output verbosity')
    parser.add_argument('-q', '--quiet', action='store_true',
                       help='Decrease output verbosity')
    parser.add_argument('--pattern', default='test_*.py',
                       help='Pattern to match test files (default: test_*.py)')
    parser.add_argument('--dir', default='tests',
                       help='Directory containing tests (default: tests)')
    parser.add_argument('--file', 
                       help='Run tests from a specific file')
    
    args = parser.parse_args()
    
    # Determine verbosity level
    if args.quiet:
        verbosity = 0
    elif args.verbose:
        verbosity = 2
    else:
        verbosity = 1
    
    print("Car Rental Project - Unit Test Runner")
    print("="*50)
    
    # Run tests
    if args.file:
        success = run_specific_test_file(args.file, verbosity)
    else:
        success = discover_and_run_tests(args.dir, args.pattern, verbosity)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()