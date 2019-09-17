import password_checker
import pytest

#password_is_valid tests
def test_password_exists():
	"""it should raise a suitable exception if the password does not exist"""
	with pytest.raises(Exception, match = 'password should exist'):
		password_checker.password_is_valid('')

def test_password_length():
	"""it should raise a suitable exception if the password is not longer than 8 characters"""
	with pytest.raises(Exception, match = 'password should be longer than 8 characters'):
		password_checker.password_is_valid('Aa34')

def test_password_has_lower():
	"""it should raise a suitable exception if the password does not contain a lowercase character"""
	with pytest.raises(Exception, match = 'password should contain a lowercase character'):
		password_checker.password_is_valid('A23456789')

def test_password_has_upper():
	"""it should raise a suitable exception if the password does not contain an uppercase character"""
	with pytest.raises(Exception, match = 'password should contain an uppercase character'):
		password_checker.password_is_valid('a23456789')

def test_password_has_digit():
	"""it sould raise a suitable exception if the password does not contain a digit"""
	with pytest.raises(Exception, match = 'password should contain a digit'):
		password_checker.password_is_valid('Aa_______')

#password_is_ok tests
def test_password_is_ok():
	"""it should return True if the given password meets at least 3 validation criteria, is longer than 8 characters and exists"""
	assert password_checker.password_is_ok('Aa3') == False
	assert password_checker.password_is_ok('A') == False
	assert password_checker.password_is_ok('') == False
	assert password_checker.password_is_ok('Aa345678') == False
	assert password_checker.password_is_ok('Aa3456789') == True