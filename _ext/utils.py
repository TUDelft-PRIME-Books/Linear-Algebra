import enum
from typing import Optional


def generate_style(height: Optional[str], width: Optional[str]):
	'''
	Given a height and width, generates an inline style that can be used in HTML.
	'''

	styles = ''

	if height:
		styles += f'height: {height};'

	if width:
		styles += f'width: {width};'

	return styles


def parse_value(val: str) -> str:
	'''
	Parses a string value to a string that can be used in a URL query parameter. This is a hacky way to use boolean in docutils.
	(For some reason docutils can't parse 'true' or 'True' strings??)
	'''

	if val == 'enabled':
		return 'true'
	elif val == 'disabled':
		return 'false'
	else:
		return str(val)


def parse_options(options: dict) -> dict:
	# Settings keys that are passed along to the applet iframe
	applet_keys = ['title', 'background', 'autoPlay', 'position', 'isPerspectiveCamera', 'enablePan', 'distance', 'zoom']

	return {key: parse_value(val) for key, val in options.items() if key in applet_keys and val != ''}
