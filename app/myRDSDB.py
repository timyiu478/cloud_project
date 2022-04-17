from sqlalchemy import create_engine,Table,MetaData,and_,Column,Float,Integer,String,TIMESTAMP
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
import datetime
import random

class DB:
    def __init__(self):
        self.metadata = MetaData()
        self.engine = None
        self.session = None
        self.latestTime = datetime.datetime(1, 1, 1, 0, 0)
        self.monitor = Table(
            'monitor',self.metadata,
            Column('driverID',String),
            Column('carPlateNumber',String),
            Column('Latitude',Float),
            Column('Longtitude',Float),
            Column('Speed',Integer),
            Column('Direction',Integer),
            Column('siteName',String),
            Column('Time',TIMESTAMP),
            Column('isRapidlySpeedup',Float),
            Column('isRapidlySlowdown',Float),
            Column('isNeutralSlide',Float),
            Column('isNeutralSlideFinished',Float),
            Column('neutralSlideTime',Float),
            Column('isOverspeed',Float),
            Column('isOverspeedFinished',Float),
            Column('overspeedTime',Float),
            Column('isFatigueDriving',Float),
            Column('isHthrottleStop',Float),
            Column('overspeedTime',Float),
            Column('isOilLeak',Float),
        )

    def connectDB(self):
        # connects to a postgres db
        ENDPOINT = "comp4442-project.czxv4n2n9tgm.us-east-1.rds.amazonaws.com"
        PORT = "5432"
        USER = "postgres"
        DBNAME = "postgres"
        PASSWORD="jo0p3984urj20983u123qe3hrn34uwe97y"
        
        try:
            self.engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DBNAME}", echo=True)
            self.metadata.create_all(self.engine)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            print("Database is connected")
        except Exception as e:
            print("Database connection failed due to {}".format(e))


    def getDrivers(self):
        cols = self.monitor.columns
        return self.session.query(cols.driverID).distinct()

    def getDriversData(self):
        driverIDs = self.getDrivers().all()

        cols = self.monitor.columns

        driverSeries = {}

        maxTime = self.latestTime

        for driverID in driverIDs:
            result = self.session.query(cols.Speed,cols.Time,cols.isOverspeed,cols.isOverspeedFinished).\
                where(and_(cols.Time > self.latestTime, cols.driverID == driverID[0]))\
                .order_by(cols.Time.asc()).all()
            graphData = []
            for row in result:
                graphData.append({
                    'x': row.Time.timestamp() ,
                    'y': row.Speed
                })
            driverSeries[driverID[0]] = {
                'name': driverID[0],
                'data': graphData,
                'color': "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
            }
            if len(result)>0 and maxTime < result[-1].Time:
                maxTime = result[-1].Time

        self.latestTime = maxTime

        return driverSeries
                
    def writeDrivingData(self,data):
        statement = self.monitor.insert().values(**data)
        self.session.execute(statement) 
        self.session.commit()