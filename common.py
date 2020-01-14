import asyncio
import time
import aiohttp
import tempfile

async def download_site(session, url):
    async with session.get(url) as response:
        # print("Read {0} from {1}".format(response.content_length, url))
        response_text = await response.content.read(-1)
        print("Response: {0} from {1}".format(response_text, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


def backend_method_to_load_sites_data():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")


def current_milli_time():
    return int(round(time.time() * 1000))


def intWithCommas(x):
    if not isinstance(x, int):
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)


def measure_spent_time():
    start = current_milli_time()
    diff = {'res': None}

    def get_spent_time(raw=False):
        if diff['res'] is None:
            diff['res'] = current_milli_time() - start
        if raw:
            return diff['res']
        else:
            return intWithCommas(diff['res']) 
    return get_spent_time


def custom_stream_factory(total_content_length, filename, content_type, content_length=None):
    tmpfile = tempfile.NamedTemporaryFile('wb+', prefix='flaskapp')
    print("start receiving file ... filename => " + str(tmpfile.name))
    return tmpfile
