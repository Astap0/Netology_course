stats = {"facebook": 55, "yandex": 120, "vk": 115, "google": 99, "email": 42, "ok": 98}

max_value = max(stats.values())


for soc, stat in stats.items():
    if stats[soc] == max_value:
        print(f"{soc} : {stat}")
