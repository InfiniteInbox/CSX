'''
Orbits
Yash Jain
'''
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = []

def main():
    Mass_of_Host = 6.00e25
    Distance_x = 4.00e7
    y_velocity_initial = 7.00e3
    x_velocity_initial = 0
    Distance_y = 0
    time_inc = 1
    itera = 20000
    G = 6.6743e-11
    make_data(Mass_of_Host, Distance_x, y_velocity_initial, x_velocity_initial, Distance_y, G, data, time_inc, itera)
    print(len(data))
    plot_data(data)


def make_data(Mass_of_Host, Distance_x, y_velocity_initial, x_velocity_initial, Distance_y, G, data, time_inc, itera):
    M_O_H = float(Mass_of_Host)
    D_x = float(Distance_x)
    D_y = float(Distance_y)
    y_v = float(y_velocity_initial)
    x_v = float(x_velocity_initial)
    time_inc_og = float(time_inc)
    itera = int(itera)
    data.append([0, x_v, y_v, D_x, D_y, 0, 0])
    for i in range(itera-1):
        x_a = (-G)*((M_O_H*D_x)/((D_x**2) + (D_y**2))**1.5)
        y_a = (-G)*((M_O_H*D_y)/((D_x**2) + (D_y**2))**1.5)
        x_v = x_v + (x_a*time_inc)
        D_x = D_x + (x_v*time_inc)
        y_v = y_v + (y_a*time_inc)
        D_y = D_y + (y_v*time_inc)
        time_inc = (i+1)*time_inc_og
        data.append([time_inc, x_v, y_v, D_x, D_y, x_a, y_a])

def plot_data(data):
    x_vals = []
    y_vals = []
    fig, ax = plt.subplots()
    ax.set_xlim(-5e7, 5e7)
    ax.set_ylim(-5e7, 5e7)
    ax.set_xlabel("D_x")
    ax.set_ylabel("D_y")
    line, = ax.plot([], [], 'o')

    def animate(i):
        x_vals.append(data[i][3])
        y_vals.append(data[i][4])
        line.set_data(x_vals, y_vals)
        return line,

    ani = animation.FuncAnimation(fig, animate, frames=len(data), interval=75, blit=True)
    ax.autoscale()
    plt.show()

if __name__ == '__main__':
    main()