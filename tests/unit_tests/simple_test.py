from aslo import init_app
import os
import subprocess


class TestSimple(object):

    @classmethod
    def setup_class(cls):
        # Most hackish way to run the server
        subprocess.Popen(['./start.sh'], shell=True)
        print("Setup. Starting the Server")

    def test_if_app_starts(self):
        app = init_app()
        assert(app)

    @classmethod
    def teardown_class(cls):
        os.system('killall honcho')
        print("Teardown. Stopping the server")
