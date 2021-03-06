import redis
import time

conn = redis.Redis()

while True:
    continents = conn.keys()

    for continent in continents:

        # Decrement counts for each of the continents by 1
        if continent in ["North_America", "South_America", "Europe", "Africa", "Oceania", "Asia", "China"]:
            conn.decr(continent, 1)

    # Do this every 2 seconds,
    # this amount has been tested to balance the counter
    time.sleep(2)
