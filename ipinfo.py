import requests

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    ip_address = input("Enter an IP address: ")
    ip_info = get_ip_info(ip_address)
    
    if ip_info:
        print("IP Information:")
        print(f"IP Address: {ip_info['ip']}")
        print(f"City: {ip_info['city']}")
        print(f"Region: {ip_info['region']}")
        print(f"Country: {ip_info['country']}")
        print(f"Location: {ip_info['loc']}")
    else:
        print("Failed to fetch IP information.")

if __name__ == "__main__":
    main()
