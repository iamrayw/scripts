#!/usr/bin/perl

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
