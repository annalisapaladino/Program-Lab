class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__ (self, name):
        self.name = name

    def get_data(self):
        # inizializzo una lista vuota per salvare i valori
        values=[]
        # apro e leggo il file, linea per linea
        try:
            my_file = open(self.name, 'r')
        except:
            raise ExamException('il file non esiste')

        for line in my_file:
            # faccio lo split di ogni riga sulla virgola
            elements = line.split(',')

            # se non sto processando l'intestazione
            if elements[0] != 'epoch':
                # setto l'epoch e la temperatura
                epoch = elements[0]
                temperature = elements[1]
                values.append([int(float(epoch)), float(temperature)])
                #print (epoch)

        # chiudo il file
        my_file.close ()
        return(values)

# creo la funzione a sé stante: daily_stats
def daily_stats(time_series):
    # inizializzo una lista vuota per salvare le statistiche giornaliere
    statistics = []
    # inizializzo un indice nullo che userò in seguito per ricavare i vari valori
    index = 0

    # controllo che la lista sia ordinata
    for i in range (len(time_series) - 1):
        if time_series[i][0] >= time_series[i + 1][0]:
            raise ExamException('lista non ordinata')

    while (index < len(time_series)): 
        # inizio e fine giornata
        start = time_series[index][0] - (time_series[index][0] % 86400)
        end = start + 86400

        # massimo e minimo
        minimum = time_series[index][1]
        maximum = time_series[index][1]

        # dichiaro la sommatoria ed il contatore della media nulli
        summation = 0
        counter = 0

        # uso l'indice dichiarato in precedenza per ricavare i valori delle giornate
        while (index < len(time_series) and time_series[index][0] < end):      
            if (minimum >= time_series[index][1]):
                minimum = time_series[index][1]
            if (maximum <= time_series[index][1]):
                maximum = time_series[index][1]

            # incremento
            summation += time_series[index][1]
            counter += 1
            index += 1

        summation = summation / counter

        # lista che contiene minimo, massimo e media
        lista = [minimum, maximum, summation]
        statistics.append(lista)
    print(len(statistics))
    return statistics

# questa classe si dovrà quindi poter usare così:
time_series_file = CSVTimeSeriesFile (name='data.csv')
time_series = time_series_file.get_data()

# stampo max, min, media
stats = daily_stats(time_series)

for line in stats:
    print (line, '\n')