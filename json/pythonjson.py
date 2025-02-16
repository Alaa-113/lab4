import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

for item in data["imdata"]:
    interface = item.get("l1PhysIf", {}).get("attributes", {})
    dn = interface.get("dn", "N/A")
    description = interface.get("descr", "")
    speed = interface.get("speed", "inherit")
    mtu = interface.get("mtu", "N/A")

    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<6}")
