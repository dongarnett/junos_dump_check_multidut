# junos_dump_check_multidut


Purpose:
This tool checks for existing core dumps across multiple devices by reading a list of device IP addresses from an external file.

It perform the following workflow on each device:
1. Obtain currently existing core dump(s).
2. Displays core dumps if there are any currently have been triggered.

This tool can be run at the end of a larger script after device triggers have been exercised.
This tool can also be run without triggers to determine any existing core dumps are present.



Requirements:
The Paramiko SSH library is required for connectivity to the target device.


Usage:
junos_dump_check_multidut.py -t <device_list_file> -u <username> -p <password>

Options:
-t     <device_list_file>      List of device IPs to analyze logs
-u     <username>              Device username
-p     <password>              Device password
--targets     <device_list_file>      List of device IPs to analyze logs
-username     <username>              Device username
-password     <password>              Device password


Example Run:
me@my_computer# python3 junos_core_dump_check_multidut.py -t dut_list.txt -u user123 -p pass123




Analyzing target host 10.0.0.11:
Sending command: show system core-dumps | no-more

################################################
############# Existing Core Dumps ##############
################################################
Last login: Sat Apr 15 03:04:46 2023 from 10.0.0.49
--- JUNOS 18.2R1.9 Kernel 64-bit  JNPR-11.0-20180614.6c3f819_buil
show system core-dumps | no-more
don@milnet-r1> show system core-dumps | no-more
-rw-r--r--  1 root  wheel    8074005 Dec 2  08:29 /var/crash/core.J-UKERN.mpc0.1669969759.14814.gz
-rw-r--r--  1 root  wheel    8026040 Apr 3  15:13 /var/crash/core.J-UKERN.mpc0.1680534783.9770.gz
-rw-r--r--  1 root  wheel    7853531 Apr 4  04:29 /var/crash/core.J-UKERN.mpc0.1680582533.23426.gz
-rw-r--r--  1 root  wheel    8157128 Apr 7  16:04 /var/crash/core.J-UKERN.mpc0.1680883383.9880.gz
-rw-r--r--  1 root  wheel    1877439 Apr 13 11:22 /var/crash/core.J-UKERN.mpc0.1681384952.18278.gz
/var/tmp/*core*: No such file or directory
/var/tmp/pics/*core*: No such file or directory
/var/crash/kernel.*: No such file or directory
/var/jails/rest-api/tmp/*core*: No such file or directory
/tftpboot/corefiles/*core*: No such file or directory
total files: 5

don@milnet-r1>




Analyzing target host 10.0.0.21:
Sending command: show system core-dumps | no-more

No core dumps present on device




Analyzing target host 10.0.0.31:
Sending command: show system core-dumps | no-more

No core dumps present on device
