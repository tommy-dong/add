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
        self.run("git clone https://github.com/tommy-dong/add.git")
        copy_tree("add", ".")
    
    def build(self):
        cmake = CMake(self) #self._configure_cmake()#CMake(self)
        cmake.configure(source_dir="add")
        cmake.build()
        #cmake.install()
   
    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
 
    def package_info(self):
        self.cpp_info.libs = ["add"]
