from tilemap import *
import output
import scripts.default
import omg

til = Tilemap(30,20)
print (til.get_size())
scripts.default.run(til)
output.to_print(til)

wad = omg.WAD()
wad.maps["MAP01"] = output.to_map(til)
wad.to_file("C:/Users/JMickle/Dropbox/Projects/Python/shit.wad")