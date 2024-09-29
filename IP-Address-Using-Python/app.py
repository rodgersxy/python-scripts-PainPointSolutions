import requests


def get_ip():

    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "currency": response.get("currency"),
        "country_population": response.get("country_population"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "asn": response.get("asn"),
        "timezone": response.get("timezone"),
        "postal": response.get("postal"),
        "country_code": response.get("country_code"),
        "country_area": response.get("country_area")

    }
    return location_data


print(get_location())