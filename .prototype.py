import os
brm="\33[36;1m";pth="\33[1;37m";

def banner():
	os.system('clear')
	print(f'''\33[34;1m
	     ░▀█▀░█▀█░█▀▀░▀█▀░█▀█░█░░░█▀█░█▀█░█▀▄░█▀▀░█▀▄
             ░░█░░█░█░▀▀█░░█░░█▀█░█░░░█░█░█▀█░█░█░█▀▀░█▀▄
             ░▀▀▀░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀
			  \33[30;47m    By Lusmaysh    \33[37;40m
''')

def menu():
	banner()
	print(f"{brm}This tools automatic downloading your target instagram media.")
	print(f"{brm}Type {pth}help {brm}to show the options")
	sss = input(f'{brm}\n>> {pth}')
	if sss == 'install':
		banner()
		print(f'{brm}Starting Download The Package{pth}')
		os.system('pip install instaloader')
	elif sss == 'list':
		os.system('nano .list.txt')
		menu()
	elif sss == 'help':
		banner()
		print(f'''{brm}
type anything options are available below :

options		information
{pth}–––––––		–––––––––––
{brm}help		{pth}Print this help and exit.
{brm}about		{pth}Show this tools information.
{brm}login		{pth}If you want to log into your account
{brm}start		{pth}Starting this tools, CTRL+c or CTRL+z to stop.
{brm}install		{pth}When you first use this tool,
		type install to download the materials needed
		to run this tool.
''')
	elif sss == 'about':
		banner()
		print(f'''
{brm}About
{pth}––––––

{brm}Name Tools		: {pth}Instaloader
{brm}Version			: {pth}1.0
{brm}Date Created		: {pth}5-April-2021
{brm}Author			: {pth}Lusmaysh
{brm}Thanks to		: {pth}Instaloader
{brm}Special Thanks		: {pth}Allah SWT
{brm}Info			: {pth}This tool for downloading instagram media,
			  It is very simple to use,
			  No login required,
			  And it mean this tool is very safe.
{brm}Note			: {pth}This script can die at any time,
			  don't blame the author.
{brm}Result			: {pth}To move file to internal memory,
			  ex : mv bjiryu /sdcard
''')
	elif sss == 'clear':
		banner()
		os.system('rm -rf ~/.config/instaloader')
		os.system('python main.py')
	elif sss == 'ig':
		banner()
		print(f"{brm}Profile  : {pth}bjiryu")
		print(f"{brm}Password : {pth}*********")
		a = input(f'{brm}Download For saved/stories/feed ? : {pth}')
		print(f"{brm}Getting Info from {pth}bjiryu")
		if a == 'saved' or a == 'stories' or a == 'feed':
			os.system(f'instaloader -l bjiryu -p Syamsul10022005 --no-compress-json --no-metadata-json --no-captions --no-video-thumbnails --no-resume :{a}')
		else:
			exit()
	elif sss == 'login':
		banner()
		log = input(f'{brm}Your Profile Name : {pth}')
		while len(log) == 0:
			print("\33[33mCan't be blank!")
			log = input(f'{brm}Your Profile Name : {pth}')
		pw = input(f'{brm}Password : {pth}')
		while len(pw) == 0:
			print("\33[33mCan't be blank!")
			pw = input(f'{brm}Password : {pth}')
		hh = input(f'{brm}Download For saved/stories/feed ? ({pth}h{brm}) : {pth}')
		while hh == '':
			print("\33[33mCan't be blank!")
			hh = input(f'{brm}Download For saved/stories/feed ? ({pth}h{brm}) : {pth}')
		while hh == 'h':
			print(f'''\33[31m======================================================================
{brm}Options		Information
{pth}–––––––		–––––––––––
{brm}(target)		{brm}Download post from target. (Ex target : bjiryu)
{brm}saved		{brm}Download the posts that you marked as saved.
{brm}stories		{brm}Download the stories of your followees.
{brm}feed		{brm}Download pictures from your feed.
\33[31m======================================================================''')
			hh = input(f'{brm}Download For saved/stories/feed ? ({pth}h{brm}) : {pth}')
			while hh == '':
				print("\33[33mCan't be blank!")
				hh = input(f'{brm}Download For saved/stories/feed ? ({pth}h{brm}) : {pth}')
		print(f"{brm}Getting Info.. {pth}")
		if hh == 'saved' or hh == 'stories' or hh == 'feed':
			os.system(f'instaloader -l {log} -p {pw} --no-compress-json --no-metadata-json --no-captions --no-video-thumbnails --no-resume :{hh}')
		else:
			os.system(f'instaloader -l {log} -p {pw} {hh} --no-compress-json --no-metadata-json --no-captions --no-video-thumbnails --no-resume --no-profile-pic')
	elif sss == 'start':
		banner()
		id = input(f'{brm}Target Username ({brm}Example : {pth}bjiryu{brm}) : {pth}')
		while len(id) == 0:
			print("\33[33mCan't be blank!")
			id = input(f'{brm}Target Username ({brm}Example : {pth}bjiryu{brm}) : {pth}')
		choice = input(f"{brm}Download For Photo/Video/All ? ({pth}h{brm}) : {pth}")
		while choice == '':
			print("\33[33mCan't be blank!")
			choice = input(f"{brm}Download For Photo/Video/All ? ({pth}h{brm}) : {pth}")
		while choice == 'h':
			print(f"""\33[31m======================================================================
{brm}Options		Information
{pth}–––––––		–––––––––––
{brm}pp		{brm}Download Target photo profile.
{brm}a		{brm}Download target media photo and video.
{brm}p		{brm}Download target media but only photos.
{brm}v		{brm}Download target media but only videos.
{brm}#		{brm}Download hashtag photo and video.
{brm}#p		{brm}Download hashtag but only photo.
{brm}#v		{brm}Download hashtag but only video.
\33[31m======================================================================""")
			choice = input(f"{brm}Download For Photo/Video/All ? ({pth}h{brm}) : {pth}")
			while choice == '':
				print("\33[33mCan't be blank!")
				choice = input(f"{brm}Download For Photo/Video/All ? ({pth}h{brm}) : {pth}")
		print(f"{brm}Getting Media From {pth}{id} ")
		print(f"{brm}Getting Info.. {pth}")
		if choice == 'p':
			 os.system(f"instaloader {id} --no-videos --no-profile-pic --no-compress-json --no-metadata-json --no-captions --no-video-thumbnails --no-resume")
		elif choice == 'v':
			os.system(f"instaloader {id} --no-pictures --no-video-thumbnails --no-profile-pic --no-compress-json --no-metadata-json --no-captions --no-resume")
		elif choice == 'a':
			os.system(f"instaloader {id} -post --no-compress-json --no-metadata-json --no-captions --no-video-thumbnails --no-resume --no-profile-pic")
		elif choice == 'pp':
			os.system(f"instaloader {id} --profile-pic-only --no-compress-json --no-metadata-json --no-captions")
		elif choice == '#':
			os.system(f'instaloader "#{id}" --no-compress-json --no-metadata-json --no-captions --no-profile-pic --no-video-thumbnails')
		elif choice == '#v':
			os.system(f'instaloader "#{id}" --no-compress-json --no-metadata-json --no-captions --no-profile-pic --no-pictures --no-video-thumbnails')
		elif choice == '#p':
			os.system(f'instaloader "#{id}" --no-compress-json --no-metadata-json --no-captions --no-profile-pic --no-videos --no-video-thumbnails')
		else:
			exit()
	else:
		exit()

if __name__=='__main__':
	banner()
	try:
		menu()
	except:
		pass
#	except (KeyboardInterrupt,EOFError):
#		print(f"Exit")
#	except requests.exceptions.ConnectionError:
#		print(f"Connection Error...")
