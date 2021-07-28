import time
from cv_app import start
from webserver import app
import multiprocessing

import os

if __name__ == "__main__":
    # Change working directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    webserver = multiprocessing.Process(
        target=app.run, kwargs={"host": "0.0.0.0", "debug": True, "use_reloader": False}
    )
    cv_app = multiprocessing.Process(target=start)

    webserver.start()

    time.sleep(1)

    cv_app.start()
