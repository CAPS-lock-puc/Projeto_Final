from sqlalchemy import (
    create_engine, Column, Integer, String, Boolean, Float, ForeignKey, DateTime
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Tabela principal para dispositivos
class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    estado_ativacao = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)

# Tabela de gerenciadores
class Gerenciador(Base):
    __tablename__ = 'gerenciadores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)
    login = Column(String(50), unique=True, nullable=False)

# Generalização de gerenciadores: usuários e administradores
class Usuario(Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, ForeignKey('gerenciadores.id'), primary_key=True)

class Administrador(Base):
    __tablename__ = 'administradores'
    id_adm = Column(Integer, ForeignKey('gerenciadores.id'), primary_key=True)

# Sensores e Atuadores para Pancs
class SensorPanc(Base):
    __tablename__ = 'sensors_pancs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('devices.id'))
    unit = Column(String(50))
    topic = Column(String(50))
    temp = Column(Float)
    umidade = Column(Float)
    leitura_id = Column(Integer)
    unid_medida = Column(String(50))

class ActuatorPanc(Base):
    __tablename__ = 'actuators_pancs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('devices.id'))
    unit = Column(String(50))
    topic = Column(String(50))
    estado_liberado = Column(Boolean)
    unid_medida = Column(String(50))

class HistoricoPanc(Base):
    __tablename__ = 'historico_pancs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, nullable=False)
    sensor_pancs_id = Column(Integer, ForeignKey('sensors_pancs.id'), nullable=False)
    value = Column(Float, nullable=False)

# Sensores e Atuadores para Abelhas
class SensorAbelha(Base):
    __tablename__ = 'sensors_abelhas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('devices.id'))
    unit = Column(String(50))
    topic = Column(String(50))
    temp = Column(Float)
    nivel_agua = Column(Float)
    umidade_ar = Column(Float)
    leitura_id = Column(Integer)
    unid_medida = Column(String(50))

class ActuatorAbelha(Base):
    __tablename__ = 'actuators_abelhas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('devices.id'))
    unit = Column(String(50))
    topic = Column(String(50))
    estado_liberado = Column(Boolean)
    unid_medida = Column(String(50))

class HistoricoAbelha(Base):
    __tablename__ = 'historico_abelhas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, nullable=False)
    sensor_abelhas_id = Column(Integer, ForeignKey('sensors_abelhas.id'), nullable=False)
    value = Column(Float, nullable=False)

# Sensores e Atuadores para Vacas
class SensorVaca(Base):
    __tablename__ = 'sensors_vacas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('devices.id'))
    unit = Column(String(50))
    topic = Column(String(50))
    peso = Column(Float)
    leitura_id = Column(Integer)
    unid_medida = Column(String(50))

class ActuatorVaca(Base):
    __tablename__ = 'actuators_vacas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('devices.id'))
    unit = Column(String(50))
    topic = Column(String(50))
    estado_liberado = Column(Boolean)
    comportas = Column(Boolean)
    unid_medida = Column(String(50))

class HistoricoVaca(Base):
    __tablename__ = 'historico_vacas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, nullable=False)
    sensor_vacas_id = Column(Integer, ForeignKey('sensors_vacas.id'), nullable=False)
    value = Column(Float, nullable=False)

# Sensores e Atuadores para Peixes
class SensorPeixe(Base):
    __tablename__ = 'sensors_peixes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('devices.id'))
    unit = Column(String(50))
    topic = Column(String(50))
    ph = Column(Float)
    temp_agua = Column(Float)
    leitura_id = Column(Integer)
    unid_medida = Column(String(50))

class ActuatorPeixe(Base):
    __tablename__ = 'actuators_peixes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('devices.id'))
    unit = Column(String(50))
    topic = Column(String(50))
    estado_liberado = Column(Boolean)
    unid_medida = Column(String(50))

class HistoricoPeixe(Base):
    __tablename__ = 'historico_peixes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, nullable=False)
    sensor_peixes_id = Column(Integer, ForeignKey('sensors_peixes.id'), nullable=False)
    value = Column(Float, nullable=False)

# Configurando a conexão e sessão
engine = create_engine('mysql+pymysql://user:password@localhost/db_name')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Métodos genéricos para CRUD
def add_entry(entry):
    session.add(entry)
    session.commit()

def get_all_entries(model):
    return session.query(model).all()

def get_entry_by_id(model, entry_id):
    return session.query(model).filter_by(id=entry_id).first()

def delete_entry(entry):
    session.delete(entry)
    session.commit()
