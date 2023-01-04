import requests
from fake_useragent import UserAgent
import json
import sqlite3
from config import host, user, password, db_name


def collect_data(weapon_type=2):
    offset = 0
    batch_size = 60
    result = []
    count = 0

    db = sqlite3.connect('elements.db')
    c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS elements (
        itemName text,
        link text,
        computed integer,
        discount integer,
        id integer
    )""")
    db.commit()

    while True:
        for item in range(offset, offset + batch_size, 60):

            url = f'https://cs.money/1.0/market/sell-orders?deliverySpeed=instant&deliverySpeed=fast&limit=60&maxPrice=1000&minPrice=150&offset={item}&type={weapon_type}'
            response = requests.get(
                url=url,
                headers={
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
            )

            offset += batch_size
            data = response.json()
            items = data.get("items")

            for i in items:
                item_id = i.get("id")
                assets = i.get("asset")

                if i.get("pricing").get("discount") is not None and i.get("pricing").get("discount") >= 0.19:
                    item_3d = i.get("links").get("3d")
                    item_price = i.get("pricing").get("computed")
                    item_over_price = i.get("pricing").get("discount")
                    item_name = assets.get('names').get('full')
                    result.append(
                        {
                            'name': item_name,
                            '3d': item_3d,
                            'computed': item_price,
                            'discount': item_over_price,
                            'id': item_id
                        }
                    )
                    c.execute("INSERT INTO elements VALUES(?, ?, ?, ?, ?)", (item_name, item_3d, item_price, item_over_price, item_id))

        db.commit()
        count += 1
        print(f'Page #{count}')
        print(url)

        if len(items) < 60:
            break

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print(len(result))
    print(result)


def main():
    collect_data()


if __name__ == '__main__':
    main()
