from easyprocess import EasyProcess
from easyprocess import extract_version
from PIL import Image
from pyscreenshot.tempexport import read_prog_img

PROGRAM = 'import'
# http://www.imagemagick.org/


class ImagemagickWrapper(object):
    name = 'imagemagick'
    childprocess = True

    def __init__(self):
        EasyProcess([PROGRAM, '-version']).check_installed()

    def grab(self, bbox=None):
        command = [PROGRAM, '-silent', '-window', 'root']
        if bbox:
            pbox = '{}x{}+{}+{}'.format(
                bbox[2] - bbox[0], bbox[3] - bbox[1], bbox[0], bbox[1])
            command += ['-crop', pbox]
        im = read_prog_img(command)
        return im

    def backend_version(self):
        return extract_version(
            EasyProcess([PROGRAM, '-version']).call().stdout.replace('-', ' '))
