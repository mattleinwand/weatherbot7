if __name__ == "__main__":
    import time

    def to_f(kelvin):
            f = ((float(kelvin)-273.15)* (9/5) + 32)
            return int(f)
    candler_lat = '33.7649'
    candler_long = '-84.3418'
    api_key = '6289b89740b48b5748b7e7306ed8a52b'

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={candler_lat}&lon={candler_long}&appid={api_key}"
    def weatherbot(hours_to_wait):
        i = 0
        while True:
            weather_result =requests.get(url).json()
            kelvin = weather_result['main']['temp']
            F_temp = to_f(kelvin)
            account_sid = 'AC06da32eeccde42ee4750
            auth_token = 'cca4ac1da3533e0deb811d1bccb96082'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
              body= f"{i}today's weather is {int(F_temp)}",
              from_='+15139604922',
              to='+12692717174')
            seconds_to_wait = hours_to_wait*60*60
            time.sleep(seconds_to_wait)
            i+=1
            if i == 4:
                break
    weatherbot(24)
