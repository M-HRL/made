from project.src.persistence.repository import Repository
from project.src.service.data_service import DataService

repository = Repository()
data_service = DataService(repository)


def load_data():
    data_service.load_rides(url="https://www.mvg.de/dam/mvg/services/mobile-services/mvg-rad/fahrten-csv/MVG_Rad_Fahrten_2022.zip")
    data_service.load_paths(url="https://opendata.muenchen.de/dataset/7ad3bc6c-4c1a-4a63-9cb2-0d613f5b69fa/resource/14977232-94f3-4cdb-94fc-1e709698ba3f/download/radwege_t2.csv")


if __name__ == '__main__':
    # load datasets
    load_data()
