from playsound import playsound
# playsound('sample-6s.mp3')
print("no. of avialble songs\n1.sample-6s\n2.sample-9s\n3.sample-12s")
order=input('enter the music which you want to play')
if "sample-6s" in order:
 playsound('sample-6s.mp3')
elif "sample-9s" in order:
 playsound('sample-9s.mp3')
elif "sample-12s" in order:
 playsound('sample-12s.mp3')