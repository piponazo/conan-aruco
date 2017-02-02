import os
from conans import ConanFile, tools, CMake

class ArucoConan(ConanFile):
    name = 'ArUco'
    lib_version = '2.0.18'
    version = '%s-0' % lib_version
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'ArUco recipe for the public repository in sourceforge'
    url = 'https://github.com/piponazo/conan-aruco'
    license = ' GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007'

    def config_options(self):
        self.requires('OpenCV/3.1.0-0@piponazo/testing')

    def source(self):
        zip_name = 'aruco-%s.zip' % self.lib_version
        url='https://sourceforge.net/projects/aruco/files/%s/%s' % (self.lib_version, zip_name)
        self.output.info('Downloading %s...' % url)
        tools.download(url, zip_name)
        tools.unzip(zip_name, '.')
        os.remove(zip_name)

    def build(self):
        source_path = 'aruco-%s' % self.lib_version
        build_path = '%s/buildConan' % source_path
        os.makedirs(build_path)

        cmake = CMake(self.settings)
        cmake_options = ['CMAKE_BUILD_TYPE=%s' % self.settings.build_type,
                         'CMAKE_PREFIX_PATH="%s"' % self.deps_cpp_info['OpenCV'].rootpath,
                         'CMAKE_INSTALL_PREFIX=%s' % self.package_folder]

        options = '-D' + ' -D'.join(cmake_options)

        config_command = 'cd %s && cmake .. %s %s' % (build_path, cmake.command_line, options)
        self.output.warn(config_command)
        self.run(config_command)

        compile_command = 'cd %s && cmake --build . %s' % (build_path, cmake.build_config)
        if self.settings.os != 'Windows':
            n_cores = tools.cpu_count()
            compile_command = compile_command + ' -- -j%s' % n_cores
        self.output.warn(compile_command)
        self.run(compile_command)

        install_command = 'cd %s && cmake --build . --target install' % build_path
        install_command = install_command + ' --config %s' % (self.settings.build_type)
        self.output.warn(install_command)
        self.run(install_command)
