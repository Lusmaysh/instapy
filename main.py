import os
G="\33[32;1m";B="\33[36;1m";

def Logo():
	os.system('clear')
	print(f"""\33[1;31m
          ▄▀▄     ▄▀▄
         ▄█░░▀▀▀▀▀░░█▄
     ▄▄  █░░░░░░░░░░░█  ▄▄
    █▄▄█ █░░█░░┬░░█░░█ █▄▄█{B}
╔════════════════════════════════════════╗
║{G} ♚ Project : 𝕋𝕖𝕣𝕞𝕦𝕩-𝕀𝔻𝕃™                {B}║
║{G} ♚ Author  : Lusmaysh                   {B}║
║{G} ♚ Github  : github.com/Lusmaysh        {B}║
║{G} ♚ Website : -                          {B}║
╠════════════════════════════════════════╝""")

def rerun(user,plus):
	os.system("clear")
	print(f"【•】𝕊𝕥𝕒𝕣𝕥𝕚𝕟𝕘 𝕋𝕙𝕖 ℙ𝕣𝕠𝕘𝕣𝕒𝕞{B}")
	os.system(f"instaloader {user} --no-compress-json --no-metadata-json --no-caption --no-resume {plus}")

def Main():
	Logo()
	option=input(f"""{B}╠═{G}▶ 1. Download Target Post
{B}╠═{G}▶ 2. Download Hastag Post
{B}╠═{G}▶ 3. Login
{B}╚═{G}▶【𝕊𝕖𝕝𝕖𝕔𝕥 𝕋𝕙𝕖 𝕆𝕡𝕥𝕚𝕠𝕟】➳ """)
	if option == "1":
		Logo()
		id=input(f"{B}╚═{G}▶【𝕀𝕟𝕡𝕦𝕥 𝕋𝕒𝕣𝕘𝕖𝕥 𝕌𝕤𝕖𝕣𝕟𝕒𝕞𝕖】➳ ")
		Logo()
		ops=input(f"""{B}╠═{G}▶ 1. Photo
{B}╠═{G}▶ 2. Video
{B}╠═{G}▶ 3. Photo Profile
{B}╠═{G}▶ 4. All
{B}╚═{G}▶【𝕊𝕖𝕝𝕖𝕔𝕥 𝕋𝕙𝕖 𝕆𝕡𝕥𝕚𝕠𝕟】➳ """)
		if ops == "1":
			rerun(id,"--no-videos --no-profile-pic --no-video-thumbnails")
		elif ops == "2":
			rerun(id,"--no-pictures --no-video-thumbnails --no-profile-pic")
		elif ops == "3":
			rerun(id,"--profile-pic-only")
		elif ops == "4":
			rerun(id,"-post --no-video-thumbnails --no-profile-pic")
		else:
			exit(os.system("clear"))
	elif option == "2":
		Logo()
		id=input(f"{B}╚═{G}▶【𝕀𝕟𝕡𝕦𝕥 𝕋𝕒𝕣𝕘𝕖𝕥 𝕌𝕤𝕖𝕣𝕟𝕒𝕞𝕖】➳ #")
		Logo()
		ops=input(f"""{B}╠═{G}▶ 1. Photo
{B}╠═{G}▶ 2. Video
{B}╠═{G}▶ 3. All
{B}╚═{G}▶【𝕊𝕖𝕝𝕖𝕔𝕥 𝕋𝕙𝕖 𝕆𝕡𝕥𝕚𝕠𝕟】➳ """)
		if ops == "1":
			rerun("\#"+id,"--no-videos --no-profile-pic --no-video-thumbnails")
		elif ops == "2":
			rerun("\#"+id,"--no-pictures --no-video-thumbnails --no-profile-pic")
		elif ops == "3":
			rerun("\#"+id,"-post --no-video-thumbnails --no-profile-pic")
		else:
			exit(os.system("clear"))
	elif option == "3":
		os.system("rm -rf ~/.config/instaloader")
		Logo()
		usr=input(f"{B}╚═{G}▶【𝕐𝕠𝕦𝕣 𝕌𝕤𝕖𝕣𝕟𝕒𝕞𝕖】➳ ")
		Logo()
		pw=input(f"""{B}╠═{G}▶【𝕐𝕠𝕦𝕣 𝕌𝕤𝕖𝕣𝕟𝕒𝕞𝕖】➳ {usr}
{B}╚═{G}▶【𝕐𝕠𝕦𝕣 ℙ𝕒𝕤𝕤𝕨𝕠𝕣𝕕】➳ """)
		Logo()
		ops=input(f"""{B}╠═{G}▶ 1. Saved
{B}╠═{G}▶ 2. Stories
{B}╠═{G}▶ 3. Feed
{B}╚═{G}▶【𝕊𝕖𝕝𝕖𝕔𝕥 𝕋𝕙𝕖 𝕆𝕡𝕥𝕚𝕠𝕟】➳ """)
		if ops == "1":
			rerun(f"-l {usr} -p {pw}","--no-video-thumbnails :saved")
		elif ops == "2":
			rerun(f"-l {usr} -p {pw}","--no-video-thumbnails :stories")
		elif ops == "3":
			rerun(f"-l {usr} -p {pw}","--no-video-thumbnails :feed")
		else:
			exit(os.system("clear"))
	else:
		exit(os.system("clear"))

if __name__=="__main__":
	Main()
