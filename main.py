# Copyright 2015 Louis-Gabriel ZAITI
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


__author__ = 'lgzaiti'

import sys
import os
import getopt



verbose = False


def usage():
    print 'Usage DrawTurbinator [-h] [-v] [-dest=]'
    print ''
    print 'Move Android drawable generated on Google \'Android Asset Studio\''


def main():
    print('Hello World!')
    # args = '--condition=foo --testing --output-file abc.def -x a1 a2'.split()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
    # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    print(args)
    # optlist, args = getopt.getopt(args, 'x', ['condition=', 'output-file=', 'testing'])
    print(opts)

    for option in opts:
        if (option in ('-v', '--verbose')):
            verbose = True
        elif option in ('-h', '--help', '--h'):
            usage()
            sys.exit()
        else:
            assert False, "Unhandled option"


    moveDrawablesTurbinator()


if __name__ == "__main__":
    main()


def moveDrawablesTurbinator():
    i = 0
    print 'hellooooo'

    src_path_ = "/tmp/New_topic_picto"

    hdpi = 'drawable-hdpi'
    mdpi = 'drawable-mdpi'
    xhdpi = 'drawable-xhdpi'
    xxhdpi = 'drawable-xxhdpi'
    xxxhdpi = 'drawable-xxxhdpi'

    path_drawable_hdpi_ = src_path_ + '/' + hdpi + '/'
    path_drawable_mdpi_ = src_path_ + '/' + mdpi + '/'
    path_drawable_xhdpi_ = src_path_ + '/' + xhdpi + '/'
    path_drawable_xxhdpi_ = src_path_ + '/' + xxhdpi + '/'
    path_drawable_xxxhdpi_ = src_path_ + '/' + xxxhdpi + '/'

    if (os.path.exists(path_drawable_hdpi_) == False):
        os.mkdir(path_drawable_hdpi_)

    if (os.path.exists(path_drawable_mdpi_) == False):
        os.mkdir(path_drawable_mdpi_)

    if (os.path.exists(path_drawable_xhdpi_) == False):
        os.mkdir(path_drawable_xhdpi_)

    if (os.path.exists(path_drawable_xxhdpi_) == False):
        os.mkdir(path_drawable_xxhdpi_)

    if (os.path.exists(path_drawable_xxxhdpi_) == False):
        os.mkdir(path_drawable_xxxhdpi_)

    for file in os.listdir(src_path_):

        if (file.startswith('res')):
            res_directory = src_path_ + "/" + file

            if (verbose):
                print 'Found a res folder: ' + res_directory
            if (os.path.isdir(res_directory)):
                # The component is a directory
                for _density_folder in os.listdir(res_directory):

                    # print 'found an item in ' + res_directory + ' : ' + _density_folder
                    if (_density_folder.startswith("drawable-") and
                            os.path.isdir(res_directory + "/" + _density_folder)):

                        _density_folder_path = res_directory + '/' + _density_folder
                        for drawable in os.listdir(_density_folder_path):
                                # print _density_folder[0: _density_folder.index("-")]
                            #
                            if (verbose):
                                print 'Moving file { ' + _density_folder_path + '/' + drawable + ' } into : ' + src_path_ + _density_folder[
                                                                                                                        0: _density_folder.index(
                                                                                                                            "-")]
                            if (_density_folder.endswith('-hdpi')):
                                os.rename(_density_folder_path + '/' + drawable, path_drawable_hdpi_ + drawable)
                            if (_density_folder_path.endswith('-mdpi')):
                                os.rename(_density_folder_path + '/' + drawable, path_drawable_mdpi_ + drawable)
                            if (_density_folder_path.endswith('-xhdpi')):
                                os.rename(_density_folder_path + '/' + drawable, path_drawable_xhdpi_ + drawable)
                            if (_density_folder_path.endswith('-xxhdpi')):
                                os.rename(_density_folder_path + '/' + drawable, path_drawable_xxhdpi_ + drawable)
                            if (_density_folder_path.endswith('-xxxhdpi')):
                                os.rename(_density_folder_path + '/' + drawable, path_drawable_xxxhdpi_ + drawable)

                    else:
                        print 'Item was not starting with drawable || Was not a folder'

    return
