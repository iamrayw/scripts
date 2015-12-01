#!/usr/bin/perl
#nslookup.pl by iamrayw
#create lists.hosts file in running directory. IPs need to be return carriage delimated.

open (HOSTLIST,"lists.hosts");
@hosts = <HOSTLIST>;

foreach $host(@hosts) {
$results = `nslookup $host`;
chomp ($host);
print ("Results for $host:\n");
print ("=" x 50,"\n");
print ("$results\n\n");
}
close (HOSTLIST);
