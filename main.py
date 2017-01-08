# This is a learning on recursion.
# Random strings were pre-generated using: https://www.random.org/strings/?mode=advanced

from collections import defaultdict
from random import randrange

RANDOM_ATTRS = ['hvoi', 'xyaj', 'uudh', 'dstt', 'tskg', 'syqt', 'ravg', 'gdcw', 'hwwc', 'afok', 'kgey', 'itog',
				'opwy', 'hzxv', 'miqc', 'kuhf', 'rtke', 'rkqg', 'vlhq', 'rsqx', 'bmsw', 'oytw', 'rggj', 'hfce',
				'davs', 'owip', 'rakq', 'mvcq', 'bhec', 'qtto', 'mgmd', 'inkj', 'saif', 'movj', 'lfky', 'qxpb',
				'vilz', 'gqfu', 'hura', 'dbyz', 'thfc', 'nily', 'rget', 'cufv', 'jrti', 'nqru', 'caws', 'uwwe',
				'qxwq', 'atrx']
RANDOM_VALS = ['qyumjm', 'urycjk', 'guppsz', 'xvdgif', 'ylgvkj', 'krzyai', 'gbaspm', 'gqftyg', 'sihsqs', 'imcyqq',
			   'snjpeg', 'bjczcs', 'rbxtwg', 'uimufk', 'xpdpyb', 'bgvajo', 'yawyoy', 'yurfgk', 'lgxulv', 'oymcqy',
			   'oihjyt', 'wvkqfc', 'drofrb', 'dfgixe', 'qkunhy', 'jdpiqc', 'zaaxnk', 'rdruqs', 'mhrbiy', 'ocftoa',
			   'yqlqzj', 'emefcb', 'txisrv', 'eztixh', 'ongpcc', 'xgwche', 'gcryxz', 'nvlazb', 'hohgoq', 'urtbgz',
			   'ryypro', 'atupmn', 'obzdhf', 'oertjf', 'rpaatm', 'ilmzkt', 'popjtp', 'evxhxy', 'lhquut', 'mwlfzy']
RANDOM_NAMES = ['FvKIDB', 'xoWKru', 'YEagKQ', 'LrQuww', 'UwsSrC', 'mzHeWZ', 'SGmuiD', 'thdvDH', 'JGPQdx', 'mtTOWR']

MAX_CHILDREN = 10


class Data(object):
	def __init__(self, name):
		self.children = []
		self.parent = None
		self.attributes = defaultdict()
		self.name = name


def build_complex_data(root_data=None, depth=2):
	if not root_data:
		root_data = Data('root')
	generate_depth_tree(root_data, depth)
	return root_data


def generate_depth_tree(node, depth):
	if depth < 0:
		return

	node.children = generate_children(node, randrange(0, MAX_CHILDREN))
	for ch in node.children:
		generate_depth_tree(ch, depth - 1)


def generate_children(root, max_range):
	children = []
	for i in range(max_range):
		name = RANDOM_NAMES[randrange(0, len(RANDOM_NAMES))]
		child = Data(name)
		child.parent = root
		child.attributes[RANDOM_ATTRS[randrange(0, len(RANDOM_ATTRS))]] = RANDOM_VALS[randrange(0, len(RANDOM_VALS))]
		children.append(child)
	return children


def get_by_attr_name(attr, data, found=None):
	if not found:
		found = []
	if attr in data.attributes.keys():
		found.append(data)
	if data.children:
		for ch in data.children:
			found = get_by_attr_name(attr, ch, found)
	return found


def get_by_attr_value(val, data, found=None):
	if not found:
		found = []
	for k, v in data.attributes.items():
		if v == val:
			found.append(data)
	if data.children:
		for ch in data.children:
			found = get_by_attr_value(val, ch, found)
	return found


def get_by_attr_and_value(attr, val, data, found=None):
	if not found:
		found = []
	for k, v in data.attributes.items():
		if k == attr and v == val:
			found.append(data)
	if data.children:
		for ch in data.children:
			found = get_by_attr_and_value(attr, val, ch, found)
	return found


def get_by_name(name, data, found=None):
	if not found:
		found = []
	if data.name == name:
		found.append(data)
	if data.children:
		for ch in data.children:
			found = get_by_name(name, ch, found)
	return found


def filter_name(name, items, found):
	for item in items:
		if item.name == name:
			found.append(item)
	return found


def find(data, name=None, attr=None, val=None, found=None):
	if not found:
		found = []
	if name and not attr and not val:
		found = get_by_name(name, data, found)
	elif attr and not name and not val:
		found = get_by_attr_name(attr, data, found)
	elif val and not name and not attr:
		found = get_by_attr_value(val, data, found)
	elif attr and val and not name:
		found = get_by_attr_and_value(attr, val, data, found)
	elif name and attr and not val:
		by_attr = get_by_attr_name(attr, data, found)
		found = filter_name(name, by_attr, found)
	elif name and val and not attr:
		by_val = get_by_attr_value(val, data, found)
		found = filter_name(name, by_val, found)
	elif name and attr and val:
		by_attr_val = get_by_attr_and_value(attr, val, data, found)
		for item in by_attr_val:
			if item.name == name:
				found.append(item)
	return found


def main():
	root = build_complex_data(depth=5)

	attr_obj = find(root, attr='hzxv')
	val_obj = find(root, val='emefcb')
	attr_val_obj = find(root, attr='mvcq', val='drofrb')
	name_obj = find(root, name='xoWKru')
	name_and_attr = find(root, name='xoWKru', attr='hzxv')
	name_and_val = find(root, name='xoWKru', val='drofrb')
	name_attr_val = find(root, name='xoWKru', attr='hzxv', val='atupmn')

	break_point = None  # used for setting break point in debug

if __name__ == '__main__':
	main()
