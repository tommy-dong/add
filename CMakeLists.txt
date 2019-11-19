cmake_minimum_required(VERSION 3.14)
project(add)
aux_source_directory(src DIR_LIB_SRCS)

add_library(add ${DIR_LIB_SRCS})
