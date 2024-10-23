import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt  # Fix import here
from requests import session  # No issues here
fastf1.plotting.setup_mpl()  # Assuming this sets up matplotlib for FastF1 plotting

def session_loader(ax):

    sT = str(input("input session (p1,p2,p3,Q or race)"))
    sY = int(input("session year"))
    sL = str(input("choose track"))


    session = fastf1.get_session(sY,sL,sT)
    session.load()
    add_drivers(session,ax)

def graph_setup():
    fig, ax = plt.subplots(4)
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Speed [Km/h]')
    ax[0].set_title(' fastest lap')


    ax[1].set_xlabel('Time')
    ax[1].set_ylabel('Throttle')

    ax[2].set_xlabel('Time')
    ax[2].set_ylabel('Brake')

    ax[3].set_xlabel('Time')
    ax[3].set_ylabel('Gear')
    session_loader(ax)

def add_drivers(session,ax):
    driver = str(input("input drivers shorthand (e.g VER,HAM,PER)"))
    temp = session.laps.pick_driver(driver)
    temp_fastest = temp.pick_fastest()
    temp_data = temp_fastest.get_car_data().add_distance()

    ax[0].plot(temp_data['Distance'], temp_data['Speed'], label=str(driver))
    ax[1].plot(temp_data['Distance'], temp_data['Throttle'], label=str(driver))
    ax[2].plot(temp_data['Distance'], temp_data['Brake'], label=str(driver))
    ax[3].plot(temp_data['Distance'], temp_data['nGear'], label=str(driver))



    ans = int(input("add another driver? 1.yes,2.no"))
    if ans == 1:
        add_drivers(session,ax)
    else:
        plt.show()
graph_setup()
