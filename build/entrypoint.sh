#!/bin/bash
CONF='/etc/bind/named.conf'

function createNamedConf(){
    local ip=`hostname -i`
	cat <<EOF > $CONF
acl "tuimacnet" {
    10.3.0.0/16;
    172.17.0.0/16;
};

options {
    listen-on port 53 {
        127.0.0.1;
		${ip};
    };
    listen-on-v6 { none; };
    allow-query     { localhost; tuimacnet; };
    allow-query-cache { localhost; tuimacnet; };
    allow-recursion { localhost; tuimacnet; };
    forwarders{
        10.3.0.2;
        8.8.8.8;
        8.8.4.4;
    };
    forward first;
    recursion yes;
};

logging {
    channel default_debug {
        file "/var/log/bind9.log";
        severity dynamic;
    };
};

zone "tuimac.private" IN {
    type master;
    file "/etc/bind/named/tuimac.private";
    allow-update { none; };
};
EOF
    cat $CONF
}

function startDNS(){
    /usr/sbin/named -c /etc/bind/named.conf -g -u root
    [[ $? -ne 0 ]] && { echo 'Starting Bind9 was failed.'; exit 1; }
}

function main(){
    createNamedConf
    startDNS
}

main
