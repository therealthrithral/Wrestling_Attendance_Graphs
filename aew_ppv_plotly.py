import pandas as pd
import plotly.express as px
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def load_csv_data():
    root = Tk()
    root.withdraw()  # No full GUI.  Keep root window from appearing
    filename = askopenfilename()  # Show open box and return path
    root.destroy()
    if filename:
        return pd.read_csv(filename)
    else:
        return None


def plot_ppv_data_with_plotly(dataframe):
    dataframe['Date:'] = pd.to_datetime(dataframe['Date:'])  # Ensure Date is in datetime format
    dataframe.sort_values('Date:', inplace=True)  # Sort data by date

    # Use Plotly Express to plot the data, showing 'Event:' names on hover
    fig = px.scatter(dataframe, x='Date:', y='Attendance:', text='Event:',
                     hover_data=['Event:'], title='AEW PPV Attendance')
    fig.update_traces(marker=dict(size=10),
                      selector=dict(mode='markers+text'))
    fig.update_layout(xaxis_title='Date', yaxis_title='Attendance')
    fig.show()


def main():
    data = load_csv_data()
    if data is not None:
        plot_ppv_data_with_plotly(data)


if __name__ == "__main__":
    main()
