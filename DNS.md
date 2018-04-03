**INTRODUCTION** **TO** **THE** **DNS** **SYSTEM**

> Tran Thi Dung
>
> Overview

• Introduction to the DNS • DNS Components

• DNS Structure and Hierarchy

> DNS History (1)

• ARPANET utilized a central file HOSTS.TXT – Contains names to
addresses mapping

> – Maintained by SRI’s NIC (*Stanford-Research-Institute:*
> *Network-Information-Center)*

• Administrators email changes to NIC – NIC updates HOSTS.TXT
periodically

• Administrators FTP (download) HOSTS.TXT

> DNS History (2)

• As the system grew, HOSTS.TXT had problems with:

> – Scalability (traffic and load) – Name collisions
>
> – Consistency

• In 1984, Paul Mockapetris released the first version (RFCs 882 and
883, superseded by 1034 and 1035 …)

> The DNS is…

• The “Domain Name System”

• What Internet users use to reference anything by name on the Internet

• The mechanism by which Internet software translates names to
attributes such as addresses

> DNS as a Lookup Mechanism

• Users generally prefer names to numbers

• Computers prefer numbers to names

• DNS provides the mapping between the two – I have “x”, give me “y”

> DNS as a Database

• Keys to the database are “domain names” – www.foo.com,
18.in-addr.arpa, 6.4.e164.arpa

• Over 200,000,000 domain names stored

• Each domain name contains one or more attributes

> – Known as “resource records”

• Each attribute individually retrievable

> The DNS is also…

• A globally distributed, scalable, reliable database • Comprised of
three components

> – A “name space”
>
> – Servers making that name space available
>
> – Resolvers (clients) which query the servers about the name space
>
> Global Distribution

• Data is maintained locally, but retrievable globally

> – No single computer has all DNS data

• DNS lookups can be performed by any device

• Remote DNS data is locally cachable to improve performance

> Loose Coherency

• Each version of a subset of the database (a zone) has a serial number

> – The serial number is incremented on each database change

• Changes to the master copy of the database are propagated to replicas
according to timing set by the zone administrator

• Cached data expires according to timeout set by zone administrator

> Scalability

• No limit to the size of the database • No limit to the number of
queries

> – Tens of thousands of queries handled easily every second

• Queries distributed among masters, slaves, and caches

> Reliability

• Data is replicated

– Data from master is copied to multiple slaves • Clients can query

> – Master server
>
> – Any of the copies at slave servers

• Clients will typically query local caches

• DNS protocols can use either UDP or TCP

> – If UDP, DNS protocol handles retransmission, sequencing, etc.
>
> Dynamicity

• Database can be updated dynamically – Add/delete/modify of any record

> – Only master can be dynamically updated

• Modification of the master database triggers replication

> Overview

• Introduction to the DNS • DNS Components

> – The name space – The servers
>
> – The resolvers

• DNS Structure and Hierarchy • The DNS in Context

> The Name Space

• The *name* *space* is the structure of the DNS database – An inverted
tree with the root node at the top

• Each node has a label

> – The root node has a null label, written as “”
>
> Domain Names

• A *domain* *name* is the sequence of labels from a node to the root,
separated by dots (“.”s), read left to right

> – The name space has a maximum depth of 127 levels – Domain names are
> limited to 255 characters in length

• A node’s domain name identifies its position in the name space

> Subdomains

• One domain is a subdomain of another if its domain name ends in the
other’s domain name

> – So *sales.nominum.com* is a subdomain of • *nominum.com* *&* *com*
>
> – *nominum.com* is a subdomain of *com*
>
> Delegation

• Administrators can create subdomains to group hosts – According to
geography, organizational affiliation etc.

• An administrator of a domain can delegate responsibility for managing
a subdomain to someone else

> – But this isn’t required

• The parent domain retains links to the delegated subdomains

> – The parent domain “remembers” who it delegated the subdomain too
>
> Dividing a Domain into Zones nominum.com
>
> domain
>
> nominum.com zone

rwc.nominum.com zone

ams.nominum.com zone

> Overview

• Introduction to the DNS • DNS Components

> – The name space – The servers
>
> – The resolvers

• DNS Structure and Hierarchy • The DNS in Context

> Name Servers

• Name server answeres “DNS” questions

• Name servers store information about the name space in units called
“zones”

> – The name servers that load a complete zone are said to “have
> authority for” or “be authoritative for” the zone

• Usually, more than one name server are authoritative for the same zone

> – This ensures redundancy and spreads the load

• Also, a single name server may be authoritative for many zones

> Name Servers and Zones

128.8.10.5 serves data for both nominum.com and isc.org zones

> 202.12.28.129 serves data for nominum.com zone only
>
> 204.152.187.11 serves data for isc.org zone only
>
> **Name** **Servers**
>
> 128.8.10.5
>
> 202.12.28.129

204.152.187.11

> **Zones**

nominum.com

> isc.org
>
> Types of Name Servers

• Two main types of servers

> – Authoritative – maintains the data • Master – where the data is
> edited
>
> • Slave – where data is replicated to
>
> – Caching – stores data obtained from an authoritative server

• No special hardware necessary

> Authoritative name server

• The master server normally loads the data from zone file • A slave
server normally replicates the data from

> the master via zone transfer
>
> Recursive servers

• Recursive servers do the actual lookups; they ask questions to the DNS
on behalf of the clients.

• Answers are obtained from authoritative servers but the answers
forwarded to the clients are marked as not authoritative

• Answers are stored for future reference in the cache

> Overview

• Introduction to the DNS • DNS Components

> – The name space – The servers
>
> – The resolvers

• DNS Structure and Hierarchy • The DNS in Context

> Resolvers

• *Resolver* *ask* *the* *question* *to* *DNS* *system* *on* *behalf*
*of* *the* *application*

> Overview

• Introduction to the DNS • DNS Components

• DNS Structure and Hierarchy • The DNS in Context

> The Root Nameservers

• The root zone file lists the names and IP addresses of the
authoritative DNS servers for all top-level domains (TLDs)

• The root zone file is published on 13 servers, “A” through “M”, around
the Internet

• Root name server operations currently provided by volunteer efforts by
a very diverse set of organizations

> Top-level Domain servers

• TLD divided the internet domain name space organizationally into 7
domains:

> – Com, edu, gov, mil, net, org, int

• Storing TLDs’ address information

> The Resolving Process

• Let’s look at the resolving process step-by-step:

> annie.west.sprockets.com
>
> ping www.nominum.com.
>
> The Resolving Process
>
> • The workstation *annie* asks its configured name server, *dakota,*
> for *www.nominum.com’s* address
>
> dakota.west.sprockets.com
>
> What’s the IP address of www.nominum.com?

annie.west.sprockets.com

> ping www.nominum.com.
>
> The Resolving Process

• The name server *dakota* asks a root name server, *m*, for
*www.nominum.com’s* address

> m.root-servers.net
>
> dakota.west.sprockets.com
>
> What’s the IP address of www.nominum.com?
>
> annie.west.sprockets.com
>
> ping www.nominum.com.
>
> The Resolving Process

• The root server *m* refers *dakota* to the *com* name servers • This
type of response is called a “referral”

> m.root-servers.net
>
> dakota.west.sprockets.com

Here’s a list of the com name servers. Ask one of them*.*

> annie.west.sprockets.com
>
> ping www.nominum.com.
>
> The Resolving Process

• The name server *dakota* asks a *com* name server, *f*, for
*www.nominum.com’s* address

> What’s the IP address of www.nominum.com?
>
> m.root-servers.net
>
> dakota.west.sprockets.com
>
> f.gtld-servers.net
>
> annie.west.sprockets.com
>
> ping www.nominum.com.

The Resolving Process • The *com* name server *f* refers *dakota* to the

> *nominum.com* name servers
>
> m.root-servers.net
>
> dakota.west.sprockets.com

Here’s a list of the nominum.com name servers. Ask one of them*.*

> f.gtld-servers.net
>
> annie.west.sprockets.com
>
> ping www.nominum.com.
>
> The Resolving Process

• The name server *dakota* asks a *nominum.com* name server,
*ns1.sanjose*, for *www.nominum.com’s* address

> What’s the IP address of www.nominum.com?
>
> m.root-servers.net
>
> dakota.west.sprockets.com
>
> ns1.sanjose.nominum.net
>
> f.gtld-servers.net
>
> annie.west.sprockets.com
>
> ping www.nominum.com.

The Resolving Process • The *nominum.com* name server *ns1.sanjose*

> responds with *www.nominum.com’s* address
>
> m.root-servers.net
>
> dakota.west.sprockets.com
>
> Here’s the IP address for www.nominum.com

ns1.sanjose.nominum.net

> f.gtld-servers.net
>
> annie.west.sprockets.com
>
> ping www.nominum.com.
>
> The Resolving Process

• The name server *dakota* responds to *annie* with *www.nominum.com’s*
address

> Here’s the IP address for www.nominum.com
>
> m.root-servers.net
>
> dakota.west.sprockets.com
>
> ns1.sanjose.nominum.net
>
> f.gtld-servers.net
>
> annie.west.sprockets.com
>
> ping www.nominum.com.
>
> Resolving Process (Caching)

• After the previous query, the name server *dakota* now knows: – The
names and IP addresses of the *com* name servers

> – The names and IP addresses of the *nominum.com* name servers – The
> IP address of *www.nominum.com*

• Let’s look at the resolving process again

> annie.west.sprockets.com
>
> ping **ftp**.nominum.com.

Resolving Process (Caching) • The workstation *annie* asks its
configured name

> server, *dakota,* for *ftp.nominum.com’s* address
>
> m.root-servers.net
>
> dakota.west.sprockets.com
>
> What’s the IP address of ftp.nominum.com?

ns1.sanjose.nominum.net

> f.gtld-servers.net
>
> annie.west.sprockets.com
>
> ping ftp.nominum.com.
>
> Resolution Process (Caching)

• *dakota* has cached a NS record indicating *ns1.sanjose* is an

> *nominum.com* name server, so it asks it for *ftp.nominum.com’s*
> address
>
> What’s the IP address of ftp.nominum.com?
>
> m.root-servers.net
>
> dakota.west.sprockets.com
>
> ns1.sanjose.nominum.net
>
> f.gtld-servers.net
>
> annie.west.sprockets.com
>
> ping ftp.nominum.com.

Resolution Process (Caching) • The *nominum.com* name server
*ns1.sanjose*

> responds with *ftp.nominum.com’s* address
>
> m.root-servers.net
>
> dakota.west.sprockets.com
>
> Here’s the IP
>
> address for ns1.sanjose.nominum.net ftp.nominum.com
>
> f.gtld-servers.net
>
> annie.west.sprockets.com
>
> ping ftp.nominum.com.

Resolution Process (Caching) • The name server *dakota* responds to
*annie* with

> *ftp.nominum.com’s* address
>
> Here’s the IP address for ftp.nominum.com
>
> m.root-servers.net
>
> dakota.west.sprockets.com
>
> ns1.sanjose.nominum.net
>
> f.gtld-servers.net
>
> annie.west.sprockets.com
>
> ping ftp.nominum.com.
>
> Resource records (Detail)

• Format {name, ttl, class,type, rdata}

• TTL is timer used in caches

> • An indication for how long the data may be used

• Data that is expected to be “stable” can have high TTLs • IN class is
widest used

• There are mutilple types of RR

• Everything behind the type identifier is called rdata

> Resource records
>
> CNAME

Tạo một bản ghi thay thế hay biệt danh cho một bản ghi

> CNAME WWW=Web
>
> b1

DNS server

> Địa chỉ ip của WWW là gì?
>
> Computer Web 1
>
> Web 2

Mail exchange (MX) • Định danh mail server cho dns name

> Mx record cho xxx.com là gì?

Mail1.xxx.com

> Mx record cho xxx.com
>
> Sending Mail server

Mx record M1.xxx.com mail1

DNS mail1 server

> Mail exchange

• Có nhiều mx record cho cùng một dns name • Độ ưu tiên thấp nhất được
dùng đầu tiên

• Nếu cùng độ ưu tiên thì mx sẽ được chọn ngẫu nhiên

• Nếu email gửi đến server có độ ưu tiên thấp bị lỗi thì Mx sẽ gửi độ ưu
tiên tiếp theo cho mail server

> Reference

\*referred to slides by David Conrad at nominum.com\\
