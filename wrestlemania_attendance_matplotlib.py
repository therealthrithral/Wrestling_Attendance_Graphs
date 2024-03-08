import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_csv_data():
    root = Tk()
    root.withdraw()  # No full GUI. Keep root window from appearing
    filename = askopenfilename()  # Show open box and return path
    root.destroy()
    if filename:
        data = pd.read_csv(filename)
        print(data.columns)
        return data
    else:
        return None

def plot_ppv_data(dataframe):
    #  CSV must have columns 'Event' and 'Date'
    dataframe['Date:'] = pd.to_datetime(dataframe['Date:'])  # Ensure Date is in datetime format
    dataframe.sort_values('Date:', inplace=True)  # Sort data by date

    for i, txt in enumerate(dataframe['Event:']):
        plt.annotate(txt, (dataframe['Date:'].iloc[i], dataframe['Attendance:'].iloc[i]), fontsize=8, ha='right')

    plt.figure(figsize=(10,5))
    plt.plot(dataframe['Date:'], dataframe['Event:'], marker='o', linestyle='-')
    plt.title('Wrestlemania Claimed Attendance')
    plt.xlabel('Date:')
    plt.ylabel('Event:')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    data = load_csv_data()
    if data is not None:
        # Convert 'Date' column to datetime and sort
        data['Date:'] = pd.to_datetime(data['Date:'])
        data.sort_values('Date:', inplace=True)

        # Creating the plot
        root = Tk()
        root.title("Wrestling PPV Attendance Graph")
        fig = plt.Figure(figsize=(10, 5), dpi=100)
        plot = fig.add_subplot(1, 1, 1)

        # Plot 'Attendance' over 'Date'
        plot.plot(data['Date:'], data['Attendance:'], marker='o', linestyle='-')
        plot.set_title('Wrestlemania Claimed Attendance')
        plot.set_xlabel('Date:')
        plot.set_ylabel('Attendance:')
        fig.autofmt_xdate()  # Auto format date labels

        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

        root.mainloop()

if __name__ == "__main__":
    main()