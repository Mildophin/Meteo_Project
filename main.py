import requests
import sys

print("Bienvenue chez météo France")
ville = input("Dans quelle ville voulez-vous connaître la météo ? ")

url_weather = "http://api.openweathermap.org/data/2.5/weather?q=" + ville + "&APPID=beb97c1ce62559bba4e81e28de8be095"

r_weather = requests.get(url_weather)
data = r_weather.json()

print("Vous êtes à " + ville)

# température moyenne
t = data['main']['temp']
print("La température moyenne est de {} degrés Celsius".format(t - 273.15))
# écart de température
t_min = data['main']['temp_min']
t_max = data['main']['temp_max']
print("Les temperatures varient entre {}".format(t_min - 273.15) + " a {} degrés Celsius".format(t_max - 273.15))
# taux d'humidité
humidite = data['main']['humidity']
print("Taux d'humidité est de {}".format(humidite) + "%")
# état du ciel
temps = data['weather'][0]['description']
print("Conditions climatiques : {}".format(temps))

# on demande ensuite si l'utilisateur veut les prévisions pour les jours à venir

url_forecast = "http://api.openweathermap.org/data/2.5/forecast?q=" + ville + "&APPID=beb97c1ce62559bba4e81e28de8be095"
r_forecast = requests.get(url_forecast)
data = r_forecast.json()

def connaitre_les_previsions():
    prevision = input("Voulez vous connaitre les prévisions météo de cette ville ? ")
    if prevision.isalpha() == True:
        if prevision == ("oui"):
            for i in range(0, 25):
                t = data['list'][i]['main']['temp']
                temps = data['list'][i]['weather'][0]['description']
                time = data['list'][i]['dt_txt']
                print("Prévisions pour le {}".format(time))
                print("La température moyenne est de {} degrés Celsius".format(t - 273.15))
                print("Conditions climatiques : {}".format(temps))
                sys.exit()
        if prevision == ("non"):
            print("Ok")
            sys.exit()
        else:
            print("Veuillez indiquer \"oui\" ou \"non\" uniquement")
            connaitre_les_previsions()
    else:
        print("Veuillez indiquer une réponse valide")
        connaitre_les_previsions()

connaitre_les_previsions()
