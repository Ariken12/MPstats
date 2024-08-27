import MPStatsConnector as mpsc
import MainWindow as mw


def main():
    mainwindow = mw.MainWindow()
    mainwindow.mainloop()
    token = '66c83e9a0ea899.5280906501a06672de4c5f55c764555248370db6'
    id = '1618484998'
    stats_connector = mpsc.MPStatsConnector(token)
    stats_connector.add_id(id, 'ozon')
    print(stats_connector.search())

if __name__ == '__main__':
    main()