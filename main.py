import requests
import subprocess
import sys

def command_caller(MagnetLink, choice):
	cmd=[]
	cmd.append("webtorrent")
	cmd.append(MagnetLink)
	if choice==1:
		cmd.append("--vlc")
	elif choice==2:
		if sys.platform.startswith('linux'):
			subprocess.call(cmd)
	elif choice==3:
		cmd.append("--mpv")
	subprocess.call(cmd)
def main():
	name=input("Enter the movie name\t")
	url=f"https://api.sumanjay.cf/torrent/?query={name}"

	results=requests.get(url).json()
	index=1
	magnet=[]
	for result in results:
		if "movie" in result['type'].lower() and result["nsfw"]==False and (result["leecher"]-result["seeder"])<0:
			print(index,"....",result['name'],"....",result['size'])
			magnet.append(result['magnet'])
			index+=1
	choice = int(input("Enter movie index"))
	MagnetLink=magnet[choice-1]

	download=False

	StreamChoice=int(input("1 for stream on vlc \n 2 for Download \n 3 for stream on mpv"))
	if StreamChoice==1:
		download=False
	elif StreamChoice==2:
		download=True
	elif StreamChoice==3:
		download=False
	else:
		print("Wrong option choosen\nExiting.....")
		exit(1)
	command_caller(MagnetLink,StreamChoice)



main()