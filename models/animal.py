class Animal(db.Model):
    __tablename__ = 'animais'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False) # peixe, abelha.. 

    # atributos fixos para cada tipo de animal
    temperatura_agua = db.Column(db.Float, nullable=True)  # peixes e abelhas
    ph = db.Column(db.Float, nullable=True)  # peixes
    umidade_ar = db.Column(db.Float, nullable=True)  # PANCS e abelhas
    temperatura_ar = db.Column(db.Float, nullable=True)  # abelhas
    nivel_agua = db.Column(db.Float, nullable=True)  # abelhas
    peso = db.Column(db.Float, nullable=True)  # vacas
    comportas = db.Column(db.String(50), nullable=True)  #  aberto, fechado (PANCS)