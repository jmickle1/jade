from tilemap import *
import output
import scripts.cavey
import omg

print("-------------")
print("jade")
print("   by jmickle")
print("-------------")
print("")
print("")

til = Tilemap(80,60)
print ("map size: "+str(til.get_size()))
scripts.cavey.run(til)
#output.to_print(til)

output.to_file(til,"C:/Users/JMickle/Documents/shit.wad")