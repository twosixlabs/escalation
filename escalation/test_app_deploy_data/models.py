# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class DataUploadMetadata(Base):
    __tablename__ = "data_upload_metadata"

    upload_id = Column(Integer, primary_key=True, nullable=False)
    table_name = Column(Text, primary_key=True, nullable=False)
    upload_time = Column(DateTime)
    active = Column(Boolean)
    username = Column(Text)
    notes = Column(Text)


class MeanPenguinStat(Base):
    __tablename__ = "mean_penguin_stat"

    upload_id = Column(Integer, primary_key=True, nullable=False)
    row_index = Column(Integer, primary_key=True, nullable=False)
    study_name = Column(Text)
    species = Column(Text)
    sex = Column(Text)
    culmen_length = Column(Float(53))
    culmen_depth = Column(Float(53))
    flipper_length = Column(Float(53))
    body_mass = Column(Float(53))
    delta_15_n = Column(Float(53))
    delta_13_c = Column(Float(53))


class MiserablesEdges(Base):
    __tablename__ = "miserables_edges"

    upload_id = Column(Integer, primary_key=True, nullable=False)
    row_index = Column(Integer, primary_key=True, nullable=False)
    start = Column(Text)
    end = Column(Text)
    count = Column(Integer)
    edge_id = Column(Integer)


class MiserablesNodes(Base):
    __tablename__ = "miserables_nodes"

    upload_id = Column(Integer, primary_key=True, nullable=False)
    row_index = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text)
    color = Column(Integer)


class PenguinLterSmall(Base):
    __tablename__ = "penguin_lter_small"

    upload_id = Column(Integer, primary_key=True, nullable=False)
    row_index = Column(Integer, primary_key=True, nullable=False)
    date_egg = Column(DateTime)
    island = Column(Text)
    study_name = Column(Text)
    region_culmen_list = Column(Text)
    clutch_completion = Column(Integer)


class PenguinSize(Base):
    __tablename__ = "penguin_size"

    upload_id = Column(Integer, primary_key=True, nullable=False)
    row_index = Column(Integer, primary_key=True, nullable=False)
    study_name = Column(Text)
    species = Column(Text)
    island = Column(Text)
    sex = Column(Text)
    region = Column(Text)
    culmen_depth_mm = Column(Float(53))
    culmen_length_mm = Column(Float(53))
    flipper_length_mm = Column(Integer)
    body_mass_g = Column(Integer)


class PenguinSizeSmall(Base):
    __tablename__ = "penguin_size_small"

    upload_id = Column(Integer, primary_key=True, nullable=False)
    row_index = Column(Integer, primary_key=True, nullable=False)
    species = Column(Text)
    island = Column(Text)
    culmen_length_mm = Column(Float(53))
    culmen_depth_mm = Column(Float(53))
    flipper_length_mm = Column(Integer)
    body_mass_g = Column(Integer)
    sex = Column(Text)


class Temperature(Base):
    __tablename__ = "temperature"

    upload_id = Column(Integer, primary_key=True, nullable=False)
    row_index = Column(Integer, primary_key=True, nullable=False)
    Date = Column(DateTime)
    Temp = Column(Float(53))
