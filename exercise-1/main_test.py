import main

def test_hello_world():
  assert main.hello_world() == "Hello, world!"

def test_greet_with_no_name():
  assert main.greet() == "Hello, world!"

def test_greet_with_conventional_names():
  assert main.greet("Richard") == "Hello, Richard!"
  assert main.greet("Esme") == "Hello, Esme!"
  assert main.greet("Neill") == "Hello, Neill!"


def test_describe_number_positive_and_even():
  assert main.describe_number(2) == { 'is_positive': True, 'is_even': True }
  assert main.describe_number(12034) == { 'is_positive': True, 'is_even': True }

def test_describe_number_positive_and_not_even():
  assert main.describe_number(1) == { 'is_positive': True, 'is_even': False }
  assert main.describe_number(12035) == { 'is_positive': True, 'is_even': False }
  # Decimals are not even
  assert main.describe_number(1.20352) == { 'is_positive': True, 'is_even': False }

def test_describe_number_non_positive_and_even():
  assert main.describe_number(-2) == { 'is_positive': False, 'is_even': True }
  assert main.describe_number(-20422) == { 'is_positive': False, 'is_even': True }
  # Zero is not a positive number
  assert main.describe_number(0) == { 'is_positive': False, 'is_even': True }

def test_describe_number_non_positive_and_non_even():
  assert main.describe_number(-1) == { 'is_positive': False, 'is_even': False }
  assert main.describe_number(-20421) == { 'is_positive': False, 'is_even': False }
  assert main.describe_number(-0.8) == { 'is_positive': False, 'is_even': False }
