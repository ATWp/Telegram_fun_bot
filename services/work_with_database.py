from config import DATA_PHRASES_PATH

def load_database():
    return list(open(DATA_PHRASES_PATH))