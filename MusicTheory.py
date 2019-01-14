scale = input('Which scale do you want to get info on?')

scale = scale.upper()

type = 'undefined'
type = input('[M]ajor/mi[n]or: ')

if type == 'undefined':
	type = 'major'
elif type.lower() != 'major':
	type = 'major'
elif type.lower() != 'minor':
	type = 'major'

allnotes = {1:'A', 2: 'A#/Bb', 3: 'B', 4: 'C', 5: 'C#', 6: 'D', 7: 'D#/Eb', 8: 'E', 9: 'F', 10: 'F#', 11: 'G', 12: 'G#', 13:'A', 14: 'A#/Bb', 15: 'B', 16: 'C', 17: 'C#', 18: 'D', 19: 'D#/Eb', 20: 'E', 21: 'F', 22: 'F#', 23: 'G', 24: 'G#'}

def findnote(scale):
	for note in allnotes:
		if allnotes[note] == scale:
			notePos = note
			return (notePos)
			break
		
def chord(note):
	firstN = findnote(note)
	print('Notes to play', note, 'chord:', allnotes[firstN], allnotes[firstN+4], allnotes[firstN+7])

first = findnote(scale)

#print('Scale starts with position', first)

print('Notes in', type, 'scale of', scale, 'are:', allnotes[first], allnotes[first+2], allnotes[first+4], allnotes[first+5], allnotes[first+7], allnotes[first+9], allnotes[first+11])

print('Common triad used for this scale is:', allnotes[first], allnotes[first+5], allnotes[first+7])

#print('Notes to play', scale, 'chord:', allnotes[first], allnotes[first+4], allnotes[first+5])


chord(allnotes[first])

findnote(allnotes[first+5])

chord(allnotes[first+5])

findnote(allnotes[first+7])

chord(allnotes[first+7])