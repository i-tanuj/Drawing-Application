import cx_Oracle
class Model:
    def __init__(self):
        self.song_dict={}
        self.db_status=True
        self.conn=None
        self.cur=None
        try:
            self.conn=cx_Oracle.connect("mouzikka/music@127.0.0.1/xe")
            print("Connection opened")
            self.cur=self.conn.cursor()
            print("Cursor opened")
        except cx_Oracle.DatabasaeError as ex:
            print("DB Error:",ex)
            self.db_status=False

    def get_db_status(self):
        return self.db_status

    def close_db_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("Cursor closed")
        if self.conn is not None:
            self.conn.close()
            print("Connection closed")

    def add_song(self,song_name,song_path):
        self.song_dict[song.name]=song_path
        print("Song added:",song_name)

    def get_song_path(self,song_name):
        return self.song_dict[song_name]

    def remove_song(self,song_name):
        self.song_dict.pop(song_name)
        print("song removed:",song_name)

obj=Model()
obj.close_db_connection()