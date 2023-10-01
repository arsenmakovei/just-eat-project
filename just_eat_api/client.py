import aiohttp

from just_eat_api.models import Restaurant


class JustEatClient:
    def __init__(self, proxy=None):
        self.base_url = "https://uk.api.just-eat.io/restaurants/bypostcode/"
        self.proxy = proxy

    async def by_postcode(self, postcode):
        url = f"{self.base_url}{postcode}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, proxy=self.proxy) as response:
                    data = await response.json()
                    restaurants_data = data.get("Restaurants")

                    if restaurants_data:
                        restaurants = []

                        for restaurant_data in restaurants_data:
                            restaurant = Restaurant(
                                name=restaurant_data["Name"],
                                rating=restaurant_data["RatingStars"],
                                cuisines=[
                                    cuisine["Name"]
                                    for cuisine in restaurant_data.get("Cuisines")
                                ],
                            )
                            restaurants.append(restaurant)

                        return restaurants

                    raise Exception(
                        f"There are no restaurants for postcode: {postcode}"
                    )
        except aiohttp.ClientProxyConnectionError:
            raise Exception(
                f"Cannot connect to host {self.proxy}, "
                "please check your network connection or "
                "ensure you have entered the correct proxy settings"
            )
        except aiohttp.ContentTypeError:
            raise Exception(
                "You have been blocked, ensure you have entered the correct proxy settings"
            )
