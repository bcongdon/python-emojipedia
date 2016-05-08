from emojipedia import Emojipedia

face_with_tears = Emojipedia.search('face-with-tears-of-joy')

print face_with_tears.title # Title

print face_with_tears.description # Description

print face_with_tears.aliases # Aliases

print [x['title'] for x in face_with_tears.platforms] # Prints the titles of available platforms
