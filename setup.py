from setuptools import setup
from setuptools.command.install import install

class CustomInstallCommand(install):
    """Customized install command to print 'Predator_97'."""
    def run(self):
        print("Predator_97")
        install.run(self)

setup(
    name='predator_print',
    version='0.1',
    description='A setup script that prints Predator_97',
    cmdclass={
        'install': CustomInstallCommand,
    },
)
