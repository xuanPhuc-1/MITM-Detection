import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates


def plot_data(filename):
    aps = []
    abps = []
    subarp = []
    miss_mac = []
    time = []

    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            row = line.split(",")
            aps.append(float(row[0]))
            abps.append(float(row[1]))
            subarp.append(int(row[2]))
            miss_mac.append(int(row[3]))
            time_obj = datetime.strptime(row[4].strip(), "%H:%M:%S")
            time.append(time_obj)

    plt.plot(time, aps, label="APS")
    plt.plot(time, abps, label="ABPS")
    plt.plot(time, subarp, label="SUBARP")
    plt.plot(time, miss_mac, label="MISS_MAC")

    plt.grid(True)  # Bật lưới trên đồ thị
    plt.gca().format_xdata = mdates.DateFormatter(
        '%H:%M:%S')  # Định dạng hiển thị giá trị trục x

    plt.legend()
    plt.xlabel("Time (H:M:S)")
    plt.ylabel("Value")

    # Hiển thị giá trị khi click
    def onpick(event):
        thisline = event.artist
        xdata, ydata = thisline.get_xdata(), thisline.get_ydata()
        ind = event.ind
        print(
            f'Clicked on line with label {thisline.get_label()} at x={xdata[ind]}, y={ydata[ind]}')

    plt.show()


if __name__ == "__main__":
    plot_data("evaluation.csv")
