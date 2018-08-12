from hsaudiotag import auto
from hsaudiotag.id3v2 import Id3v2
ftags=auto.File("/home/sander/Muziek/1982 - Eye in the Sky (2007 RM, Expanded Edition, Arista 82876815272)/01. Sirius.mp3")
#ftags=auto.File("/home/sander/Muziek/Beauty and the Beast/1-01 Overture.m4a")
#print(ftags.track)
#ftags.image.show()

#ftags = Id3v2(None)
print(ftags.musicbrainz_release_id)
print(ftags.musicbrainz_artist_id)
print(ftags.musicbrainz_recording_id)
print(ftags.musicbrainz_album_artist_id)
print(ftags.musicbrainz_release_group_id)
print(ftags.musicbrainz_track_id)
print(ftags.musicbrainz_work_id)
print(ftags.part_of_set)