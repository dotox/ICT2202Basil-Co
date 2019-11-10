"""add trim option for excess word in cover"""
# -*- coding: utf-8 -*-
import codecs

def uniCode2(hfile):
	whitespace = {u'\u0020', u'\u00A0', u'\u1680', u'\u180E', u'\u2000', u'\u2001', u'\u2002', u'\u2003', u'\u2004',
				  u'\u2005',
				  u'\u2006', u'\u2007', u'\u2008', u'\u2009', u'\u200A', u'\u200B', u'\u202F', u'\u205F', u'\u3000',
				  u'\uFEFF'}
	hf = open(hfile, 'r', encoding="utf-8")
	hidden = hf.read().split(' ')
	hf.close()

	output= ""
	bits = ''
	for word in hidden:
		if word[0] in whitespace:
			bits += '0'
		elif word[-1] in whitespace:
			bits += '1'

		else:
			try:
				output += chr(int(bits, 2))
				bits = ''
			except ValueError:
				pass

	return output

