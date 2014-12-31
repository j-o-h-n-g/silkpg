create server multicore_silk foreign data wrapper multicorn
options (
wrapper 'silkpg.SilkDataWrapper',
siteconf '/home/john/Development/SiLK-LBNL-05/silk.conf', rootdir '/home/john/Development/SiLK-LBNL-05');


CREATE FOREIGN TABLE silk (    application int, bytes bigint, classname varchar, classtype_id int, dip inet, dport int, duration interval,  etime timestamp, initial_tcpflags varchar, icmpcode int, icmptype int, input int, nhip inet, packets bigint, protocol int, sensor varchar, sensor_id int, session_tcpflags varchar, sip inet, sport int, stime timestamp, tcpflags varchar, timeout_killed boolean, timeout_started boolean, typename varchar, uniform_packets boolean ) server multicorn_silk;
