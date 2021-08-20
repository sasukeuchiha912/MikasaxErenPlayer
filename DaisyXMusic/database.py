from DaisyXMusic import musicdb

try:
    eval(musicdb.get("MusicChats"))
except BaseException:
    musicdb.set("MusicChats", "[]")

def is_music(chat_id):
    list = eval(musicdb.get("MusicChats"))	
    if chat_id in list:
    	return True
    return False
	   
def set_music(chat_id):
    list = eval(musicdb.get("MusicChats"))
    if chat_id not in list:
    	list.append(chat_id)
    	musicdb.set("MusicChats", str(list))
    return 
	
def rem_music(chat_id):
	list = eval(musicdb.get("MusicChats"))
	if chat_id in list:
		list.remove(chat_id)
		musicdb.set("MusicChats", str(list))
	return 
