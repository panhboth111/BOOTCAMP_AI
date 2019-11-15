
import sys
class Info:
    @staticmethod
    def script_name():
        print(sys.argv[0].split('/')[-1])
    @staticmethod
    def python_path():
        print(sys.executable)
    @staticmethod
    def python_version():
        print(sys.version)
    @staticmethod
    def python_platform():
        print(sys.platform)