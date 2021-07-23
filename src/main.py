import time
from cv_app import start
from webserver import app
import multiprocessing

import os

print(f"Running main app: {__name__}")


def test():
    print("this should only run once")
    app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    # Change working directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # webserver = multiprocessing.Process(
    #     target=app.run, kwargs={"host": "0.0.0.0", "debug": True}
    # )
    webserver = multiprocessing.Process(target=test)
    cv_app = multiprocessing.Process(target=start)

    print("Starting webserver...")
    value = webserver.start()

    print(f"Got: {value}")

    # time.sleep(1)

    # print("Starting cv app")
    # cv_app.start()

    # webserver.join()
    # cv_app.join()
