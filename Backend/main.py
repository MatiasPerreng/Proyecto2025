import json
from database import SessionLocal
import modelos

def row_to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

def main():
    db = SessionLocal()
    try:
        personas = db.query(modelos.Personal).all()
        data = [row_to_dict(p) for p in personas]

        return data   
    finally:
        db.close()

if __name__ == "__main__":
    resultado = main()
    print(json.dumps(resultado, ensure_ascii=False, indent=2, default=str))
