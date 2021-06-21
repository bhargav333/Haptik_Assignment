import requests
from q3_can_create import CanCreate
import pytest

@pytest.fixture()
def example_input():
	return ["back", "end", "front", "tree"],"endtree"
def test_can_create(example_input):
	input,output = example_input
	test = CanCreate(input,output)
	out = test.can_create()
	assert out == True