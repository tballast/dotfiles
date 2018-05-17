#!/usr/bin/python2.7

import argparse
import i3
import pprint
import sys
from time import sleep

def mv_workspace(new_ws):
	# retrieve only active outputs
	outputs = filter(lambda output: output['active'], i3.get_outputs())

	workspace_names = [w['name'] for w in i3.get_workspaces()]
	pprint.pprint(i3.get_workspaces())

	visible_workspaces = [w['name'] for w in i3.get_workspaces() if w['visible'] == True]
	current_ws = [w['name'] for w in i3.get_workspaces() if w['focused'] == True][0]
	temp_name = 'temporary'
	cmds = []

	print "Moving ", current_ws, " to ", new_ws

	if new_ws in workspace_names:
		
		# Exit if it's the same workspace
		if new_ws == current_ws:
			return

		cmds.append(rename_a_to_b(current_ws, temp_name))
		cmds.append(rename_a_to_b(new_ws, current_ws))	
	cmds.append(rename_a_to_b(temp_name, new_ws))
		
	else:
		cmds.append(rename_a_to_b(current_ws, new_ws))

	print cmds

	# for i in cmds:
	# 	print i
	# 	sleep(5)
	# 	i3.command(i)

	# [i3.command(cmd) for cmd in cmds]


def rename_a_to_b(a, b):
	return 'rename workspace ' + str(a) + ' to ' + str(b)

if __name__ == '__main__':
		

	parser = argparse.ArgumentParser(description='Workspace you wish to swap with')
	parser.add_argument('ws', metavar='W', type=str, nargs=1,
	                    help='The workspace to swap with')
	
	args = parser.parse_args()
	
	try:
		ws = args.ws[0]
	except IndexError:
		print "Give me a workspace you shit"
		sys.exit(1)

	mv_workspace(ws)
