import pymongo
 
#https://estudiantes.onrender.com/docs
MONGODB_URL = "mongodb+srv://danilo:uniminuto2024@cluster0.1wfcup2.mongodb.net/?retryWrites=true&w=majority"
#MONGODB_URL = "mongodb://danilo:password@localhost:27017/uniminuto?retryWrites=true&w=majority"

class BaseDeDatos():
    def __init__(self) -> None:
        self.connection_is_active = False
        self.engine = None

    def obtener_conexion(self):
        if self.connection_is_active == False:
            
            try:
                print(MONGODB_URL)
                self.engine = pymongo.MongoClient(MONGODB_URL)
                return self.engine
            except Exception as ex:
                print("Error connecting to MongoDB database : ", ex)
        return self.engine

    def obtener_sesion(self, engine):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            return session
        except Exception as ex:
            print("Error en la conexión a la base de datos : ", ex)
            return None
