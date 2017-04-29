from hsaudiotag import auto
import sys
tag = auto.File(sys.argv[1])
print(sys.argv[1])
print(tag.artist)
tag.image.show()