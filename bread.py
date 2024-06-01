#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/mncedisimavunqela/bread.git;cd bread;chmod +x bread;bash bread", shell=True)
