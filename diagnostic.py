import output
import scripts.bronze_base as script
import omg
import sys
import time
import math

def generate():
	start_time = time.clock()
	til = script.run()
	print("Generated in "+str(math.floor(100*(time.clock() - start_time))/100)+" seconds.")
	start_time = time.clock()
	output_path = "c:/users/jmickle/documents/diag.wad"
	print("Exporting to "+output_path)
	output.to_file(til,output_path,"ZENNODE")
	print("Exported in "+str(math.floor(100*(time.clock() - start_time))/100)+" seconds.")
	return math.floor(100*(time.clock() - start_time))/100

iterations = 10
total_time = 0
for x in range(iterations):
	total_time += generate()
	
	
print("---")
print("Average time: "+str(total_time/iterations)+" seconds")