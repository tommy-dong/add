from conans import ConanFile, CMake
from distutils.dir_util import copy_tree

class AddConan(ConanFile):
    name = "add"
    version = "0.1"
    settings = "os","arch","build_type","compiler"
    
    #options = {
    #    "macos_minversion": ["10.10"],
    #    "macos_sdk": ["10.14"]
    #}    

    def source(self):
        print("sourcing...")
        copy_tree("~/Projects/test/add", ".")
    
    def build(self):
        cmake = CMake(self) #self._configure_cmake()#CMake(self)
        cmake.configure(source_dir="src")
        cmake.build()
        #cmake.install()
   
    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
 
    def package_info(self):
        self.cpp_info.libs = ["add"]
