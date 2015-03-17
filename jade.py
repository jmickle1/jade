from tilemap import *
import output
import toolbox.digger

til = Tilemap(30,20)

print (til.get_size())

toolbox.digger.dig(til,"#",15,10)
toolbox.digger.dig(til,"#",15,10)
toolbox.digger.dig(til,"#",15,10)

output.to_print(til)