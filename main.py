import asyncio
import json
import platform

from just_eat_api.client import JustEatClient


async def main():
    try:
        postcode = "EC4"
        proxy = "http://15.204.161.192:18080"
        client = JustEatClient(proxy=proxy)
        restaurants = await client.by_postcode(postcode)

        restaurants_json = json.dumps(
            [restaurant.__dict__ for restaurant in restaurants], indent=4
        )
        print(restaurants_json)

        with open("restaurants.json", "w") as json_file:
            json_file.write(restaurants_json)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
