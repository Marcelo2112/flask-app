class Config:
    #protocolo: // usurario:password@host:puerto/basededatos
    SQLALCHEMY_DATABASE_URI = 'postgres://mcadenas:optativo123@35.224.193.212:5432/mcadenas'
    SQLALCHEMY_TRACK_MODIFICATIONS= False 
    SECRET = '12345'