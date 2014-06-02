#!/usr/bin/python
#coding=utf-8

import subprocess
import argparse
import sys


def upLoadBinToSTM32():
	'''将编译生产的二进制文件上传至单片机'''
	try:
		subprocess.check_output('''openocd -d0 -f board/stm32f4discovery.cfg -c init -c targets -c 	"poll" -c "reset halt" -c "flash probe 0" -c "flash write_image erase build/main.elf" -c "verify_image build/main.elf" -c "reset run" -c shutdown ''',
			stderr=subprocess.STDOUT,
			shell=True)
	except subprocess.CalledProcessError:
		print "没有安装openOCD"
		sys.exit()
	except:
		print "其他错误"
		sys.exit()
	print "上传成功"
	

def main():
	''' 主程序'''
	parser = argparse.ArgumentParser(description='stm32f4自动工具')
	parser.add_argument("--programme", "-P", action='store_true', help="烧写程序")
	parser.add_argument("--upload", "-L", action='store_true', help="烧写程序")
	args = parser.parse_args()
	if args.programme or args.upload:
		upLoadBinToSTM32()
	



if __name__ == '__main__':
    main()
