import fastf1.ergast
import pandas
from fastf1 import *
import pandas as pd
ergast = fastf1.ergast.Ergast()

def session_creator(year,circuit,session_type):
    session = get_session(year=year,gp=circuit,identifier=session_type)
    return(session)

def fastest_lap_loader(session,driver):
    session.load()
    laps = session.laps.pick_driver(driver)
    lap = laps.pick_fastest()
    return(lap)



def get_ciruits_and_country(year):
    circuit_list = ergast.get_circuits(year)
    country_list = circuit_list['country']
    country_list = country_list.to_list()
    circuit_list = circuit_list['circuitId']
    circuit_list = circuit_list.to_list()
    return(circuit_list,country_list)


def get_drivers(year,circuit):
    driver_list = ergast.get_driver_info(season=year,circuit=circuit)
    driver_list = driver_list['driverId']
    driver_list = driver_list.to_list()
    return(driver_list)

def get_years():
    year_list = []
    years = ergast.get_seasons(limit=100)
    years = years['season']
    for i in range(0,len(years)):
        if years[i] >= 2018:
            year_list.append(years[i])
    return(year_list)

def get_countries(year):
    country_list = ergast.get_circuits(year)
    country_list = country_list['country']
    country_list = country_list.to_list()
    return (country_list)

def driver_laps(driver,session):
    session.load()
    laps = session.laps.pick_driver(driver)
    return(laps)


def round_num_id(year,circuit):
    lst = ergast.get_circuits(year)
    lst = lst['circuitId']
    lst = lst.to_list()
    h = str(circuit).lower()
    return(lst.index(h))

def driver_id(driver,year,circuit):
    s = get_session(year, circuit, 'Q')
    s.load()
    driver_list = ergast.get_driver_info(season=year,circuit=circuit)
    id_list = driver_list['driverNumber']
    id_list = id_list.to_list()
    driver_list = driver_list['driverId']
    driver_list = driver_list.to_list()
    x = driver_list.index(driver)
    id = id_list[x]
    print(id)
    return(id)
