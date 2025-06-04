"""Example client for interacting with the running Flask API."""
import requests


def main():
    timestamp = input("Timestamp: ")
    pattern = input("Pattern (e.g. 1010): ")
    params = {"timestamp": timestamp, "pattern": pattern}
    response = requests.get("http://localhost:5000/Ratio", params=params)
    print(response.json())


if __name__ == "__main__":
    main()
