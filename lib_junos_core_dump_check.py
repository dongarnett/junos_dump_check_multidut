import argparse, datetime, os, paramiko, re, sys, time
from lib_ssh_connectivity import Device
from lib_ssh_connectivity import create_handle_quiet
from pprint import pprint
from collections import defaultdict




'''Get chassis core dump values from device'''
def get_dump_messages(dut_host):
    date_time = datetime.datetime.now()
    current_time = date_time.timestamp()
    '''Command sets for device configuration'''
    command_set_1 = [f'show system core-dumps | no-more']
    '''Create handle'''
    dut_host_session = create_handle_quiet(dut_host)
    dut_host_terminal = dut_host_session.invoke_shell()
    '''Start execution'''
    for command in command_set_1:
        print(f'Sending command: {command}\n')
        try:
            dut_host_terminal.send(f'{command}\n')
            time.sleep(5)
        except:
            print(f"An error occurred.")
            time.sleep(1)
        output = dut_host_terminal.recv(1000000).decode('utf-8')
    output_recv = output.split('\r\n')
    dut_host_terminal.send('exit\n')
    return output



'''Parse output from core dump data retrieved'''
def parse_dump_count(inputs):
    init_core_dump_data = re.findall(r'^total\sfiles:\s+\d+', inputs, re.MULTILINE)
    for init_line in init_core_dump_data:
        line_list = re.findall(r'\d+', init_line)
        for line in line_list:
            #print(line)
            if int(line) > 0:
                dump_count = int(line)
            else:
                dump_count = 0
    if len(init_core_dump_data) == 0:
         dump_count = 0
    return dump_count
