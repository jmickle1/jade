from tilemap import *
import output
import scripts.cavey
import omg
import sys

print("-------------")
print("jade")
print("   by jmickle")
print("-------------")
print("")
print("")
print(sys.argv)
if (len(sys.argv) < 2):
	print("Usage: jade.py output_path [config_path]")
else:
	output_path = sys.argv[1]
	if (len(sys.argv) > 2): config_path = sys.argv[2]
	til = scripts.cavey.run()
	output.to_file(til,output_path)