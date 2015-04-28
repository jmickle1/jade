from tilemap import *
import output
import scripts.bronze_base as script
import omg
import sys
import time
import math

print("-------------")
print("Jade")
print("   by jmickle")
print("-------------")
print("")
print("")
start_time = time.clock()
if (len(sys.argv) < 2):
	#print("Usage: jade.py output_path [config_path]")
	til = script.run()
	print("Generated in "+str(math.floor(100*(time.clock() - start_time))/100)+" seconds.")
	output_path = "c:/users/jmickle/documents/bronze.wad"
	print("Exporting to "+output_path)
	output.to_file(til,output_path,"ZENNODE")
	
else:
	output_path = sys.argv[1]
	if (len(sys.argv) > 2): config_path = sys.argv[2]
	til = scripts.cavey.run()
	output.to_file(til,output_path)
print("Jade completed in "+str(math.floor(100*(time.clock() - start_time))/100)+" seconds.")