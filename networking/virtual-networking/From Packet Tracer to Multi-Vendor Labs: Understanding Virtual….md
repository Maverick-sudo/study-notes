# From Packet Tracer to Multi-Vendor Labs: Understanding Virtual…

## Summary

for CCNA-level switching and routing. But once you step into more advanced labs — hypervisor (runs on top of a Linux OS) — you’re suddenly faced with dozens of i86bi-linux-l2-adventerprisek9-15.1.201.bin asav981.qcow2 fortios6.2.ova which is a switch, or how ASA differs from Fortinet or Palo Alto.

## Table of Contents

  - [From Packet Tracer to Multi-Vendor Labs:](#from-packet-tracer-to-multi-vendor-labs)
  - [Understanding Virtual Images and Device Roles](#understanding-virtual-images-and-device-roles)
  - [Many networking learners begin with Cisco Packet Tracer, which is excellent](#many-networking-learners-begin-with-cisco-packet-tracer-which-is-excellent)
  - [using EVE-NG or GNS3 or PNETLABs which are all virtualization platform](#using-eve-ng-or-gns3-or-pnetlabs-which-are-all-virtualization-platform)
  - [based on QEMU/KVM running on Ubuntu/Debian. It is technically a Type 2](#based-on-qemukvm-running-on-ubuntudebian-it-is-technically-a-type-2)
  - [mysterious file names like:](#mysterious-file-names-like)
  - [PA-VM-10.1.8.ova](#pa-vm-1018ova)
  - [It can be confusing at first, especially when you're unsure which is a router,](#it-can-be-confusing-at-first-especially-when-youre-unsure-which-is-a-router)
  - [linux = Runs on Linux](#linux-runs-on-linux)
  - [l2 or l3 = Layer 2 switch or Layer 3 router](#l2-or-l3-layer-2-switch-or-layer-3-router)
  - [Based on IOS on Unix (IOU): A lightweight Cisco virtual image used](#based-on-ios-on-unix-iou-a-lightweight-cisco-virtual-image-used)
- [Mpls, Bgp](#mpls-bgp)
- [Iol-L2](#iol-l2)
- [Iol-L3](#iol-l3)
- [Ngfw)](#ngfw)
- [Csr1000](#csr1000)
- [Ios Xe](#ios-xe)
- [(1–2Gb](#12gb)
- [Ram)](#ram)
- [Bgp,](#bgp)
- [Eigrp,](#eigrp)
- [Nat, Vpn](#nat-vpn)
- [Ios Xr](#ios-xr)
- [Xr Cli](#xr-cli)
- [3Gb+)](#3gb)
- [Mpls, Is-](#mpls-is)
- [Is, Sp](#is-sp)
- [Sd-Wan /](#sd-wan)
- [4Gb Ram)](#4gb-ram)
- [+ Sd-](#sd)
  - [Cisco IOU Images for GNS3](#cisco-iou-images-for-gns3)
  - [Cisco ASA Firewall Images for GNS3](#cisco-asa-firewall-images-for-gns3)
  - [Firepower Threat Defense (NGFW)](#firepower-threat-defense-ngfw)
  - [Let’s Compare on-premises Cisco ASAv (Adaptive Security Virtual](#lets-compare-on-premises-cisco-asav-adaptive-security-virtual)
  - [Appliance) with a cloud-based Network Virtual Appliance (NVA) helps](#appliance-with-a-cloud-based-network-virtual-appliance-nva-helps)
- [Kvm)](#kvm)
  - [Cisco ASAv (On-Prem)](#cisco-asav-on-prem)
  - [FortiGate/Checkpoint VM)](#fortigatecheckpoint-vm)
  - [You can actually deploy Cisco ASAv as a Cloud NVA too. Cisco offers ASAv](#you-can-actually-deploy-cisco-asav-as-a-cloud-nva-too-cisco-offers-asav)
  - [images in AWS and Azure marketplaces that act as cloud NVAs. In that case:](#images-in-aws-and-azure-marketplaces-that-act-as-cloud-nvas-in-that-case)
  - [branding, These support modern features like SD-Access, high-throughput](#branding-these-support-modern-features-like-sd-access-high-throughput)
  - [You can use IOU-L2 or Juniper vQFX when you](#you-can-use-iou-l2-or-juniper-vqfx-when-you)
  - [need actual Layer 2 switch behavior. Though labeled “Catalyst,” these vIOS-XE](#need-actual-layer-2-switch-behavior-though-labeled-catalyst-these-vios-xe)
  - [Catalyst images act as routers, not true L2 switching platforms. Real Catalyst](#catalyst-images-act-as-routers-not-true-l2-switching-platforms-real-catalyst)
  - [switch simulation (e.g., Cat3650/3850) is typically only available via IOU](#switch-simulation-eg-cat36503850-is-typically-only-available-via-iou)
  - [images or hardware. The virtual Catalyst 8K/9K primarily supports routing,](#images-or-hardware-the-virtual-catalyst-8k9k-primarily-supports-routing)
  - [Notes per Vendor](#notes-per-vendor)
  - [Here's a comparison table between Cisco images (IOS, IOU/IOL, ASA) and](#heres-a-comparison-table-between-cisco-images-ios-iouiol-asa-and)
  - [vendors. This covers routers, switches, and firewalls — focusing on virtual](#vendors-this-covers-routers-switches-and-firewalls-focusing-on-virtual)
- [(Ios/](#ios)

---

## Content

### From Packet Tracer to Multi-Vendor Labs:

### Understanding Virtual Images and Device Roles

### Many networking learners begin with Cisco Packet Tracer, which is excellent

for CCNA-level switching and routing. But once you step into more advanced labs —
### using EVE-NG or GNS3 or PNETLABs which are all virtualization platform

### based on QEMU/KVM running on Ubuntu/Debian. It is technically a Type 2

hypervisor (runs on top of a Linux OS) — you’re suddenly faced with dozens of
### mysterious file names like:

i86bi-linux-l2-adventerprisek9-15.1.201.bin asav981.qcow2 fortios6.2.ova
### PA-VM-10.1.8.ova

### It can be confusing at first, especially when you're unsure which is a router,

which is a switch, or how ASA differs from Fortinet or Palo Alto.
### This blog is your step-by-step map to understanding these appliances —

especially how to recognize and classify them — using real images Understanding Cisco Image Naming & Evolution Cisco IOU/IOU-L2 (e.g., i86bi-linux-l2-) i86 = Intel x86 architecture bi = Built-in
### linux = Runs on Linux

### l2 or l3 = Layer 2 switch or Layer 3 router

### Based on IOS on Unix (IOU): A lightweight Cisco virtual image used

internally by Cisco for testing, later leaked and adopted for GNS3/EVE- Use Cases: Great for VLAN, STP, OSPF, BGP labs without needing full hardware emulation. Cisco Images Breakdown Image Name Category Notes c1700–c7200 series IOS Routers Legacy ISR platforms IOU/i86bi-linux-l3-* L3 Routers Virtual routers (OSPF, BGP, EIGRP capable) IOU/i86bi-linux-l2-* L2 Switches Emulated Catalyst- style switches asav* (e.g. asav981.qcow2, asav991.qcow2) ASA Firewall Modern ASAv virtual firewalls asa842-initrd.gz ASA Firewall Legacy ASA 8.x
FTD (if included) NGFW Firepower Threat Defense (optional) Cisco Router Evolution: c1700 → c7200 Image Era Description c1700 Early Entry-level ISR, basic routing only c2600 Legacy Adds modularity and more services c3725 Mid-tier Better for EIGRP/BGP labs, still old c7200 High-end Supports complex routing, VPN, multiple NICs These are router images—physical router platforms that run IOS for routing functionalities: c1700-adventerprisek9-mz.124-25d c2600-adventerprisek9-mz.124-15.T14 c2691-adventerprisek9-mz.124-15.T14 c3620-a3jk8s-mz.122-26c c3640-a3js-mz.124-25d c3660-a3jk9s-mz.124-15.T14 c3725-adventerprisek9-mz.124-15.T14 c3745-adventerprisek9-mz.124-25d c7200-adventerprisek9-mz.153-3.XB12 c7200-adventerprisek9-mz.152-4.S6 c7200-adventerprisek9-mz.124-24.T5 Abbreviation Full Meaning Explanation / Usage CSR1000v Cloud Services Router 1000 Virtual A virtualized IOS XE router used in cloud and enterprise labs; supports advanced features like VPN,
## Mpls, Bgp

IOSv Internetwork Operating System Virtual A virtual router running IOS inside a virtual machine (QEMU); good for general routing labs
IOSvL2 Internetwork Operating System Virtual Layer 2 A virtual switch running IOS; simulates L2 switching features (basic STP, VLANs) IOL IOS on Linux Lightweight IOS used internally by Cisco; often used in labs via .bin files (e.g., i86bi)
## Iol-L2

IOS on Linux Layer 2 L2 switch simulation (VLANs, STP, EtherChannel); often more feature-rich than IOSvL2
## Iol-L3

IOS on Linux Layer 3 L3 routing simulation; lighter than CSR but still powerful for labs XRv IOS XR Virtual Router Runs Cisco IOS XR (used in service provider gear); useful for MPLS, BGP SP simulations NX-OSv Nexus Operating System Virtual Nexus 9000/7000 simulator; used for data center labs ASA Adaptive Security Appliance Cisco firewall; asav is the virtual version for security labs vWLC Virtual Wireless LAN Controller Manages wireless networks; used in wireless architecture labs vNAM Virtual Network Analysis Module For network traffic analysis; not commonly used in most labs vFMC Virtual Firepower Management Center Manages Firepower security devices (e.g.,
## Ngfw)

vFTD Virtual Firepower Threat Defense Unified threat firewall platform by Cisco
Platform OS Type Target Use Case CLI Style Resource Usage Best For
## Csr1000

## Ios Xe

Cloud/ virtual branch routers Traditional IOS-like Medium
## (1–2Gb

## Ram)

Routing,
## Bgp,

## Eigrp,

## Nat, Vpn

IOS XRv / XRv9000
## Ios Xr

Service provider core routers
## Xr Cli

(different flow) High (2–
## 3Gb+)

## Mpls, Is-

## Is, Sp

Labs Catalyst 8000v
## Ios Xe

## Sd-Wan /

advanced enterprise routing
## Ios Xe

Medium– High CCNP Enterprise Core, SD- WAN concepts Catalyst 9000v
## Ios Xe

Modern campus switches (Access/ Core)
## Ios Xe

with DNA/ SD- Access High (2–
## 4Gb Ram)

Switching
## + Sd-

Access (Advance d Labs) ISRv (ISR 1000v)
## Ios Xe

Software- based ISR router
## Ios Xe

Medium HQ/ Branch routing, full IOS feature set
### Cisco IOU Images for GNS3

These are IOU (IOS on UNIX) images used in simulation and split into Layer 2 (switching) and Layer 3 (routing) roles: Image Name Role i86bi-linux-l2- adventerprise-15.1b / …- ipbasek9-15.1g Layer 2 switch i86bi-linux-l2-upk9-12.2 / …-15.0b Layer 2 switch i86bi-linux-l3-jk9s-15.0.1 / …l3- p-15.0a / …l3-p-15.0b Layer 3 router i86bi-linux- l3-tpgen-adventerprisek9-12.4 Layer 3 router
### Cisco ASA Firewall Images for GNS3

ASA stands for Adaptive Security Appliance — it replaced Cisco PIX in the
2000s and became the standard Cisco firewall platform. These are firewall virtual images (ASAv or classic ASA): ASA Image Notes asa842 Legacy ASA (8.4.2), limited memory. * asa842-initrd.gz – classic ASA 8.4.2 asav981+ Virtual ASA (ASAv), supports ASDM GUI asav981.qcow2 – ASAv 9.8.3 (also duplicate listed version 9.8.1) asav991.qcow2 – ASAv 9.9.1 asav992-32.qcow2 – ASAv 9.9.2 FTD (optional)
### Firepower Threat Defense (NGFW)

### Let’s Compare on-premises Cisco ASAv (Adaptive Security Virtual

### Appliance) with a cloud-based Network Virtual Appliance (NVA) helps

clarify how security solutions differ between traditional data centers and modern cloud environments. Key Differences: Cisco ASAv vs Cloud NVA Feature Cisco ASAv (On- Premises) Cloud NVA (e.g., Azure/AWS) Deployment Location Deployed on physical/ virtual servers in on- prem or private cloud environments (e.g., VMware, Hyper-V,
## Kvm)

Deployed in public cloud (Azure, AWS, GCP) within virtual networks (VNets/ VPCs) Purpose Acts as a virtual firewall, VPN concentrator, IPS/IDS Acts as a cloud firewall, router, IDS/ IPS, load balancer, etc. depending on vendor Control Plane Full control over OS, updates, patches Shared responsibility with cloud provider; some abstraction in management Networking Integration Connects to VLANs, physical interfaces, subnets in data centers Integrates with cloud- native constructs (e.g., Azure VNet, AWS VPC) using cloud routing tables, NICs, and UDRs
Scalability Manual scaling (CPU/ RAM/storage) or via orchestration tools Often scalable using cloud autoscaling groups, availability zones Licensing BYOL (Bring Your Own License) or Smart Licensing PAYG (Pay-as-you-go) or BYOL; cloud marketplace-based licensing Use Cases Secure on-prem apps, remote access VPN, inter-DC security Secure traffic between cloud subnets, hybrid VPN, cloud perimeter defense Performance Tuning Hardware-dependent, tuned based on hypervisor resources Cloud resource-based (VM size/SKU), optimized for IOPS and throughput High Availability (HA) Manual configuration via clustering or failover pairs Cloud-native HA (e.g., Azure Availability Zones, AWS Auto Recovery) or via cloud load balancers Example Use Cases
### Cisco ASAv (On-Prem)

Internal network segmentation in a private data center. IPSec VPN termination for remote workers. East-west firewall inside a private VMware environment. Cloud NVA (e.g., Cisco ASAv in Azure/AWS or native
### FortiGate/Checkpoint VM)

Secure ingress/egress traffic in Azure/AWS. Cloud VPN gateway in a hub-and-spoke VNet topology. IDS/IPS filtering between workloads in different subnets. ASAv Can Be Both!
### You can actually deploy Cisco ASAv as a Cloud NVA too. Cisco offers ASAv

### images in AWS and Azure marketplaces that act as cloud NVAs. In that case:

It's still ASAv software, but running inside the cloud. Integrates with cloud-native routing (UDRs, NSGs, route tables). Useful for companies wanting to extend their Cisco-based security policies into the cloud. What is Catalyst Edge 8000v/9000v? These are modern Cisco virtual routers, not switches, despite the "Catalyst"
### branding, These support modern features like SD-Access, high-throughput

routing, and full IOS-XE support — ideal for enterprise WAN simulation, but not suitable as L2 switches.
### You can use IOU-L2 or Juniper vQFX when you

### need actual Layer 2 switch behavior. Though labeled “Catalyst,” these vIOS-XE

### Catalyst images act as routers, not true L2 switching platforms. Real Catalyst

### switch simulation (e.g., Cat3650/3850) is typically only available via IOU

### images or hardware. The virtual Catalyst 8K/9K primarily supports routing,

policy, QoS, security, and other network services—akin to routers Model Function Real Hardware Equivalent C8000v * c8000v-17.06.03, catalyst8000v-17.04. 01, catalyst8000v-17.06. 01a These are software-based router appliances built on the IOS-XE platform (designed for edge/branch WAN routing). Edge router, SD-WAN,
## Ios-Xe

Catalyst 8000 Edge Platforms CAT9Kv * cat9kv-17.10.01-prd7 This is a virtualized Catalyst 9000 series router, also IOS-XE, suited for enterprise routing and policy enforcement in virtual/ cloud environments. Core routing, policy- aware Catalyst 9300/9400 (routing mode) Image Type Device Type Primary Function Catalyst 8000V Edge Virtual Router Branch/edge WAN routing (SD-WAN, secure connectivity, advanced services) Catalyst 9000V Virtual Router Enterprise/core routing, policy management, SD- Access, virtualization use-cases
### Notes per Vendor

### Here's a comparison table between Cisco images (IOS, IOU/IOL, ASA) and

equivalent images or virtual platforms from other popular network/security
### vendors. This covers routers, switches, and firewalls — focusing on virtual

images commonly used in GNS3, EVE-NG, or labs. Cross-Vendor Comparison Table Functio Cisco
## (Ios/

## Iou/

## Asa)

Fortinet (FortiG ate) Palo Alto
## (Pa-

VM) MikroTi (Router OS) Sophos
## (Xg/

## Utm)

Juniper (vSRX/ vMX) Router IOS (c1700– c7200) Great for routing protocol s (OSPF,
## Bgp,

etc.)
## Iou L3

(i86bi- linux-l3) Lightwei ght, fast for
## Gns3/

EVE labs. Limited real switchin function Routing
## + Utm

✔ Some static/
## Dhcp +

NAT ✔ Full router
## (Bgp,

## Ospf)

Limited (mainly gateway ✔ vMX (full routing stack) Switch
## - Iou L2

(i86bi- linux- l2)- Limited L2 in vIOS ✖ Not a switch ✖ Not a switch Router with bridging ✔ vQFX (for switchin
Firewall
## - Asa

8.x/9.x-
ASAv (9.x series)- FTD (optiona Classic firewall, support s NAT,
## Vpn,

ACLs. ASAv adds
## Ngfw-

like features (with FirePOW
## Er).

FortiGat e VM
## (Ngfw,

## Utm)

*suppor
t full NGFW function ality.
## ✔ Pa-

NGFW (AppID, Threats) Requires more
## Cpu/

## Ram.

✖ Basic
## Nat/

firewall only Sophos XG/UTM firewall ✔ vSRX (Juniper
## Ngfw/

## Ips)

NGFW Feature Partial (with FirePOW
## Er/Ftd)

✔ App control,
## Ssl,

## Ips, Av

✔ App- ID, WildFire , Threat ✖ Basic filtering
## ✔ Av,

IPS, App Ctrl Unified security routing GUI
## Asa:

ASDMIO
## S: Cli/

HTTP (limited) FortiOS Web GUI Panora ma / WebUI WinBox
- WebUI
WebAd min ✔ J- Web or CLI License -Free Lab Use IOU (limited)
## , Ios

(older) FortiGat e 6.2.x free eval
## ✔ Pa-

VM trial device) RouterO S free
## (Chr

trial) ✔ 30- day XG Home Trial ✔ vSRX/ vMX trial Device Role Breakdown with Image Options Role Function Cisco Image(s) Other Vendor Image(s)
Edge Firewall
## Ngfw, Nat,

## Vpn, Acl

asav9xx.qcow2,
## Asa 842, Ftd

(optional) fortios.qcow2, PA-VM.ova, sophosXG.qcow 2, vSRX Core Router
## Ospf, Bgp,

static routes c7200, IOU-L3, c8000v, cat9kv RouterOS, vMX, FortiGate (routing), PA- VM (basic) L2 Switch VLANs, trunking, STP IOU-L2, limited L2 in cat9kv vQFX (Juniper), MikroTik (limited bridging only) PCs/Hosts Traffic generation/ testing VPCS, TinyCore, Alpine, Windows.qcow2 Server Web, DNS,
## Dhcp, Ad

Alpine, Ubuntu, Windows Server
### Using a Mac with EVE-NG (running in VMware Fusion Player) is fully

### supported, and the process is similar to Windows. Here's how to do everything

the Mac way, including the equivalent SCP/SFTP method and correct image directory paths.
### Transfer Images from macOS to EVE-NG using SCP or SFTP

### Method 1: Using Terminal (SCP)

### You can use your Mac’s built-in Terminal to copy files into EVE-NG over SSH:

scp your-image-file.qcow2 root@<eve-ng-ip>:/opt/unetlab/addons/qemu/
### <image-folder>/

### Replace <eve-ng-ip> with your EVE-NG VM’s IP (e.g. 192.168.56.101)

<image-folder> should follow naming rules like: asav-981 iosv-152 fortinet-6.2.3 Example:
### scp asav981.qcow2 root@192.168.56.101:/opt/unetlab/addons/qemu/asav-981/

### You’ll be prompted for the root password (default: eve)

Method 2: Using Cyberduck (GUI Alternative to FileZilla) Download Cyberduck for macOS
### Connect using:

Protocol: SFTP (SSH File Transfer Protocol) Server: eve-ng-ip Username: root Password: eve Navigate to:
/opt/unetlab/addons/qemu/
### Create a new folder (e.g. asav-981)

Upload your .qcow2 or .vmdk image inside.
### Correct File Path for Router/Switch/Firewall Images

### All image files go into:

/opt/unetlab/addons/qemu/<image-folder-name>/ Examples: Device Folder Name Path Cisco IOSv iosv-152 /opt/unetlab/addons/ qemu/iosv-152/ Cisco IOU (L2) i86bi-linux-l2 /opt/unetlab/addons/ iol/bin/ (different) ASA Firewall asav-981 /opt/unetlab/addons/ qemu/asav-981/ Fortinet FW fortinet-6.2 /opt/unetlab/addons/ qemu/fortinet-6.2/ Palo Alto pa-10.1.8 /opt/unetlab/addons/
### qemu/pa-10.1.8/

### After Uploading — Fix Permissions & Reload

### Run these commands via SSH to fix permissions and parse the image:

### /opt/unetlab/wrappers/unl_wrapper -a fixpermissions

Then refresh your EVE-NG web UI and the new image should appear when adding a node. Vendor Device Type OSI Layer Examples from Repo Notes Cisco Router Layer 3 iosv, iosv-l3, c7200, c3725 Virtual and emulated routers Switch Layer 2 i86bi-linux- l2, iosvl2 IOU-based and IOSv-L2 Firewall Layer 3/4 asav, asa842 Cisco ASA Virtual (ASAv) Juniper Router/ Switch L2/L3 vSRX, vMX, vQFX vSRX = firewall, vMX = router Fortinet Firewall Layer 3/4 fortinet-6.x FortiGate NGFW virtual appliances
Palo Alto Firewall Layer 3/4 pa-vm,
## Pa-10.1.8

Full-featured NGFW Checkpoint Firewall Layer 3/4 checkpoint-
## R80.30

GAiA OS- based firewall Arista Switch Layer 2 vEOS-lab Used as virtual switch VyOS Router/ Firewall Layer 3 vyos-1.1.7 Open- source routing and firewall MikroTik Router Layer 3 chr-6.40.3 Cloud Hosted Router Load Balancer Layer 4–7
## Big-Ip

Application delivery controller Huawei Router/ Switch Layer 2/3 eNSP, AR- series,
## Ce12800

If supported, rare in repo Device Vendor Device Type Folder Name Path Cisco Router iosv-152 /opt/unetlab/ addons/qemu/ iosv-152/ Cisco Switch i86bi-linux-l2 /opt/unetlab/ addons/iol/bin/ (IOU specific) Cisco Firewall asav-981 /opt/unetlab/ addons/qemu/ asav-981/ Cisco Legacy RTR c7200 /opt/unetlab/ addons/ dynamips/ (Dynamips) Juniper Firewall vsrx-20.3R1.8 /opt/unetlab/ addons/qemu/ vsrx-20.3R1.8/ Juniper Switch vqfx-re /opt/unetlab/ addons/qemu/ vqfx-re/
Fortinet Firewall fortinet-6.2 /opt/unetlab/ addons/qemu/ fortinet-6.2/ Palo Alto Firewall pa-10.1.8 /opt/unetlab/ addons/qemu/ pa-10.1.8/ Checkpoint Firewall checkpoint-R80 /opt/unetlab/ addons/qemu/ checkpoint-
## R80/

Arista Switch veos-lab /opt/unetlab/ addons/qemu/ veos-lab/ VyOS Router vyos-1.1.7 /opt/unetlab/ addons/qemu/ vyos-1.1.7/ MikroTik Router chr-6.40.3 /opt/unetlab/ addons/qemu/ chr-6.40.3/ Load Balancer bigip-ve /opt/unetlab/ addons/qemu/ bigip-ve/ All legacy Cisco router platforms like c1700, c2600, c2691, c3725, and c7200 use Dynamips
### Important:

### Dynamips is CPU-intensive and doesn’t scale well, making it mostly

useful for small lab scenarios or legacy certification studies.
### Modern labs should use IOSv, IOSv-L3, or cat8000v where

possible, especially when simulating modern features like OSPFv3, EIGRP for IPv6, or Layer 3 switching. IOSv/IOSv-L3/L2: Best for CCNA/CCNP route/switch training in EVE-NG — easy to set up. C8000v: Emulates real-world enterprise routers with full IOS XE — great for advanced WAN/SD-WAN scenarios.
### Cat9Kv: The most realistic Layer 2/3 Catalyst switch you can run virtually

— excellent for enterprise switching labs. Platform Model Folder Path Type Notes c1700 1710/1720 /opt/unetlab/ addons/ dynamips/ Router Very old ISR platform, minimal features
c2600 2610/2620 /opt/unetlab/ addons/ dynamips/ Router Better interface support, still legacy c2691 2691 /opt/unetlab/ addons/ dynamips/ Router Higher throughput, limited by software image c3725 3725 /opt/unetlab/ addons/ dynamips/ Router Supported in many CCNA/ CCNP books for basic labs c7200 7200 series /opt/unetlab/ addons/ dynamips/ Router Highest capacity in Dynamips, supports PA interfaces
### Calculating IDLE-PC:

### First time it is recommended to check Dynamips image IDLE PC usage. The

### Idle-PC value is a Dynamips-specific optimization setting used to reduce

### CPU usage when emulating Cisco routers like c7200, c3725, c1700, etc. It only

applies to Dynamips images, not to modern IOSv, C8000v, or Cat9Kv platforms. Why Is Idle-PC Important?
### Without setting an Idle-PC value, Dynamips emulation will peg your CPU at

### 100% — even if the router is doing nothing. This makes the lab sluggish and

### can overheat or drain system resources. Idle-PC tells Dynamips which CPU

instruction pattern to treat as "idle," so it can pause CPU execution when the router is idle. When and How to Set Idle-PC (Mac-compatible Steps): When?
### Only for Dynamips images: c1700, c2600, c2691, c3725, c7200

You need to set it once per image version, and EVE-NG will reuse it
### How to Set Idle-PC in EVE-NG

You'll do this through the EVE-NG web GUI after dragging a Dynamips router into your lab. Start the router node (e.g., c7200) in the lab. Right-click the node → choose "Idle-PC Finder"
EVE-NG will pause and show you a list of values (e.g., 0x6047c1f4,
### 0x607478cc, etc.)

Pick the one marked with a * (best recommended). If none have a *, try the first one. Restart the node and check CPU usage. If CPU usage is still high, repeat and try another value from the list. Tip: How to Monitor CPU Usage (Mac) Use Activity Monitor or run in Terminal:
### top -o cpu

### Look for qemu-system-x86_64 or Dynamips processes. After applying a good

Idle-PC value, CPU should drop significantly. Summary Table Item Applies To Required? Purpose Idle-PC Value c1700–c7200 (Dynamips) Yes Prevent 100% CPU usage Set From GUI Yes (Right-click) EVE-NG finds optimal values Modern IOSv Images Use virtualization, not emu
### IOL images must end with the “.bin” extension and must be executable. EVE-NG

### Pro has not required to generate iourc license. License must be stored under

### the same path. IOU/IOL license is bound to the hostname and domain name of

the server. A test should be made to check if IOU/IOL images can run properly.
### Google for how to create iourc license file. Bellow is an EXAMPLE how it should

### look like: cat /opt/unetlab/addons/iol/bin/iourc [license] [license] Eve-ng =

### 972f30267ef51616; If the IOL/IOU instance doesn’t start, then you won’t be

### able to use IOL/IOU nodes inside EVE. This is critical knowledge for anyone

using Cisco IOU/IOL images in EVE-NG Community Edition (non-Pro). Understand the licensing mechanism and setup steps for IOU/IOL images. The iourc license file belongs in the /opt/unetlab/addons/iol/ directory.
### Purpose: This folder holds Cisco IOL (IOS on Linux) images. iourc file:

Required here to authorize and enable IOL images to run in EVE-NG.
### Additional Notes:

Make sure the iourc file is owned by root and has the correct
### permissions:

chown root:root /opt/unetlab/addons/iol/iourc chmod 644 /opt/unetlab/addons/iol/iourc
### After placing it:

/opt/unetlab/wrappers/unl_wrapper -a fixpermissions
Where exactly does the iourc file go? Within the iol image directory (/opt/unetlab/addons/iol/), you may see two
### subdirectories:

/opt/unetlab/addons/iol/bin/ – holds the actual .bin IOL images. /opt/unetlab/addons/iol/lib/ – rarely used unless the image depends on external libraries.
### The **iourc** license file does not go into bin/ or lib/. It should be placed

### directly in the root of the iol directory:

### Cisco IOU/IOL Image Setup in EVE-NG (Community)

### IOL (IOS on Linux) or IOU (IOS on Unix) are lightweight Cisco images primarily

### used internally at Cisco. They’re also supported in EVE-NG, but require a

license file to run in the Community Edition. Key Rules for IOU/IOL Setup Requirement Details File Extension Must end with .bin (e.g., i86bi- linux-l2-ipbasek9-15.1g.bin) Permissions Must be executable (chmod +x) License File Required in Community Edition (not needed in Pro) License Path /opt/unetlab/addons/iol/bin/iourc License Format Must match the EVE-NG hostname (e.g., unl01) Image Folder Location /opt/unetlab/addons/iol/bin/ Image Testing Required to verify it runs (drag IOL into a lab and start it)
### License File Example

Create the file at: /opt/unetlab/addons/iol/bin/iourc With this content (example): [license]
### “Hostname” = 0123456789abcdef;

### Replace the license key with a valid 16-character hex string (you can

find generators online or in forum discussions — typically for lab use only)
### Set Executable Permissions

### Make sure your IOL images are executable:

### chmod +x /opt/unetlab/addons/iol/bin/*.bin

Also apply correct ownership (for EVE-NG compatibility):
/opt/unetlab/wrappers/unl_wrapper -a fixpermissions
### Verifying IOL Functionality

After importing an IOL image and setting the license file, drag the device into a topology Power it on If it fails to boot, it likely means: The license file is incorrect The hostname mismatch
### The .bin file is not executable

### Understanding QEMU Image Naming and Folder

### Structure in EVE-NG (Beginner Friendly Guide)

### If you're new to EVE-NG and coming from tools like Cisco Packet Tracer, the

### transition to working with real virtual network appliances can feel

### overwhelming. One common issue for beginners is incorrect QEMU image

folder names or filenames, which prevents appliances from showing up in the EVE-NG web UI. In this post, you’ll learn how to correctly organize QEMU images, using reliable references from: EVE-NG Documentation – QEMU Image Naming
### Why Image Folder Name Matters

EVE-NG scans for specific folder names inside the directory:
### /opt/unetlab/addons/qemu/

### Each folder name must match EVE’s expected naming convention (usually

lowercase, no spaces), or the image won’t appear in the EVE-NG UI when adding nodes to your topology. General Folder + File Structure
### When uploading .qcow2 images to EVE-NG:

/opt/unetlab/addons/qemu/<folder_name>/<correct_image_name>.qcow2 Then run:
### /opt/unetlab/wrappers/unl_wrapper -a fixpermissions

This corrects ownership and permission errors (root:root, 755). Folder Name and Image File Naming Table (Top QEMU Appliances) Device/ Platform Folder Name Required Filename Notes Cisco IOSv (Router) vios vios.qcow2 Lightweight IOS virtual router
Cisco IOSvL2 (Switch) iol-switch virtioa.qcow2 L2 features, not full Cat9K Cisco IOS-XRv xrv xrv.qcow2 IOS-XR based image Cisco CSR1000v csr1000v csr1000v- universalk9.qco High-end virtual router Cisco ASAv asav asav.qcow2 Cisco ASA virtual firewall Cisco NX-OSv nxosv nxosv.qcow2 Nexus platform Cisco Catalyst 8000v c8000v c8000v- universalk9.qco Modern high- performance router Cisco Catalyst 9000v cat9kv cat9kv.qcow2 Enterprise- grade L2/L3 switching Arista vEOS veos veos.qcow2 Arista switch OS Fortinet FortiGate fortinet fortios.qcow2
## Ngfw, Utm

appliance Juniper vSRX vsrx vsrx.qcow2 Juniper firewall platform Palo Alto PAN- virtioa.qcow2 (rename if needed) May require multiple interfaces VyOS vyos virtioa.qcow2 Open-source router Checkpoint Gaia checkpoint virtioa.qcow2 Used for firewall testing
### How to Rename and Move Your Image Correctly

SSH into your EVE-NG VM (use Terminal or Cyberduck SCP): ssh root@<your-EVE-IP>
### Create the correct folder:

mkdir -p /opt/unetlab/addons/qemu/csr1000v
### Upload and rename image:

mv csr1000v-universalk9.16.12.01.qcow2 /opt/unetlab/addons/qemu/ csr1000v/csr1000v-universalk9.qcow2
### Fix permissions:

/opt/unetlab/wrappers/unl_wrapper -a fixpermissions
### Naming Rules (Important!)

Folder names must be exactly as listed above — case-sensitive and no spaces.
### Image files must end in .qcow2

Do not place multiple .qcow2 files in the same folder. If your image still doesn’t show, double-check: File extension
### Folder spelling

Permissions (chmod +x is not needed for .qcow2, only .bin in IOL) Verify in EVE-NG UI Refresh your browser
### Click Add Node

### Look under the correct vendor (e.g., Cisco, Fortinet)

Your image should appear, ready to drag into your topology!
### Bonus: Check What’s Already Installed

To list all QEMU images installed in your EVE-NG: ls /opt/unetlab/addons/qemu/ Summary for Beginners Key Step What to Do Use the right folder name Match EVE-NG official naming convention Rename .qcow2 file correctly Use proper filename (e.g., vios.qcow2) Run fixpermissions after upload To avoid permission issues Refresh EVE Web UI Newly added images will now show
### Here’s the updated section of your blog in Markdown format, integrating your

### new discovery about extracting QEMU-compatible Cisco images (ASAv, IOL-XE,

### IOLV2-XE) from CML’s reference platform ISO — and how to correctly rename

and integrate them into EVE-NG without hitting the 5-node limit of CML. How I Extracted Cisco Images from CML Without the 5-Node Limit
### If you’ve used Cisco Modeling Labs (CML) Free Community Edition, you’re

### probably aware of the 5-node restriction. But here’s a little-known hack:

### The refplat.iso (Reference Platform ISO) provided with CML contains

prebuilt QEMU-compatible images that work flawlessly on EVE-NG — without the CML licensing restrictions! Images Extracted from CML refplat.iso That Work on EVE-NG Image Type Folder Name in
## Eve-Ng

Final QEMU File Name Notes
## Iol-Xe

iol-xe virtioa.qcow2 XE-based IOS, useful for routers
## Iolv2-Xe

iolv2-xe virtioa.qcow2 L2/L3 XE image, more feature- rich ASAv asav asav.qcow2 Virtualized ASA firewall
### Steps to Add CML .qcow2 Images to EVE-NG Properly

These steps assume you’ve already extracted the .qcow2 files from refplat.iso. SSH into Your EVE-NG VM ssh root@<your-eve-ip>
### Create the Right Folder Structure

Each image goes into a separate directory inside EVE’s QEMU structure: mkdir -p /opt/unetlab/addons/qemu/asav mkdir -p /opt/unetlab/addons/qemu/iol-xe mkdir -p /opt/unetlab/addons/qemu/ iolv2-xe
### Move and Rename the Image

### Move your .qcow2 files into the appropriate directory and rename accordingly:

mv ~/Downloads/asav-9.12.qcow2 /opt/unetlab/addons/qemu/asav/asav.qcow2 mv ~/Downloads/iol-xe-17.3.1.qcow2 /opt/unetlab/addons/qemu/iol-xe/
### virtioa.qcow2

mv ~/Downloads/iolv2-xe-17.3.1.qcow2 /opt/unetlab/addons/qemu/iolv2-xe/
### virtioa.qcow2

### Make sure only one image per folder, and the filenames match EVE’s

expectations (asav.qcow2 or virtioa.qcow2).
### Fix Permissions

/opt/unetlab/wrappers/unl_wrapper -a fixpermissions How to Verify the Images in EVE-NG UI Open the EVE-NG Web UI Go to your lab topology Click Add New Node Select Cisco or use the search bar:
### Search IOL-XE, IOLV2-XE, or ASAv

Drag them into your topology and start your lab!
### These will run without CML’s 5-node restriction, giving you greater

flexibility for larger simulations and practice labs.
### Bonus: Where to Find refplat.iso

This ISO is bundled with CML releases. Once downloaded, you can mount it and
extract:
### hdiutil mount refplat.iso  # On macOS

### cp /Volumes/REFPLAT/images/*.qcow2 ~/Downloads/

Summary Table of CML to EVE-NG Integration Source File
## (Cml Iso)

Target Folder in EVE-NG New Filename Device Type asav-9.12.qcow /asav/ asav.qcow2 Firewall iol- xe-17.3.1.qcow2 /iol-xe/ virtioa.qcow2 Router iolv2- xe-17.3.1.qcow2 /iolv2-xe/ virtioa.qcow2 L2 Switch
### By combining these high-quality .qcow2 images from CML and correctly

### adapting them into your EVE-NG environment, you unlock a premium-grade

lab experience — without licensing or node limits.
### How are EVE-NG and PNetLab manage and share labs, both platforms are very

similar (PNetLab is essentially a fork of EVE-NG, so there's a lot of shared structure under the hood).
### What are .CFG files in EVE-NG?

These are the saved configurations of individual nodes (routers, switches, etc.) in your lab. Details:
### When you export or save a node's config from EVE-NG, it creates

a .CFG file. These are essentially device startup-configs (like show running-config).
### They’re stored in: /opt/unetlab/tmp/0/<lab-ID>/<node-ID>/configs/ or

in saved states: /opt/unetlab/labs/<your-lab-folder>/<your-node>.cfg Example: If your lab is called ccna-lab.unl, configs may be saved as: /opt/unetlab/labs/ccna-lab/node1.cfg Use: When you reboot or reopen the lab, EVE-NG uses the .cfg files to restore node states. You can manually edit or replace these configs to preload labs with desired router configs.
### What is a .UNL file?

A .unl file is a lab topology file, written in JSON/XML-like structure but with a .unl extension. Think of it as: “Blueprint” of the lab topology — but not the actual configs.
Contains:
### Node definitions (device types, image used, console port, etc.), Network links

### (how nodes are connected), Position info (where the icons are on the map),

Node startup configs can be linked, but not stored directly in .unl Location:
### /opt/unetlab/labs/<lab-folder>/<lab-name>.unl

### How do .UNL files relate to .CFG files?

.UNL file .CFG files Describes what the lab is Contains saved config per node Includes nodes, links, images Stores each node’s CLI state Can be shared/reused easily
### Must be copied to match node IDs

### If you import a .unl file, and don’t have the matching .cfg files, your nodes

will start with a default (blank) config unless the .unl also specifies saved states (like snapshots or configs in the same folder).
### Can you use PNetLab .UNL files in EVE-NG?

Yes, with minor tweaks. Both use the same core engine (UNetLab), and .unl file structure is nearly identical. How to use PNetLab .unl files in EVE-NG: Step-by-Step: Importing a
### PNetLab Lab into EVE-NG

### Here's a simple, clean step-by-step guide to import a full PNetLab lab into

EVE-NG — including .unl topology and config files — so it works correctly.
### Get the PNetLab Lab Files

Make sure you have:
### A .unl topology file (e.g. ccna-lab.unl)

Optional configs/ folder or .cfg files (node configurations) A list of required image names Example PNetLab lab folder: ccna-lab/ ├── ccna-lab.unl ├── configs/ ← optional │ ├── node1.cfg │ └── node2.cfg
### Transfer the Lab to EVE-NG

Use SCP or WinSCP or CyberDuck(MACOS) to copy the lab folder to your EVE-NG server: /opt/unetlab/labs/ Navigate to /opt/unetlab/labs/ Drag and drop the ccna-lab/ folder
### Fix Permissions

### Run the EVE-NG permission fixer:

/opt/unetlab/wrappers/unl_wrapper -a fixpermissions
### Match Image Names (If Needed)

### Open the .unl file:

nano /opt/unetlab/labs/ccna-lab/ccna-lab.unl Find lines like:
### <type>iou</type>

### <image>i86bi-linux-l2-adventerprisek9-15.1g.bin</image>

Make sure the image name matches what you actually have in: /opt/unetlab/addons/<type>/ You can either:
### Rename your image to match the .unl

OR update the .unl to use your image name
### Open the Lab in EVE-NG

Log in to EVE-NG web UI Navigate to:
### /Labs/ccna-lab/ccna-lab.unl

Open it — you should see the nodes and connections. Start the nodes and check if they load configurations (from .cfg files if available) Optional: Verify Node Configs If the lab included saved configs: Right-click a node > Start
### Open the console

### Verify the router/switch has config loaded

If it boots to blank config, the .cfg files may be missing or mismatched Troubleshooting Tips Issue Fix Node shows "missing image" Fix the image name in .unl or rename your image No configs loaded Make sure .cfg or configs/ folder exists and matches nodes File not showing in GUI Run fixpermissions and check folder structure Summary Task Command/Action
Upload lab scp or WinSCP to /opt/unetlab/ labs/ Fix permissions /opt/unetlab/wrappers/unl_wrapper -a fixpermissions Match image names Edit .unl or rename image files Open in EVE-NG UI Browse to the .unl in the Labs menu Confirm saved configs Ensure .cfg or configs/ matches node names/IDs
### ishare2-cli, is a powerful CLI tool designed specifically for managing EVE-NG

### image deployments using a shared cloud-based image repo. It's an open-

### source initiative from the iShare2 community, which maintains a massive repo

of prepackaged, ready-to-use EVE-NG images. What ishare2-cli Does: Feature Description Pull images easily Download EVE-NG images (Cisco, Palo, Fortinet, etc.) via a CLI. Handles import/convert Automatically places them in /opt/ unetlab/addons/, fixes permissions, and converts images. Works great on cloud Ideal for cloud-based EVE-NG setups (e.g., GCP, Azure, Oracle, Hetzner). Search & list images Find what’s available, filter by vendor/type, and pull only what you need.
### Ideal Use Case for You:

Since you're building labs using .unl files from PNetLab and want full control on
### a cloud-hosted EVE-NG server, ishare2-cli helps with:

Instantly downloading the correct image a .unl topology needs (e.g.
### vios-adventerprisek9-15.9-3)

### Auto-patching EVE-NG image folders with correct naming

Speeding up the whole import process (no more hunting for compatible .qcow2 files manually) Basic Setup & Usage (Simplified)
### Install ishare2-cli:

curl -fsSL https://raw.githubusercontent.com/ishare2-org/ishare2-cli/main/ install.sh | bash
### Use it:

ishare2 list # List all available images
### ishare2 search cisco     # Search for Cisco images

### ishare2 pull vios-l3     # Download and install the vIOS L3 image

### Example to fix permissions (done automatically, but just in case):

/opt/unetlab/wrappers/unl_wrapper -a fixpermissions Combine with Your .UNL Labs Import .unl lab as discussed earlier. See what images are required. Use ishare2-cli pull <image-name> to grab them quickly. Start lab in EVE-NG — all nodes should be recognized. Is it safe to use? Open-source, community-maintained
### No login required

### Pulls directly from a hosted repo (like GitHub Releases/CDN)

### Used widely by the EVE-NG & PNetLab community

You can inspect the source if concerned about security Resources:
### GitHub: ishare2-org/ishare2-cli

### List of supported images: ishare2 list or browse iShare2 CDN

## Part 1: VPS Providers with Nested Virtualization (KVM

Support)
### Here is a table of cloud providers that support KVM with nested virtualization,

critical for running EVE-NG and virtual router images: Provider Nested Virtualization KVM Support Notes Hetzner Yes Yes Best value VPS in EU. Ideal for labs. Vultr Yes Yes Enable nested virtualization in dashboard. Linode Yes (by request) Yes Easy to use; support may need to enable nested VT. UpCloud Yes Yes High performance with custom kernel support.
OVHcloud Yes Yes Supports nested VT via control panel. Netcup Yes Yes Excellent for budget labs in Europe. Contabo Yes Yes Massive specs for low cost; slower disks. Oracle Cloud Yes Yes Free tier supports nested VT (Ampere or
## Amd).

Scaleway Yes Yes France-based, developer- friendly. Cloud Provider Hypervisor Used Notes Amazon AWS Nitro Hypervisor (custom KVM) AWS moved from Xen to Nitro, a lightweight KVM-based hypervisor with near bare-metal performance. Microsoft Azure Hyper-V + custom extensions Azure’s base hypervisor is Hyper-V, used across VMs and AKS nodes. Google Cloud KVM (QEMU-based) GCP uses KVM, supports nested virtualization in some VM types. Oracle Cloud Xen + KVM (for some offerings) Xen for traditional compute; some newer offerings support KVM and bare metal. IBM Cloud KVM, PowerVM (for Power-based VMs) IBM supports both Intel and Power architectures. Alibaba Cloud KVM Same as GCP. Efficient for Linux-heavy workloads.
DigitalOcean KVM Lightweight and developer-friendly cloud. Platform Type Details VMware Fusion Type 2 macOS desktop virtualization. VMware Workstation Type 2 Windows/Linux desktop virtualization. VirtualBox Type 2 Popular open-source hypervisor. KVM/QEMU on Linux Type 1 Linux-native, used for EVE-NG, GNS3, lab setups. Proxmox VE Type 1 KVM-based, runs directly on hardware. ESXi Type 1 Direct hardware control, VMware’s enterprise hypervisor.
## Part 2: Step-by-Step Guide to Deploy EVE-NG on a Cloud VPS

### Requirements:

A VPS with: 4 vCPU, 8GB+ RAM, 40GB+ SSD, KVM + nested VT EVE-NG ISO: Download from eve-ng.net
### Step 1: Deploy Your VPS

Choose a KVM VPS from any provider above. Enable nested virtualization if not enabled by default. Step 2: Upload and Mount EVE-NG ISO Access VPS via noVNC/console or SSH. # Set hostname (optional) sudo hostnamectl set-hostname eve-ng # Install EVE-NG prerequisites
### apt-get install -y wget nano

### # Download and run EVE-NG installer script

wget https://www.eve-ng.net/repo/install-eve.sh chmod +x install-eve.sh
### ./install-eve.sh

OR Upload ISO using SCP or cloud provider dashboard. scp eve-ng.iso root@your-vps-ip:/root/ Step 3: Install EVE-NG
Boot from ISO. Follow installation prompts (use full disk). After installation, reboot and log in as root (default password: eve). Step 4: Basic Post-Install Config apt update && apt upgrade -y Set static IP if needed. Ensure qemu-kvm, bridge-utils, virt-manager are installed.
## Part 3: Automate Image Downloads Using iShare2-CLI

iShare2-CLI GitHub Step 1: Install Dependencies apt install python3 python3-pip git -y pip3 install rich requests
### Step 2: Clone and Run

git clone https://github.com/ishare2-org/ishare2-cli.git cd ishare2-cli python3 ishare.py Step 3: Download Images Run the tool and follow the terminal UI. It fetches router/firewall images (e.g., Cisco vIOS, FortiGate) from their open repository. Images are automatically placed in the correct EVE-NG folder.
## Part 4: Using iShare + EVE-NG Together

Create a lab in EVE-NG Web UI. Use nodes from imported images. Upload .unl lab files (from PNetLab if needed). Boot and test.
### Optional: Upload PNetLab Topologies to EVE-NG

### Copy .unl and configs/ folder into /opt/unetlab/labs/

Run fix permissions: /opt/unetlab/wrappers/unl_wrapper -a
### fixpermissions

Refresh EVE-NG GUI. Lab will show in the list. Deploying EVE-NG on the cloud unlocks professional-grade labbing anywhere.
### Combined with tools like iShare2-CLI, you can instantly populate your lab with

ready-to-use images — no need to hunt for them manually.
### Whether you're migrating from Packet Tracer or scaling up from GNS3, this

approach gives you a real-world simulation environment ready for CCNA/CCNP, security, and cloud hybrid labs.
Why Automate Image Downloads? No more wasting hours looking for Cisco, Juniper, Fortinet, or Palo Alto images. Easy to integrate with your local or cloud-deployed EVE-NG instance. One-click download and install with proper permissions set. Saves time when working with prebuilt topologies (like .unl files) from PNETLab or the community.
### Prerequisites

EVE-NG is already installed (locally via VMware or on a cloud VPS). SSH or terminal access to your EVE-NG shell. Internet access from within the EVE-NG VM.
### Yes, you can absolutely use ishare2-cli on your local EVE-NG VM

### running in VMware Fusion. In fact, this is a great way to:

Test the setup and understand how ishare2 works. Download and organize images before deploying on a cloud server. Avoid wasting cloud resources (and cost) during your learning phase.
### Image Automation for EVE-NG with ishare2-cli

### As part of my journey from Packet Tracer to EVE-NG and beyond, I quickly

### realized that one of the most frustrating bottlenecks was hunting for reliable

### and compatible device images online. Forums were inconsistent, links expired,

and half the time I was unsure if the image would even work.
### That all changed when I discovered ishare2-cli — an open-source CLI tool built

to integrate with the iShare2 image repo. It acts like a package manager for EVE-NG device images. Here's How to Use ishare2-cli on Your Local VMware EVE-NG:
### Prerequisites:

Your EVE-NG VM is running on VMware Fusion, fully installed and updated. You have SSH access or console access into the EVE-NG shell. Your EVE-NG VM has internet access (NAT or bridged network works fine).
### Step-by-Step: Installing ishare2-cli Inside Your EVE-NG VM

# Step 1: SSH into your EVE-NG VM or open terminal in console
### ssh root@<eve-ip-address>

# Step 2: Download and install ishare2-cli (official repo)
apt update
### apt install -y python3-pip git

git clone https://github.com/ishare2-org/ishare2-cli.git cd ishare2-cli
Chmod +x ./install.sh RUN ./install.sh pip3 install -r requirements.txt
### Ishare2 [action]

This tool will now be ready to download .image files directly into your /opt/ unetlab/addons directory.
### Search & Pull Workflow

# Search for available images (e.g., iosv, iol, asav)
ishare2.py search iosv
### # Pull a specific image from the results

ishare2.py pull dynamips | iol | qemu <ReferenceNumber> What Happens During Image Pull?
### When you run pull, ishare2-cli does the following:

Searches for the requested image by name. Downloads the .image file to the appropriate folder: qemu images → /opt/unetlab/addons/qemu/ iol images → /opt/unetlab/addons/iol/
### dynamips → /opt/unetlab/addons/dynamips/

The image is not automatically renamed or moved into a subfolder. Manual step: Rename .image to virtioa.qcow2 (or required filename).
### Create a directory for the image and move it inside:

### mkdir /opt/unetlab/addons/qemu/iosv-15.6-2T

mv iosv-15.6-2T.image /opt/unetlab/addons/qemu/iosv-15.6-2T/virtioa.qcow2
### Final Step: Fix Permissions

### /opt/unetlab/wrappers/unl_wrapper -a fixpermissions

This ensures the web UI can detect and launch the image.
### Pro Tip — Beware of vios_l2-adventerprisek9-M

### This image often hangs during boot, responds slowly, and has known limitations

with EtherChannel/LACP. If you need a reliable switch lab, consider IOL L2, or newer vIOS-L2 builds instead.
### Some images like Arista vEOS use the same base image for both router and

### switch roles. In such cases, the folder name determines how the node appears

in EVE-NG. You may need to manually rename the folder to veos or veos-router depending on your use case. The difference between the vEOS Router and the vEOS Switch in EVE-NG lies in: Type Directory Name Role in Lab
Router /opt/unetlab/addons/ qemu/veos-router L3 functionalities Switch /opt/unetlab/addons/ qemu/veos
### L2 switching

### Common Causes of IOL L2 Crashes - a known issue with some IOL L2

### images, particularly ones like i86bi_Linux-L2-Adventerprisek9-

ms.SSA.high_iron_20190423. These are often buggy or unstable in EVE-NG Cause Explanation Fix/Workaround Corrupt image Image might be partially broken during transfer or download Try redownloading from a known stable source Wrong platform/ emulation EVE-NG expects IOL images with specific naming & behavior Rename correctly and ensure .bin not .qcow2 Missing license (iourc) IOL requires a valid iourc license file Make sure /opt/ unetlab/addons/iol/bin/ iourc is present and valid Faulty build Some images like high_iron are known to crash Try using a more stable version like i86bi-linux-l2- adventerprisek9-15.1g .bin Wrong permissions EVE can’t access or boot properly Run unl_wrapper -a fixpermissions after any image work Why Test Locally? You avoid cloud billing while learning. You can verify images are working (console boots up, etc). Once happy, you can migrate this .qcow2 library to a cloud server later.
### Estimate: Number of Nodes You Can Run

### Here’s a quick estimate of the types of images you can run and how many,

assuming 12GB RAM assigned to EVE-NG and efficient CPU usage. Image Type RAM per Node vCPU per Node Est. Max Nodes Use Case Cisco IOL (Layer 2/3)
## 128Mb–

## 256Mb

~5–10% 15–25 nodes CCNA/CCNP switching/ routing
Cisco vIOS- L2/L3
## 512Mb–

## 768Mb

~10–20% 6–10 nodes More realistic IOS XR labs MikroTik CHR
## 256Mb

Low 10–15 nodes Routing/ Firewall labs FortiGate (low mem)
## ~1024Mb+

Moderate 4–6 nodes Security labs Windows 7/10
## 1.5Gb–2Gb

Moderate/ High 2–3 max Heavy, only for AD/ domain labs Ubuntu CLI only
## 512Mb

Low 6–10 nodes Kali, OpenVPN, Auth, etc.
### No—you shouldn’t need to resort to guestfish or manually mount the QCOW2

to tweak it, as long as you’re using ishare2-cli to pull your images.
### ishare2-cli already:

### Downloads the image in a ready-to-use format

Places it in the correct /opt/unetlab/addons/<type>/<imagename>/ folder
### Renames it to virtioa.qcow2 (or the appropriate default filename)

### Leaves it fully configured for EVE-NG’s defaults

The only time you’d need to mount and edit with guestfish (or qemu-nbd, etc.)
### is if you want to:

Inject custom files (license files, scripts, certificates) into the image
### before first boot

Change default credentials or other OS-level settings baked into the image
### Strip out unwanted services to slim it further

### But for standard lab use—especially following the EVE-NG “HowTo” docs—

### you can skip all that. After your ishare2 pull <image> and /opt/unetlab/

wrappers/unl_wrapper -a fixpermissions, just add the node in the GUI and boot it. If you do need to make small OS-level tweaks (e.g. adding SSH keys, custom banners), I’d recommend: # 1. Load the image locally for editing apt install libguestfs-tools guestfish --ro -a virtioa.qcow2 # 2. At the guestfish prompt: > run
### > mount /dev/sda1 /

> edit /etc/ssh/sshd_config # or copy-in files > exit But again—not required for any ishare2-managed image that’s otherwise
10.
unmodified. You can do all of this inside your EVE-NG VM—no need to jump back to your desktop. Here’s how:
### Install the GuestFS Tools

SSH into your EVE-NG VM (or open its console):
### ssh root@<eve-ip>

### Install the guestfish package (it provides guestfish, virt-cat, etc.):

apt update && apt install -y libguestfs-tools
### Locate Your Image File

### By default, an image you pulled with ishare2-cli lives under:

/opt/unetlab/addons/<type>/<image-folder>/virtioa.qcow2
### For example:

/opt/unetlab/addons/qemu/iosv-15.6-2T/virtioa.qcow2
### Mount (Read-Write) with Guestfish

Warning: Always work on a copy of the QCOW2 if you care about the original!
### Make a copy to play safe:

cd /opt/unetlab/addons/qemu/iosv-15.6-2T/ cp virtioa.qcow2 virtioa-edit.qcow2 Launch guestfish in read-write mode: guestfish --rw -a virtioa-edit.qcow2
### At the guestfish> prompt, run:

### run                      # discover the partitions

### list-filesystems         # see which device has / (e.g. /dev/sda1)

### mount /dev/sda1 /        # mount root partition

Edit or copy files. You can use guestfish’s built-in editor or copy files in/out:
### edit /etc/hostname       # built-in editor

copy-in /root/mykey /root/.ssh/authorized_keys # inject your SSH key Unmount and quit: umount / exit
### Replace the Original (Optional)

Once you’ve validated your changes:
### mv virtioa-edit.qcow2 virtioa.qcow2

### /opt/unetlab/wrappers/unl_wrapper -a fixpermissions

Then boot the node in EVE-NG; it will use your edited image.
### Alternative: QEMU-NBD

If you prefer, you can also use QEMU’s network block device: modprobe nbd max_part=8
qemu-nbd --connect=/dev/nbd0 virtioa.qcow2 mount /dev/nbd0p1 /mnt # make edits under /mnt umount /mnt qemu-nbd --disconnect /dev/nbd0 Both methods achieve the same result—pick whichever you find more comfortable. -machine type=pc,accel=kvm \ -cpu host \ -smp cores=2,threads=1,sockets=1 \ -device virtio-scsi-pci,id=scsi0 \ -drive file=disk1.qcow2,if=none,id=hd0,cache=none,format=qcow2 \ -device scsi-hd,drive=hd0 \ -netdev type=tap,id=net0,script=/etc/qemu-ifup \ -device virtio-net-pci,netdev=net0 \ -nographic \ -serial mon:stdio \ -nodefaults \ -rtc base=utc
### Catalyst 8000v Version Recommendation

In EVE-NG labs you want a balance between up-to-date features and resource usage. Here’s a quick pick:
### Recommendation:

For resource-constrained setups, start with c8000v-17.04.01 (1.3 GiB). For production-like CCNP Enterprise labs, use c8000v-17.09.01a (1.6 GiB) as a sweet spot. If you need the latest enhancements, go with c8000v-17.16.01a (1.7 GiB).
### Custom QEMU Template for CSR1000v

If you’re using a custom QEMU template (shown below) and seeing CSR1000v boot failures: -machine type=pc,accel=kvm \ -cpu host \ -serial mon:stdio \ -nographic \ -no-user-config \ -nodefaults \ -rtc base=utc
### Recommended Template Settings

### Use EVE-NG’s built-in CSR1000v template or adjust your custom stanza to

include the virtio devices and proper flags:
-machine type=pc,accel=kvm \
-cpu host \
-smp cores=2,threads=1,sockets=1 \
-m 2048 \
-device virtio-scsi-pci,id=scsi0 \
-drive file=disk1.qcow2,if=none,id=hd0,cache=none,format=qcow2 \
-device scsi-hd,drive=hd0 \
-netdev type=tap,id=net0,script=/etc/qemu-ifup \
-device virtio-net-pci,netdev=net0 \
-nographic \
-serial mon:stdio \
-nodefaults \
-rtc base=utc
### Key differences:

-smp cores=2,threads=1,sockets=1 binds 2 vCPUs in one socket.
-device virtio-scsi-pci and -device scsi-hd for disk bus.
-device virtio-net-pci for network.
-m 2048 allocates 2 GB RAM.
With these settings, CSR1000v will find its packages, start critical services (nesd, etc.), and boot cleanly.
### CSR1000v User Access Verification

On first boot, CSR1000v prompts for user access. Common credential pairs include: Username: cisco Password: cisco # or sometimes Username: admin Password: admin
### If neither pair works:

Use the VM console (right-click node > Console) to log in if possible. At the firepower-bash prompt, enter configuration mode to reset or create a local user: enable
### configure terminal

username myuser privilege 15 secret MySecretPassword end write memory Reconnect with your new credentials.
### If you cannot reach an enable prompt, ensure your template uses the builtin

### CSR1000v startup configuration, or reload the node and watch for the initial

banner that shows the correct default credentials.
### Recommended IOS XRv-9000 (XRv9k) Lab Images

### When choosing an XRv9k build for CCNP/MPLS or service-provider labs, you

### want enough features to practice routing protocols (OSPF, BGP, MPLS) but not

so heavy it crashes your host. Below are the disk size (for reference) and the approximate RAM you should allocate:
Image Disk Size Approx. RAM Required Feature Notes Recommen dation iosxrv9000 -7-7-1 1.5 GiB 2 GiB Early 7.x feature set; stable Good balance of features and resources iosxrv9000 -7-11-1 1.7 GiB 2.5 GiB More recent bug fixes and updates
Recommend ed if you have extra headroom xrv9k- fullk9-24.3. 1.6 GiB 3 GiB Newest 24.x train; advanced features Use for feature-com plete labs (if RAM allows) xrv9k- fullk9-6.4.1 1.2 GiB 1.5 GiB Lightweight 6.x build Fast boot and minimal resources xrv-k9- demo-6.3.1 431 MiB 512 MiB Demo mode (limited features) Only use for very basic connectivity tests
### Recommendation:

### For CCNP/SP routing labs, start with iosxrv9000-7-7-1 (allocate

2 GiB RAM) or xrv9k-fullk9-6.4.1 (allocate 1.5 GiB RAM) for best stability.
### If you need the latest enterprise features, pick iosxrv9000-7-11-1

(2.5 GiB RAM) or xrv9k-fullk9-24.3.1 (3 GiB RAM).
### The demo build (xrv-k9-demo-6.3.1) is too limited and only requires

~512 MiB but lacks full features—avoid unless you’re only testing basic L2/L3 connectivity.
### Infra Server Images for EVE-NG

### To round out your CCNA/CCNP infrastructure labs, you’ll need lightweight

### server images for DNS, DHCP, syslog, and Active Directory. Here are the

recommended images and their pull commands: Server Type Image Name Approx. RAM ishare2 Pull Command
Alpine Linux alpine-3.18- x86_64.qcow2 128 MiB python3 ishare.py --pull alpine-3.18.imag Ubuntu Server ubuntu-22.04- server-cloudimg 512 MiB python3 ishare.py --pull ubuntu-22.04.i mage Windows Server 2019 windows- server-2019- standard.qcow2 2 GiB Manual download (Microsoft Eval
## Iso)

Notes: Alpine is perfect for lightweight services (DNS, DHCP, syslog). Ubuntu Server offers richer distro support (RADIUS, NTP). Windows Server requires a valid ISO; upload to /opt/unetlab/addons/ qemu/windows/, then convert to QCOW2.
### Converting a Windows Server ISO to QCOW2 for EVE-NG

### If you already have the Windows Server ISO on your host, follow these steps

inside your EVE-NG VM to create a usable QCOW2 disk image:
### Create the target folder

mkdir -p /opt/unetlab/addons/qemu/windows/windows-server-2019- standard cd /opt/unetlab/addons/qemu/windows/windows-server-2019- standard Copy the ISO into place cp /path/to/windows-server-2019.iso . Create a blank QCOW2 disk (e.g., 60 GB) qemu-img create -f qcow2 disk0.qcow2 60G Install Windows via virt-install virt-install \ --name win2019 \ --ram 2048 \ --vcpus 2 \ --disk path=disk0.qcow2,format=qcow2 \ --cdrom windows-server-2019.iso \ --os-type windows \ --os-variant win2k19 \ --network network=default,model=virtio \ --graphics none \ --boot cdrom,hd Complete the Windows GUI install via VNC or serial console.
### Fix permissions and rename for EVE-NG

/opt/unetlab/wrappers/unl_wrapper -a fixpermissions
### Add the node in the EVE-NG GUI

Choose QEMU > Windows > Windows Server 2019
### Assign disk0.qcow2 as the image

### Your Windows Server VM will now boot from the installed QCOW2 disk. This

approach avoids manual conversion pitfalls and ensures a fully installed, persistent OS in EVE-NG.
### This series of commands sets up a virtualized Ubuntu 16.04 desktop

### environment inside EVE-NG, using QEMU for virtualization. Here's what each

step does, with an explanation of how it relates to virtualization concepts like VMDK in VMware Fusion: Step-by-Step Breakdown:
### Rename ISO image

### mv ubuntu-16.04.2-desktop-amd64.iso cdrom.iso

This renames the Ubuntu ISO file to cdrom.iso. EVE-NG expects a file named cdrom.iso when booting a VM from an ISO during the first boot. The ISO acts like a virtual DVD drive.
### Navigate to QEMU image directory for the VM template

### cd /opt/unetlab/addons/qemu/linux-ubuntu-desktop-16.04.02/

This is the path where EVE-NG stores its QEMU-based VM images (one folder per node/template). You're entering the directory specific to your custom Ubuntu Desktop node.
### Create a virtual hard drive

### /opt/qemu/bin/qemu-img create -f qcow2 virtioa.qcow2 30G

This is the key step: you're creating a virtual hard disk for your Ubuntu node. qcow2 is QEMU’s advanced disk format (similar to .vmdk in VMware). It supports compression, snapshots, and dynamic sizing.
### virtioa.qcow2 is the name of the disk. "Virtio" refers to a high-

performance virtualized driver used in KVM/QEMU VMs. 30G specifies a max disk size of 30 GB (like allocating a 30 GB VMDK in VMware Fusion). This is what Ubuntu will install onto during the first boot from the ISO.
### Comparison to VMware Fusion:

Think of this as creating a new .vmdk for a VMware VM before installing an OS. You're defining how much space the VM can use, but actual disk usage grows as needed.
### Create a lab and add the node

You now go into EVE-NG's web interface and create a lab. Add a node that uses the linux-ubuntu-desktop-16.04.02 QEMU template. When this node boots, it will load the cdrom.iso to install Ubuntu onto virtioa.qcow2.
### Remove the ISO after installation

### rm -f cdrom.iso

After the OS has been installed onto the virtual hard disk, the ISO is no longer needed.
### Removing it simulates "ejecting the installation disc."

Ensures the VM boots from the disk next time instead of looping back to the ISO.
### This summary is conceptually identical to:

### Creating a new virtual disk (VMDK) in VMware,

### Mounting an ISO to boot and install the OS, and

Removing the ISO after installation to boot normally from the virtual hard disk.
### But here you're doing it manually with QEMU inside EVE-NG, which runs as a

nested virtualization environment (on top of VMware, Proxmox, etc.).
### Absolutely! Here's a unified, clean, custom guide for installing your own

### Linux or Windows Server host in EVE-NG, abstracted from the official EVE-

NG documentation. It works for both platforms and is structured for reuse with minimal manual steps. EVE-NG Custom Image Installation Guide (Linux or
### Windows Host)

Applies to: Linux Desktops, Linux Servers, Windows Desktop, Windows Server Tested with: Ubuntu, Kali, TinyCore, Windows 10/11, Server 2016/2019/2022
### Step 1: Prepare Environment & ISO

### Upload the ISO to EVE via SCP (e.g., using FileZilla or scp):

scp your-image.iso root@<eve-ng-ip>:/opt/unetlab/addons/qemu/ Rename ISO to cdrom.iso: mv your-image.iso cdrom.iso
### Step 2: Create the Image Folder

Use naming convention: linux-[name]-version or windows-[name]-version. mkdir /opt/unetlab/addons/qemu/<custom-folder-name>
### mv cdrom.iso /opt/unetlab/addons/qemu/<custom-folder-name>/

cd /opt/unetlab/addons/qemu/<custom-folder-name> Example:
### mkdir /opt/unetlab/addons/qemu/linux-kali-2022.1

mv kali-linux-2022.1-installer-amd64.iso /opt/unetlab/addons/qemu/linux- kali-2022.1/cdrom.iso
### Step 3: Create HDD (qcow2 format)

Choose desired size (e.g., 40 GB for Windows, 15–30 GB for Linux). /opt/qemu/bin/qemu-img create -f qcow2 virtioa.qcow2 30G Step 4: Boot and Install OS Open EVE Web UI
### Create a new Lab

Add Node using the name of the folder you created Start the VM — it will boot from the ISO Install the OS manually For Linux: Install to /dev/vda For Windows: Use the VirtIO drivers if required Step 5: Post-Install Cleanup (Commit) After the OS is installed: Power off the VM
### SSH back into EVE and run:

cd /opt/unetlab/addons/qemu/<your-image-folder>
### rm -f cdrom.iso

### /opt/unetlab/wrappers/unl_wrapper -a fixpermissions

This finalizes the image so it can be cloned as a reusable node.
### Boot Kali VM in your EVE-NG lab with the cdrom.iso attached

### Install Kali to the virtioa.qcow2 hard disk

This is the key step — ensure Kali is fully installed onto the virtual HDD
### Reboot Kali

### During reboot, Kali should boot from virtioa.qcow2, not the ISO

If it boots correctly and logs you into the installed OS, the ISO is no
### longer needed

At this point, you can safely delete cdrom.iso Optional Enhancements For Windows: Use VirtIO drivers during install: Download Red Hat VirtIO ISO Place the ISO alongside your main one:
### mv virtio-win.iso /opt/unetlab/addons/qemu/<your-image-folder>/

Load it during Windows install for disk/network drivers. For Cloud-Like Linux:
### Pre-install qemu-guest-agent

Configure SSH access or cloud-init (advanced) Final Test
### Add the node to a new lab

### Boot it — confirm it loads from disk (virtioa.qcow2)

Save it as part of your personal reusable image library Naming Convention (Recommended) OS Type Example Folder Name Linux linux-ubuntu-server-22.04 Linux linux-kali-rolling-2024 Windows windows-server-2022 Windows windows10-enterprise-21h2 Script Template (Advanced Automation) You can turn this into a shell script: #!/bin/bash
### # Custom EVE-NG image initializer

### read -p "Enter image folder name (e.g., linux-ubuntu-server-22.04): " IMGDIR

### read -p "Enter HDD size (e.g., 30G): " SIZE

### mkdir -p /opt/unetlab/addons/qemu/$IMGDIR

mv cdrom.iso /opt/unetlab/addons/qemu/$IMGDIR/
### cd /opt/unetlab/addons/qemu/$IMGDIR

### /opt/qemu/bin/qemu-img create -f qcow2 virtioa.qcow2 $SIZE

/opt/unetlab/wrappers/unl_wrapper -a fixpermissions echo " Folder $IMGDIR is ready. Add to a lab and install OS."
### Let me know if you'd like:

### A version that includes cloud-init support for Ubuntu

### Pre-installed lab templates (e.g., AD + Linux + Router)

A Markdown version for your documentation/blog
### Quick summary of what that means:

### When you boot into emergency mode (via GRUB or a recovery

### environment), you’re actually running a minimal Linux shell on your real

system, but without starting all the usual services.
### You have direct access to your files (like /etc/network/interfaces) and

can edit them to fix problems blocking normal boot.
### So yes, you are “in” your Linux filesystem, but it’s a minimal

environment designed for troubleshooting. How to ask an AI to get the recovery steps again:
### Try asking something like:

“How do I recover a Linux system that won’t boot because of a
### bad network config?”

“Steps to boot into emergency mode on Ubuntu/EVE-NG and fix /
### etc/network/interfaces”

“How to fix networking errors causing systemd networking
### service failure on Linux?”

“How to repair broken network config in Linux when system won’t start networking?”
### Explanation:

eth0 and eth1 are the physical NICs on your EVE-NG host. pnet0 and pnet1 are Linux bridge interfaces connected to eth0 and eth1 respectively. Both bridges are set to get IP via DHCP from your home LAN/network (or wherever your EVE-NG host is connected).
### This allows your VMs or nodes attached to these clouds (pnet0, pnet1)

to get IPs from your DHCP server and access the internet. bridge_fd 0 disables forwarding delay (good for faster bridge startup).
### Troubleshooting tips:

Make sure eth0 and eth1 are physical interfaces actually present on your host (ip link show). Make sure your DHCP server is active on the physical network your EVE-NG host is connected to. If you want to use only one interface, configure only pnet0 as above.
### Don’t mix manual and dhcp on the same interface in confusing ways;

keep physical interfaces manual, bridges dhcp. A clear explanation of how macOS turns bridge101 into a NAT gateway and
### what it means for your EVE-NG lab:

### Think of a server—the hardware—as one computer. It can be one of the blades,

a powerful computer you can buy at the local computer store... whatever. Traditionally, when you think of one server, that one server runs one OS. Inside,
### the hardware includes a CPU, some RAM, some kind of permanent storage (like

### disk drives), and one or more NICs. And that one OS can use all the hardware

inside the server and then run one or more applications.
### With the physical server model shown in Figure 15-2, each physical server runs

### one OS, and that OS uses allthe hardware in that one server. That was true of

servers in the days before server virtualization. Today, most companies instead
### create a virtualized data center. That means the company purchases server

### hardware, installs it in racks, and then treats all the CPU, RAM, and so on as

### capacity in the data center. Then, each OS instance is decoupled from the

### hardware and is therefore virtual (in contrast to physical). Each piece of

### hardware that we would formerly have thought of as a server runs multiple

instances of an OS at the same time, with each virtual OS instance called a virtual machine, or VM.
### A single physical host (server) often has more processing power than you need

### for one OS. Thinking about processors for a moment, modern server CPUs have

### multiple cores (processors) in a single CPU chip. Each core may also be able to

### run multiple threads with a feature called multithreading. So, when you read

about a particular Intel processor with 8 cores and multithreading (typically two
### threads per core), that one CPU chip can execute 16 different programs

### concurrently. The hypervisor (introduced shortly) can then treat each available

thread as a virtual CPU (vCPU) and give each VM a number of vCPUs, with 16 available in this example.
### A VM—that is, an OS instance that is decoupled from the server hardware—still

### must execute on hardware. Each VM has configuration as to the minimum

### number of vCPUs it needs, minimum RAM, and so on. The virtualization system

### then starts each VM on some physical server so that enough physical server

### hardware capacity exists to support all the VMs running on that host. So, at any

one point in time, each VM is running on a physical server, using a subset of the
### CPU, RAM, storage, and NICs on that server. To make server virtualization work,

### each physical server (called a host in the server virtualization world) uses a

### hypervisor. The hypervisor manages and allocates the host hardware (CPU,

### RAM, etc.) to each VM based on the settings for the VM. Each VM runs as if it is

### running on a self-contained physical server, with a specific number of virtual

### CPUs and NICs and a set amount of RAM and storage. For instance, if one VM

### happens to be configured to use four CPUs, with 8 GB of RAM, the hypervisor

allocates the specific parts of the CPU and RAM that the VM actually uses.
### Server virtualization tools provide a wide variety of options for how to connect

### VMs to networks. Normally, an OS has one NIC, maybe more. To make the OS

work as normal, each VM has (at least) one NIC, but for a VM, it is a virtual NIC. (For instance, in VMware’s virtualization systems, the VM’s virtual NIC goes by
### the name vNIC.)

### Finally, the server must combine the ideas of the physical NICs with the vNICs

### used by the VMs into some kind of a network. Most often, each server uses

### some kind of an internal Ethernet switch concept, often called (you guessed it)

### a virtual switch, or vSwitch. Interestingly, the vSwitch can be supplied by the

### hypervisor vendor or by Cisco. For instance, Cisco offers the Nexus 1000VE

### virtual switch (which replaces the older and popular Nexus 1000V virtual

### switch). The Nexus 1000VE runs the NX-OS operating system found in some of

the Cisco Nexus data center switch product line.
### The vSwitch shown in Figure 15-4 uses the same networking features you now

### know from your CCNA studies; in fact, one big motivation to use a vSwitch from

### Cisco is to use the same networking features, with the same configuration, as

in the rest of the network. In particular:
### Ports connected to VMs: The vSwitch can configure a port so that the VM will

be in its own VLAN, or share the same VLAN with other VMs, or even use VLAN trunking to the VM itself.
### Ports connected to physical NICs: The vSwitch uses the physical NICs in the

### server hardware so that the switch is adjacent to the external physical LAN

switch. The vSwitch can (and likely does) use VLAN trunking.
### Automated configuration: The configuration can be easily done from within

### the same virtualization software that controls the VMs. That programmability

### allows the virtualization software to move VMs between hosts (servers) and

reprogram the vSwitches so that the VM has the same networking capabilities no matter where the VM is running. How macOS Uses bridge101 for NAT in VMware Fusion What is bridge101? bridge101 is a virtual network interface created by VMware Fusion on macOS
### when you choose:

Network Adapter → Internet Sharing (Share with my Mac)
### (This is the NAT option in Fusion.)

This setting makes your Mac act like a mini-router (NAT gateway).
### What Happens Under the Hood

VMware Fusion creates bridge101 on your Mac. bridge101 is assigned an IP, e.g.: inet 172.16.100.1 netmask
### 255.255.255.0

A DHCP server on the Mac assigns IPs like 172.16.100.100+ to any VMs using this network. macOS uses pf (Packet Filter) and natd/ipfw (or internal NAT
### rules) to:

Translate VM traffic from 172.16.100.x → your public Mac IP. Forward internet responses back to the correct VM.
### Result: NAT Access for VMs

Your EVE-NG VM (and any nodes using Cloud1 → pnet1) behave just like home
### devices behind a Wi-Fi router:

Each gets a private IP in 172.16.100.0/24. Your Mac acts like the router, NAT’ing outbound traffic. All internet traffic appears to come from your Mac’s real IP.
### Example Flow

Kali (via Cloud1 → pnet1) gets IP 172.16.100.20 via DHCP. Kali pings 8.8.8.8 → goes out eth1 → pnet1 → VMware Fusion → bridge101.
macOS NATs 172.16.100.20 → your Mac's external IP (e.g., 192.0.2.10). Google DNS replies → your Mac receives it → NAT translates back to Kali.
### What you've just done — setting up multiple interfaces (pnet0, pnet1) for

### different purposes — mirrors real-world enterprise network segmentation and

### lab design. Here's how it aligns with network engineering practices:

Common Use Cases for Multiple Interfaces in Labs Interface Typical Purpose Real-World Analogy pnet0 Management interface Out-of-band access to routers/switches or the lab environment itself (like SSH, web GUI, updates) pnet1 Cloud/Internet access for internal nodes WAN/uplink to internet or connection to external services (e.g., firewall > ISP) pnet2+ Additional lab segments or security zones DMZ, internal VLANs, partner networks, guest Wi-Fi, etc.
### A key concept in how EVE-NG integrates with your host

### When you add a new network adapter (like eth1) in VMware Fusion, it creates

### a new physical interface inside the EVE-NG virtual machine. EVE-NG then

exposes this interface as a pnet bridge (like pnet1). Until that adapter exists:
### EVE-NG doesn’t list pnet1 internally

So objects like Cloud1 won’t appear as available options in the GUI You can’t link them to your lab nodes
### How It Works:

### eth0 (from VMware) → becomes pnet0 in EVE-NG → maps to Cloud0

### eth1 (newly added) → becomes pnet1 → maps to Cloud1

So when you added Network Adapter 2 in VMware:
### It mapped to eth1 inside the VM

### You configured /etc/network/interfaces to create pnet1

Now EVE-NG sees it and Cloud1 becomes usable Summary:
VMware Fusion Adapter Inside EVE-NG EVE-NG Object Typical Use Network Adapter 1 eth0 pnet0/Cloud0 Management interface Network Adapter 2 eth1 pnet1/Cloud1 Internet or
### external access

### Let’s add two more network adapters (for pnet2 and pnet3), you'll need to

edit /etc/network/interfaces to bring them online properly. Below is a clean, working example that includes:
### pnet0 (NAT – already working)

### pnet1 (already working, probably Internet Sharing or similar)

pnet2 (Bridged Networking - Auto-detect/WiFi) pnet3 (Private to my Mac – Host-only) Why this config works: Interface Adapter type IP Config Purpose pnet0 NAT DHCP Internet from Fusion NAT pnet1 Shared with Mac DHCP Cloud1-style internal network pnet2 Bridged (Auto/ Wi-Fi) DHCP VM gets IP from same LAN as Mac pnet3 Host-only Static IP Local mgmt network, no Internet Your Current Setup in VMware Fusion Adapter VMware Setting
## Eve-Ng

Interface Function Backing macOS Interface Adapter 1 Share with my Mac
## (Nat)

eth0 → pnet0 Management access (Web
## Ui, Ssh)

bridge101 Adapter 2 Share with my Mac
## (Nat)

eth1 → pnet1 Internet access for EVE VMs bridge101 Adapter 3 Private to my Mac (Host-only) eth2 → pnet2 Internal / Isolated network bridge100 What Each Means
### NAT – "Share with my Mac" → bridge101

macOS runs a local DHCP server behind a NAT. Your EVE-NG VM gets private IPs like 172.16.100.x (behind bridge101). Outbound traffic (from EVE) is NATed to your Mac’s IP for Internet. Good for safe Internet access, but devices outside can't reach your EVE VM directly. This is what powers pnet0 and pnet1.
### Host-Only – "Private to my Mac" → bridge100

EVE-NG and your Mac can talk to each other, but no Internet. This is a separate network from Wi-Fi or LAN. The IPs you see like 172.16.228.x are issued by macOS's internal
## Dhcp.

You can use this to test isolated lab environments between your Mac and your VMs. Note: It just happens to use 172.16.228.x — same private IP range, but different from NAT's 172.16.100.x. Summary of Differences Feature NAT (bridge101) Host-only (bridge100) Internet access Yes (via NAT) Mac ↔ VM communication Yes Yes VM ↔ VM communication Yes Yes External access to VM No (unless port forward) Useful for Management, Internet Internal lab networks
### Why "Bridged" Broke Boot

### When you added Bridged Networking (Auto/Wi-Fi):

Your VM tried to join the same LAN/Wi-Fi as your Mac. But Wi-Fi bridge mode can be buggy in VMware Fusion, especially for EVE-NG. If DHCP fails or there’s a delay, the system can hang at boot trying to get an IP. So it was wise to remove it — NAT and Host-only are much more stable for local lab use. Clean /etc/network/interfaces Configuration # /etc/network/interfaces # EVE-NG Multi-NIC Configuration: NAT + Host-only # Loopback interface auto lo
iface lo inet loopback ######################################## # Adapter 1: Management & Internet (NAT) # VMware Fusion: Shared with my Mac ######################################## auto pnet0 iface pnet0 inet dhcp bridge_ports eth0 bridge_stp off pre-up ip link set dev eth0 up ######################################## # Adapter 2: Lab Internet (NAT) # VMware Fusion: Shared with my Mac ######################################## auto pnet1 iface pnet1 inet dhcp bridge_ports eth1 bridge_stp off pre-up ip link set dev eth1 up ######################################## # Adapter 3: Host-only Network # VMware Fusion: Private to my Mac ######################################## auto pnet2 iface pnet2 inet static bridge_ports eth2 bridge_stp off pre-up ip link set dev eth2 up address 192.168.200.1 netmask 255.255.255.0 sudo ifdown pnet0 && sudo ifup pnet0 sudo ifdown pnet1 && sudo ifup pnet1 sudo ifdown pnet2 && sudo ifup pnet2


---

*Document converted from PDF: 🚀 From Packet Tracer to Multi-Vendor Labs: Understanding Virtual….pdf*
