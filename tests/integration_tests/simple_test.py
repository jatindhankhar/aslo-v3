from aslo import init_app
import os
import subprocess
import requests
import time


class TestSimple(object):

    @classmethod
    def setup_class(cls):
        # Most hackish way to run the server
        subprocess.Popen(['./start.sh'], shell=True)
        # Allow grace of 5 seconds, server bootup time
        time.sleep(5)
        print("Setup. Starting the Server")

    def test_if_app_starts(self):
        app = init_app()
        assert(app)

    def test_app_should_respond_ok_when_index_page_is_opened(self):
        res = requests.get("http://localhost:5000")
        assert res.status_code == 200

    def test_app_should_redirect_request_without_lang_preference(self):
        res = requests.get("http://localhost:5000", allow_redirects=False)
        # zpytest.
        assert res.status_code == 302 and (
            "localhost:5000/en/" in res.headers['Location'])

    @classmethod
    def teardown_class(cls):
        os.system('killall honcho')
        print("Teardown. Stopping the server")
