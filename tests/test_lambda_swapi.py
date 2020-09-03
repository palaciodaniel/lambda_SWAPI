import pytest
from packages.lambda_swapi import lambda_swapi_func

class TestLambdaSwapiFunc(object):

	# Good arguments

	def test_lambda_correct_inputs(self):

		assert lambda_swapi_func("mace", "maul") == ['1. The Phantom Menace']

	# Special arguments

	def test_lambda_nomatches(self):

		assert lambda_swapi_func("han solo", "sebulba") == \
		"| RESULT | -> No matches were found."

	def test_lambda_nochar(self):
		assert lambda_swapi_func("luke", "iron man") == \
		"| RESULT | -> One or both characters weren't found on the database."

	# Bad arguments

	def test_lambda_emptyargs(self):
		with pytest.raises(SystemExit):
			assert lambda_swapi_func("", "")
