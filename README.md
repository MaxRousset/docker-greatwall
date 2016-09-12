Unbound (with DNSSEC validation and blocking sites)
===========

Fork from https://github.com/obi12341/docker-unbound


The list of hosts blocked is set from a hosts file

Default hosts file from https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-porn-social/hosts


If you dont want blocking properties just use :
    
    https://github.com/obi12341/docker-unbound


You can find various hosts file :

    https://github.com/StevenBlack/hosts

For now you can only use hosts file fomated with 0.0.0.0 not 127.0.0.1


# Running

Just use this command to start the container. Unbound will listen on port 53/udp.

```docker run -d -p 53:53/udp -p 53:53 justtolaunch/unbound-greatwall``

(optional)
Set your own hosts file url to chose what to block

```docker run -d -p 53:53/udp -p 53:53 -e HOSTS_URL=http://your.url  justtolaunch/unbound-greatwall```

(optional)
If you want to override the nameserver in the unbound container, you can use:

```docker run -d -p 53:53/udp -p 53:53 --dns="127.0.0.1" justtolaunch/unbound-greatwall```

# Configuration
These options can be set via the environment variable -e flag:
- **HOSTS_URL**: Set the hosts file url. (Default: "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-porn-social/hosts")
- **DO_IPV6**: Enable or disable ipv6. (Default: "yes", Possible Values: "yes, no")
- **DO_IPV4**: Enable or disable ipv4. (Default: "yes", Possible Values: "yes, no")
- **DO_UDP**: Enable or disable udp. (Default: "yes", Possible Values: "yes, no")
- **DO_TCP**: Enable or disable tcp. (Default: "yes", Possible Values: "yes, no")
- **VERBOSITY**: Verbosity number, 0 is least verbose. (Default: "0", Possible Values: "<integer>")
- **NUM_THREADS**: Number of threads to create. 1 disables threading. (Default: "1", Possible Values: "<integer>")
- **SO_RCVBUFF**: Buffer size for UDP port 53 incoming. Use 4m to catch query spikes for busy servers. (Default: "0", Possible Values: "<integer>")
- **SO_SNDBUF**: Buffer size for UDP port 53 outgoing. Use 4m to handle spikes on very busy servers. (Default: "0", Possible Values: "<integer>")
- **SO_REUSEPORT**: Use SO_REUSEPORT to distribute queries over threads. (Default: "no", Possible Values: "yes, no")
- **EDNS_BUFFER_SIZE**: EDNS reassembly buffer to advertise to UDP peers. 1480 can solve fragmentation (timeouts). (Default: "4096", Possible Values: "<integer>")
- **MSG_CACHE_SIZE**: The amount of memory to use for the message cache. Plain value in bytes or you can append k, m or G. (Default: "4m", Possible Values: "<integer>")
- **RRSET_CACHE_SIZE**: The amount of memory to use for the RRset cache. Plain value in bytes or you can append k, m or G. (Default: "4m", Possible Values: "<integer>")
- **CACHE_MIN_TTL**: The time to live (TTL) value lower bound, in seconds. If more than an hour could easily give trouble due to stale data. (Default: "0", Possible Values: "<integer>")
- **CACHE_MAX_TTL**: The time to live (TTL) value cap for RRsets and messages in the cache. Items are not cached for longer. In seconds. (Default: "86400", Possible Values: "<integer>")
- **CACHE_MAX_NEGATIVE_TTL**: The time to live (TTL) value cap for negative responses in the cache. (Default: "3600", Possible Values: "<integer>")
- **HIDE_IDENTITY**: Enable to not answer id.server and hostname.bind queries. (Default: "no", Possible Values: "yes, no")
- **HIDE_VERSION**: Enable to not answer version.server and version.bind queries. (Default: "no", Possible Values: "yes, no")
- **STATISTICS_INTERVAL**: print statistics to the log (for every thread) every N seconds. (Default: "0", Possible Values: "0, 1")
- **STATISTICS_CUMULATIVE**: enable cumulative statistics, without clearing them after printing. (Default: "no", Possible Values: "yes, no")
- **EXTENDED_STATISTICS**: enable extended statistics (query types, answer codes, status) printed from unbound-control. (Default: "no", Possible Values: "yes, no")
- **INTERFACE**: Sets the interface to listen on useful when using --net=host (Default 0.0.0.0, Possible Values: "<ipaddress>", "<ipaddress>@<port>")
