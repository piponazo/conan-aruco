import os
from conans import ConanFile, CMake

USERNAME = os.getenv('CONAN_USERNAME', 'piponazo')
CHANNEL = os.getenv('CONAN_CHANNEL', 'testing')

class LiblasTestConan(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    requires = 'ArUco/2.0.18-0@%s/%s' % (USERNAME, CHANNEL)
    generators = 'cmake'

    def imports(self):
        if self.settings.os == 'Windows':
            self.copy('*.dll', src='bin', dst=os.sep.join(['.', 'bin', '%s' % self.settings.build_type]))
        elif self.settings.os == 'Macos':
            self.copy('*.dylib', src='dylibs', dst=os.sep.join(['.', 'bin']))
        else:
            self.copy('*.so*', src='lib', dst=os.sep.join(['.', 'bin']))

    def build(self):
        cmake = CMake(self.settings)

        # TODO : Remove CMAKE_MODULE_PATH when Aruco CMake code improves
        cmake_options = ['CMAKE_BUILD_TYPE=%s' % self.settings.build_type,
                         'CMAKE_MODULE_PATH="%s"' % self.deps_cpp_info['ArUco'].rootpath +
                         '/lib/cmake']
        options = '-D' + ' -D'.join(cmake_options)

        self.run('cmake "%s" %s %s' % (self.conanfile_directory, cmake.command_line, options))
        self.run('cmake --build . %s' % cmake.build_config)

    def test(self):
        os.putenv('DYLD_LIBRARY_PATH', os.sep.join(['.', 'bin']))
        if self.settings.os == 'Windows':
            self.run(os.sep.join(['.', 'bin', '%s' % self.settings.build_type, 'test']))
        else:
            self.run(os.sep.join(['.', 'bin', 'test']))
