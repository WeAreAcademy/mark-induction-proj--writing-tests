from greet import greet

def test_greet_with_no_name():
  assert greet() == "Hello, world!"

def test_greet_with_conventional_names():
  assert greet("Richard") == "Hello, Richard!"
  assert greet("Esme") == "Hello, Esme!"
  assert greet("Neill") == "Hello, Neill!"