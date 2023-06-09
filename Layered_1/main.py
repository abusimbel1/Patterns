from layers import ApplicationLayer,DataLayer,PresentationLayer

if __name__ == '__main__':
    data_layer = DataLayer()
    application_layer = ApplicationLayer(data_layer)
    app = PresentationLayer(application_layer)

    while True:
        app.get_item_value()